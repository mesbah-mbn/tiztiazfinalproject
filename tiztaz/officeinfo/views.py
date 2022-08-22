from django.shortcuts import render
from officeinfo.forms import CustomerRegForm, VisaStatusForm, Tickets
from officeinfo.models import CustomerRegistertion, VisasOutcome, Tickets

# Create your views here.

def index(request):
    
    form = CustomerRegForm
    if request.method != 'POST':
        return render( request, 'officeinfo/index.html', context={'form': form})
    
    else:
        form = CustomerRegForm(request.POST)
        created = False

        if form.is_valid():
            data = form.cleaned_data
            print(data)

            customer_defaults = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'father_name': data['father_name'],
                'dob': data['dob'],
                'gender':data['gender'],
                'id_card': data['id_card'],
                'passport_number':data['passport_number'],
                'country_to_travel':data['country_to_travel'],
                'visa_type':data['visa_type'],
                'price_of_visa': data['price_of_visa'],
                'phone':data['phone'],
                'mobile':data['mobile'],
                'email':data['email'],
                'address':data['address'],
                'district':data['district'],
                'city':data['city'],
                'country':data['country'],
                'profile_image': request.FILES.get('progfile_image'),
                'passport_image':request.FILES.get('passport_image'),
                'tazkira_image':request.FILES.get('tazkira_image')
            }
            
            customer = CustomerRegistertion.objects.create(**customer_defaults)
            customer.save()

            visa_status = VisasOutcome.objects.create(customer=customer)

            created = True

            if created:
                msg = f'Customer Reg Success, Your can follow up your visa status using: {visa_status.uid}'
                return render( request, 'officeinfo/index.html', context={'message': msg, 'failed': False})
            else:
                msg = 'Customer Reg fialed'
                return render( request, 'officeinfo/index.html', context={'message': msg, 'failed': True})


def checkVisaStatus(request):

    form = VisaStatusForm
    if request.method != 'POST':
        return render( request, 'officeinfo/visaStatus.html', context={'form': form})

    else:
        form = VisaStatusForm(request.POST)
        success = False

        if form.is_valid():
            data = form.cleaned_data
            print(data)

            visa_state = VisasOutcome.objects.get(uid=data['custormer_visa_id'])

            success = True

            if success:
                if visa_state.visa_status == 'P':
                    result = 'Pending'
                elif visa_state.visa_status == 'A':
                    result = 'Approve'
                elif visa_state.visa_status == 'F':
                    result = 'Faield'

                msg = f'Your Visa Status is: {result}'
                return render( request, 'officeinfo/visaStatus.html', context={'message': msg, 'failed': False})
            else:
                msg = 'Result not found'
                return render( request, 'officeinfo/visaStatus.html', context={'message': msg, 'failed': True})

def ticket(request):
    form = Tickets
    if request.method != 'POST':
        return render( request, 'officeinfo/ticket.html', context={'form': form})
    
    else:
        form = Tickets(request.POST)
        created = False

        if form.is_valid():
            data = form.cleaned_data
            print(data)

            ticket_defaults = {
                'date_of_flights': data['date_of_flights'],
                'country_to_flights': data['country_to_flights'],
                'city_to_flights': data['city_to_flights'],
                'price_of_tickets': data['price_of_tickets'],
            }
            
            ticket_booking = Tickets.objects.create(**ticket_defaults)
            ticket_booking.save()
            created = True

            if created:
                msg = 'Tickct is booked successfully'
                return render( request, 'officeinfo/ticket.html', context={'message': msg, 'failed': False})
            else:
                msg = 'Booking is fialed'
                return render( request, 'officeinfo/ticket.html', context={'message': msg, 'failed': True})

def contact(request):
    return render(request, 'officeinfo/contact.html')