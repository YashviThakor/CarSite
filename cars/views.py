from django.shortcuts import render
from .models import Car
from django.shortcuts import get_object_or_404

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})
