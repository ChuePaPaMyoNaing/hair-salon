from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(max_length=2000)
  price = models.CharField(max_length=10)
  hairStylist = models.ForeignKey('Stylist', on_delete=models.SET_NULL, null=True)
  photo = models.ImageField(upload_to='images/')


  class Meta:
    ordering = ["id"]
    
  def get_absolute_url(self):
    return reverse('menu-detail', args=[str(self.id)])

  def __str__(self):
    return self.name


class Stylist(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  message = models.TextField(max_length=100)
  desgination = models.CharField(max_length=50)
    
  class Meta:
    ordering = ["name"]
    
  def get_absolute_url(self):
    return reverse('stylist-detail', args=[str(self.id)])

  def __str__(self):
    return self.name


class Booking(models.Model):
  menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
  username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  stylist = models.ForeignKey(Stylist, on_delete=models.SET_NULL, null=True)
  phone_no = models.CharField(max_length=20)
  booking_date = models.DateTimeField(default=date.today)
    
  class Meta:
    ordering = ["menu"]

  def __str__(self):
    return self.username
