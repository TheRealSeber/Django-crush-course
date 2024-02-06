from django.http.response import HttpResponse


def home_view(request):
    return HttpResponse("Hello, world. You're at the playground home page.")
