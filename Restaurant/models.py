from django.db import models

# Create your models here.

class Menu(models.Model):
   Title = models.CharField(max_length=200)
   Price = models.DecimalField(max_digits=6, decimal_places=2)
   Inventory = models.SmallIntegerField()

   def __str__(self):
    return f'{self.Title} : {str(self.Price)}'

   '''def get_item(self):
    return f'{self.Title} : {str(self.Price)}' '''



class Booking(models.Model):
    Name = models.CharField(max_length=200)
    No_of_guests = models.SmallIntegerField(default=1)
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name
