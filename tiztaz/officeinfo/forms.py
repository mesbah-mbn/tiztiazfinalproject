from django import forms
from django.forms.widgets import TextInput, DateInput, PasswordInput, Textarea

class CustomerRegForm(forms.Form): 

    FAMALE = 'F'
    MALE = 'M'

    GENDER_CHOICES = [(FAMALE, 'FAMALE'),(MALE, 'MALE')]

    CHINA = 'C'
    PAKISTAN = 'P'
    IRAN = 'I'
    RUSSIA = 'R'
    INDIA = 'IN'

    COUNTRY_TO_TRAVEL_CHOICES = [
        (CHINA, 'China'),
        (PAKISTAN, 'Pakistan'),
        (RUSSIA, 'Russia'),
        (IRAN, 'Iran'),
        (INDIA, 'India')
        ]

    MEDICAL_VISA = 'M'
    STUDENT_VISA = 'S'
    TOURIST_VISA = 'T'
    BUSINESS_VISA = 'B'

    TYPES_OF_VISA_CHOICES = [
        (MEDICAL_VISA, 'Medical'),
        (STUDENT_VISA, 'Student'),
        (TOURIST_VISA, 'Tourist'),
        (BUSINESS_VISA, 'Business')
    ]

    first_name = forms.CharField(required=True, widget=TextInput())
    last_name = forms.CharField(required=True, widget=TextInput())
    father_name = forms.CharField(required=True, widget=TextInput())
    dob = forms.DateField(required=True, widget=DateInput())
    id_card = forms.CharField(required=True, widget=TextInput())
    passport_number = forms.CharField(required=True, widget=TextInput())
    country_to_travel = forms.ChoiceField(required=True, choices=COUNTRY_TO_TRAVEL_CHOICES)
    visa_type = forms.ChoiceField(required=True, choices=TYPES_OF_VISA_CHOICES)
    price_of_visa = forms.DecimalField()
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    phone = forms.CharField(required=True, widget=TextInput())
    mobile = forms.CharField(required=False, widget=TextInput())
    email = forms.CharField(required=False, widget=TextInput())
    address = forms.CharField(required=False, widget=TextInput())
    district = forms.CharField(required=True, widget=TextInput())
    city = forms.CharField(required=True)
    country = forms.CharField(required=True)
    profile_image = forms.ImageField(required=False)
    passport_image = forms.ImageField(required=False)
    tazkira_image = forms.ImageField(required=False)

class VisaStatusForm(forms.Form):
    custormer_visa_id = forms.CharField(required=True, widget=TextInput())


class Tickets(forms.Form):
    date_of_flights = forms.DateField(required=True, widget=DateInput())
    country_to_flights = forms.CharField(required=True, widget=TextInput())
    city_to_flights = forms.CharField(required=True, widget=TextInput())
    price_of_tickets = forms.DecimalField()
