from django.urls import path
from . import views

urlpatterns = [
    path("simple/", views.simple_view, name="simple_view"),
    # path('<int:page_num>', views.redirect_num_page, name='redirect_num_page'),
    # path('<str:topic>/', views.news_view, name='topic-page'),
    path(
        "examples/",
        views.example_connected_template_view,
        name="example-connected-template-view",
    ),
    path("add/<int:a>/<int:b>/", views.add_view, name="add_view"),
]
