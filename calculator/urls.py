from django.urls import path

# from . import views
from .views import HomePageView, AboutPageView
from calculator.views import plaster_calculator, download_plaster_pdf, serve_pdf, display_plaster_image, display_plaster_pdf

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", plaster_calculator, name="home"),

    path('plaster-image/<int:plaster_id>/',
         display_plaster_image, name='display_plaster_image'),
    path('plaster-pdf/<int:plaster_id>/',
         display_plaster_pdf, name='display_plaster_pdf'),


]
