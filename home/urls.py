from django.urls import path
from . import views

urlpatterns = [
    # path("", view, name)
    path("", views.home_view, name="home")
]

