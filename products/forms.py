from django import forms

class BookingForm(forms.Form):
    booking_date = forms.DateField()  # Replace with the actual form field you're using
