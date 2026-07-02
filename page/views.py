from django.shortcuts import render, redirect
from django.template.defaultfilters import title

from .models import Car
# Create your views here.
def get_car(request):
    car=Car.objects.all()
    context={
        'cars':car
    }
    return render(request,'car/list.html',context)

def detail_car(request,pk):
    car=Car.objects.get(pk=pk)
    context={
        'shoh':car
    }
    return render(request,'car/detail.html',context)

def create_car(request):
    if request.method == "POST":
        Car.objects.create(
            brand=request.POST.get("brand"),
            model_name=request.POST.get("model_name"),
            color=request.POST.get("color"),
            year=request.POST.get("year"),
            price=request.POST.get("price"),
            release_date=request.POST.get("release_date"),
            engine_type="Petrol",
            horsepower=100,
            mileage=0,
            fuel_type="Petrol",
            transmission="Automatic",
            vin_number="VIN123456789012345",
            country="Uzbekistan",
        )
        return redirect("list")

    return render(request, "car/create.html")