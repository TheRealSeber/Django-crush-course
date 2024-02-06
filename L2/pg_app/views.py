from django.shortcuts import render


# Create your views here.
def example_view(request):
    return render(request, "pg_app/example.html")


def variable_view(request):
    var_dict = {
        "first_name": "SEBEK",
        "last_name": "CHLEBEK",
        "some_list": ["a", "b", "c", "d", "e"],
        "inside_dict": {"key1": "value1", "key2": "value2"},
        "user_logged_in": True,
    }
    return render(request, "pg_app/variables.html", context=var_dict)
