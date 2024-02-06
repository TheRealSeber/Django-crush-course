from django.shortcuts import render
from . import models
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
def index_view(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_available_instances = models.BookInstance.objects.filter(
        status__exact="a"
    ).count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_available_instances": num_available_instances,
    }

    return render(request, "catalog/index.html", context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = models.Book
    fields = "__all__"


class BookDetailView(DetailView):
    model = models.Book
    context_object_name = "book"


@login_required
def restricted_view(request):
    return render(request, "catalog/restricted_view.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "catalog/signup.html"


class CheckedOutBooksByUserView(LoginRequiredMixin, ListView):
    model = models.BookInstance
    template_name = "catalog/profile.html"
    context_object_name = "checked_out_books"
    paginate_by = 10

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).all()
