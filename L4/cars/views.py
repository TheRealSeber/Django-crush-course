from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http.request import HttpRequest
from . import models


# Create your views here.
def list_view(request):
    all_cars = models.Car.objects.all()
    content = {"cars": all_cars}

    return render(request, "cars/list.html", content)


def add_view(request: HttpRequest):
    if request.method == "POST":
        brand = request.POST["brand"]
        year = request.POST["year"]
        new_car = models.Car(brand=brand, year=year)
        new_car.save()
        return redirect(reverse("cars:list"))
    return render(request, "cars/add.html")


def delete_view(request: HttpRequest):
    if request.method == "POST":
        pk = request.POST["pk"]
        try:
            car = models.Car.objects.get(pk=pk)
            car.delete()
        except models.Car.DoesNotExist:
            pass
        return redirect(reverse("cars:list"))
    return render(request, "cars/delete.html")
