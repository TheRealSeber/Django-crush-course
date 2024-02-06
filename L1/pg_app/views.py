from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import Http404
from django.http.response import HttpResponseRedirect
from django.urls import reverse


def simple_view(request):
    return HttpResponse("Hello, world. very simple view.")


articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def news_view(request, topic):
    try:
        topic = articles[topic]
        return HttpResponse(f"Hello at {topic}")
    except:
        raise Http404("Page Not Found")


def add_view(request, a, b):
    return HttpResponse(f"Sum of {a} and {b} is {a+b}")


def redirect_num_page(request, page_num):
    topics_list = list(articles.keys())
    try:
        webpage = reverse("topic-page", args=[topics_list[page_num]])
        return HttpResponseRedirect(webpage)
    except:
        raise Http404("Page Not Found")


def example_connected_template_view(request):
    return render(request, "pg_app/example.html")
