from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):

  def clean_booking_date(self):
    booking_date = self.cleaned_data['booking_date']
    # stylist = self.cleaned_data['stylist']
    # count = Booking.objects.filter(booking_date=booking_date, stylist=stylist).count()
    # if booking_date == menu.booking_date:
    if Booking.objects.filter(booking_date=booking_date):
      raise forms.ValidationError('Your booking date is unavaliable now!!!')
    return booking_date

  class Meta:
    model = Booking
    fields = ['username', 'phone_no', 'booking_date', 'stylist']
