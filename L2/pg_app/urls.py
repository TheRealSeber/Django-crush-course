from . import views
from django.urls import path

app_name = "pg_app"

urlpatterns = [
    path("", views.example_view, name="example"),
    path("variables/", views.variable_view, name="variables"),
]
