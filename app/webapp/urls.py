from django.urls import path
from webapp.views.articles import add_view

urlpatterns = [
    path("", add_view),
    path('article/add/', add_view)
]