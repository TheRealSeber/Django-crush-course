from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from . import forms
from . import models

# Create your views here.


class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"


class ContactFormView(FormView):
    form_class = forms.ContactForm
    template_name = "classroom/contact.html"

    # success_url = "classroom/thanks"
    success_url = reverse_lazy("classroom:thanks")

    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request.POST)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    #  looks for teacher_form.html
    model = models.Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thanks")


class TeacherListView(ListView):
    # looks for teacher_list.html
    model = models.Teacher
    queryset = models.Teacher.objects.order_by("first_name")
    context_object_name = "teachers"


class TeacherDetailView(DetailView):
    model = models.Teacher


class TeacherUpdateView(UpdateView):
    model = models.Teacher
    fields = ["subject"]
    success_url = reverse_lazy("classroom:teacher_list")


class TeacherDeleteView(DeleteView):
    model = models.Teacher
    success_url = reverse_lazy("classroom:teacher_list")
