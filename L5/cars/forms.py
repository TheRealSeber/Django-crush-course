from django import forms
from . import models


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(
#         label="First Name",
#         max_length=100,
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#     )
#     last_name = forms.CharField(
#         label="Last Name",
#         max_length=100,
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#     )
#     email = forms.EmailField(
#         label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
#     )
#     review = forms.CharField(
#         label="Please write your review",
#         widget=forms.Textarea(attrs={"class": "form-control"}),
#     )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        # fields = ["first_name", "last_name", "email", "review"]
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "stars": "Stars",
            "review": "Please write your review",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "stars": forms.NumberInput(
                attrs={"class": "form-control"}
            ),  # "type": "number
            "review": forms.Textarea(attrs={"class": "form-control"}),
        }
        error_messages = {
            "stars": {
                "min_value": "Minimum value is 1",
                "max_value": "Maximum value is 5",
            }
        }
