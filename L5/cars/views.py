from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from . import forms


# Create your views here.
def review_view(request):
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("cars:thank_you"))
    else:
        form = forms.ReviewForm()
    return render(request, "cars/rental_review.html", {"form": form})


def thank_you_view(request):
    return render(request, "cars/thank_you.html")
