from django.test import TestCase,  Client
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User
from rest_framework import status
from django.utils import timezone
from Restaurant.models import Menu, Booking
from Restaurant.serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='password')

        self.icecream = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        self.coffee = Menu.objects.create(Title='Coffee', Price=10, Inventory=50)
        self.salad = Menu.objects.create(Title='Salad', Price=25, Inventory=75)

    def loginAsTestUser(self) -> None:
        self.client.login(username='user', password='password')

    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('protected_menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.loginAsTestUser()
        response = self.client.get(reverse('protected_menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_menu_items(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('protected_menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)



class BookingViewSetTest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='user', password='password')

        self.booking1 = Booking.objects.create(Name = 'Alice', No_of_guests = 1, BookingDate = timezone.now())
        self.booking2 = Booking.objects.create(Name = 'Bob', No_of_guests = 5, BookingDate = timezone.now())

    def loginAsTestUser(self) -> None:
        self.client.force_authenticate(user=self.user)

    def test_get_all_bookings(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)


    def test_get_single_booking(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        booking = Booking.objects.get(pk=self.booking1.pk)
        serializer = BookingSerializer(booking)
        self.assertEqual(response.data, serializer.data)