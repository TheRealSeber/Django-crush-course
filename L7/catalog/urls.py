from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("create_book/", views.BookCreate.as_view(), name="create_book"),
    path("book_detail/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("restricted/", views.restricted_view, name="restricted"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.CheckedOutBooksByUserView.as_view(), name="profile"),
]
