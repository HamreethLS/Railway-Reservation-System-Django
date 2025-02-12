from django import forms
from .models import *
from django.contrib.auth.models import User
# user reg form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']


# Booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['train', 'passenger_name', 'seat_number']

# User login
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Admin Login
class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Schedule Form
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['train','station','arrival_time', 'departure_time']



class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('name', 'location')

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ('name', 'source', 'destination')
