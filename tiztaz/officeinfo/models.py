from django.db import models

import uuid


# Create your models here.
class CustomerRegistertion(models.Model):
    FAMALE = 'F'
    MALE = 'M'
    GENDER = [
        (FAMALE, 'FAMALE'),
        (MALE, 'MALE')
    ]

    CHINA = 'C'
    PAKISTAN = 'P'
    IRAN = 'I'
    RUSSIA = 'R'
    INDIA = 'IN'

    COUNTRY_TO_TRAVEL = [
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

    TYPES_OF_VISA = [
        (MEDICAL_VISA, 'Medical'),
        (STUDENT_VISA, 'Student'),
        (TOURIST_VISA, 'Tourist'),
        (BUSINESS_VISA, 'Business')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    id_card = models.CharField(max_length=30, unique=True)
    passport_number = models.CharField(max_length=30, unique=True)
    # country_to_travel = models.CharField(max_length=max(len(v[0]) for v in COUNTRY_TO_TRAVEL),
    # choices=COUNTRY_TO_TRAVEL, default=CHINA)
    country_to_travel = models.CharField(max_length=100, choices=COUNTRY_TO_TRAVEL, default=CHINA)
    price_of_visa = models.DecimalField(max_digits=12, decimal_places=2, default=1500, editable=False)
    visa_type = models.CharField(max_length=1, choices=TYPES_OF_VISA, default=BUSINESS_VISA)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to = 'officeinfo/images/')
    passport_image = models.ImageField(upload_to = 'officeinfo/images/')
    tazkira_image = models.ImageField(upload_to = 'officeinfo/images/')
    def __str__(self) -> str:
        return '{}/{}'.format(self.first_name, self.last_name)
    

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=30)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=16, decimal_places=2)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    image = models.ImageField()
    def __str__(self) -> str:
        return '{}/{}'.format(self.first_name, self.last_name)


class EmployeeOrderHistories(models.Model):
    employees = models.ForeignKey(Employee, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return '{}'.format(self.employees)
    
    
class VisaType(models.Model):
    CHINA = 'C'
    PAKISTAN = 'P'
    IRAN = 'I'
    RUSSIA = 'R'
    INDIA = 'IN'

    COUNTRY_TO_TRAVEL = [
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

    TYPES_OF_VISA = [
        (MEDICAL_VISA, 'Medical'),
        (STUDENT_VISA, 'Student'),
        (TOURIST_VISA, 'Tourist'),
        (BUSINESS_VISA, 'Business')
    ]
    # visa_title = models.CharField(max_length=255)
    country_visa = models.CharField(max_length=100, choices=COUNTRY_TO_TRAVEL, default=CHINA)
    price_of_visa = models.DecimalField(max_digits=12, decimal_places=2, default=1500, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    types_of_visa = models.CharField(max_length=1, choices=TYPES_OF_VISA, default=BUSINESS_VISA)
    def __str__(self) -> str:
        return '{}/{}'.format(self.country_visa, self.price_of_visa)
    
class ApplicationOrderForm(models.Model):
    customer = models.ForeignKey(CustomerRegistertion, on_delete=models.PROTECT)
    visa = models.ForeignKey(VisaType, on_delete=models.PROTECT)
    employee_order_history = models.ForeignKey(EmployeeOrderHistories, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return '{}/{}'.format(self.customer, self.visa, self.employee_order_history)
    

class VisasOutcome(models.Model):
    VISA_STATUS_PENDING = 'P'
    VISA_STATUS_APPROVE = 'A'
    VISA_STATUS_FAILED = 'F'
    VISA_STATUS = [
        (VISA_STATUS_PENDING, 'Pending'),
        (VISA_STATUS_APPROVE, 'Approve'),
        (VISA_STATUS_FAILED, 'Failed')
    ]

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    place_at = models.DateTimeField(auto_now_add=True)
    visa_status = models.CharField(
        max_length=1, choices=VISA_STATUS, default=VISA_STATUS_PENDING
    )
    customer = models.ForeignKey(CustomerRegistertion, on_delete=models.PROTECT)
    # application_order_form = models.ForeignKey(ApplicationOrderForm, on_delete=models.PROTECT)
    # def __str__(self) -> str:
    #     return self.place_at, self.visa_status


class Tickets(models.Model):
    date_of_flights = models.DateTimeField(auto_now=True)
    country_to_flights = models.CharField(max_length=100)
    city_to_flights = models.CharField(max_length=100)
    price_of_tickets = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self) -> str:
        return '{}/{}'.format(self.country_to_flights, self.city_to_flights, self.price_of_tickets, self.date_of_flights)


class Booking(models.Model):
    tickests_booking = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return '{}'.format(self.tickests_booking)

class Payments(models.Model):
    application_order_form = models.ForeignKey(ApplicationOrderForm, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return '{}'.format(self.application_order_form)








