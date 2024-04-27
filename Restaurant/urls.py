#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('api/menu/', views.MenuItemView.as_view(), name='protected_menu'),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),

    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('book/', views.book, name="book"),
    path('bookings/', views.bookings, name="bookings"),
    path('reservations/', views.reservations, name="reservations"),

    path('api-token-auth/', obtain_auth_token),
]
