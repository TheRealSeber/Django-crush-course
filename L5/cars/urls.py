from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("review/", views.review_view, name="review"),
    path("thank_you/", views.thank_you_view, name="thank_you"),
]
