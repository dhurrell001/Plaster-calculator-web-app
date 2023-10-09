from django.urls import path

# from . import views
from .views import HomePageView, AboutPageView
from calculator.views import plaster_calculator

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", plaster_calculator, name="home"),

]
