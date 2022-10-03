from django.shortcuts import render


def index(request):
    return render(request, 'Tour/index.html')


# Create your views here.
def booking(request):
    return render(request, 'Tour/bookings.html')


def booking_add(request):
    return render(request, 'Tour/booking-add.html')


def booking_edit(request):
    return render(request, 'Tour/booking-edit.html')


def customer(request):
    return render(request, 'Tour/customers.html')
