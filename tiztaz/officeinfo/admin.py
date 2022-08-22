from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.CustomerRegistertion)
class CustomerRegistertionAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['first_name', 'last_update']
    list_display = ['first_name', 'last_name', 'passport_number', 'profile_image']
    search_fields = ['first_name', 'last_name', 'passport_number']
    list_per_page = 10

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

@admin.register(models.EmployeeOrderHistories)
class EmployeeOrderHistoriesAdmin(admin.ModelAdmin):
    list_display = ['employees']

@admin.register(models.ApplicationOrderForm)
class ApplicationOrderFormAdmin(admin.ModelAdmin):
    list_display = ['customer', 'visa', 'employee_order_history']

@admin.register(models.VisaType)
class VisaTypeAdmin(admin.ModelAdmin):
    list_display = ['country_visa', 'price_of_visa', 'last_update', 'types_of_visa']

@admin.register(models.VisasOutcome)
class VisasOutcomeAdmin(admin.ModelAdmin):
    list_display = ['place_at','visa_status', 'customer']

@admin.register(models.Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['application_order_form']


@admin.register(models.Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['country_to_flights','city_to_flights']