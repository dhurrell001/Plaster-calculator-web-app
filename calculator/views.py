from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PlasterCalculatorForm
from .models import Plaster
from decimal import Decimal
import math


def bagsNeeded(kg, bagWeight):
    return math.ceil(kg / bagWeight)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def plaster_calculator(request):
    template_name = 'home.html'
    plaster_amount = None
    plaster_description = None
    bags_needed = None

    if request.method == 'POST':
        form = PlasterCalculatorForm(request.POST)
        if form.is_valid():
            plasterType = form.cleaned_data['plasterType']
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            thickness = form.cleaned_data['thickness']
            # Convert coverage_by_metre to Decimal
            coverage_kg_per_mm_per_metre = Decimal(
                str(plasterType.coverage_kg_per_mm_per_metre))

            # Convert length and width to Decimal
            length_decimal = Decimal(str(length))
            width_decimal = Decimal(str(width))

            # Perform division
            total_metres = (length_decimal * width_decimal)
            plaster_amount = (
                total_metres * coverage_kg_per_mm_per_metre) * thickness
            bags_needed = bagsNeeded(plaster_amount, plasterType.plasterweight)
            plaster_description = plasterType.description
    else:
        form = PlasterCalculatorForm()

    context = {
        'form': form,
        'plaster_amount': plaster_amount,
        'plaster_description': plaster_description,
        'bags_needed': bags_needed
    }

    return render(request, template_name, context)
