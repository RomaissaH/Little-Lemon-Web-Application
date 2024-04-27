from django.test import TestCase
from Restaurant.models import Menu, Booking
import datetime

class MenuItemTest(TestCase):
    #@classmethod
    def test_get_item(self):
        item = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        self.assertEqual(item.Title, 'IceCream')
        self.assertEqual(item.Price, 80)
        self.assertEqual(item.Inventory, 100)



class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)

    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(Title = 'Coffee', Price = 10, Inventory = 50)

        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(item2.Title, 'Coffee')
        self.assertEqual(item2.Price, 10)
        self.assertEqual(item2.Inventory, 50)

    def test_get_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)

        self.assertEqual(item.Title, 'IceCream')
        self.assertEqual(item.Price, 80)
        self.assertEqual(item.Inventory, 100)

    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)

class BookingNameTest(TestCase):
    #@classmethod
    def test_get_booking_name(self):
        person = Booking.objects.create(Name='Alice', No_of_guests=1, BookingDate='2024-04-10')
        self.assertEqual(person.Name, 'Alice')
        self.assertEqual(person.No_of_guests, 1)
        self.assertEqual(person.BookingDate, '2024-04-10')


class BookingTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Booking.objects.create(Name='Alice', No_of_guests=1, BookingDate='2024-04-10')

    def test_create_reservation(self) -> None:
        item2 = Booking.objects.create(Name = 'Bob', No_of_guests=5, BookingDate='2024-04-20')

        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(item2.Name, 'Bob')
        self.assertEqual(item2.No_of_guests, 5)
        self.assertEqual(item2.BookingDate, '2024-04-20')

    def test_get_reservation(self) -> None:
        item = Booking.objects.get(id = self.item1.id)

        self.assertEqual(item.Name, 'Alice')
        self.assertEqual(item.No_of_guests, 1)
        self.assertEqual(item.BookingDate, datetime.date(2024, 4, 10))

    def test_delete_reservation(self) -> None:
        item = Booking.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Booking.objects.count(), 0)