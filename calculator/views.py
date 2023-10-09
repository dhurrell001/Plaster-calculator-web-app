from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PlasterCalculatorForm
from .models import Plaster
from decimal import Decimal


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

    if request.method == 'POST':
        form = PlasterCalculatorForm(request.POST)
        if form.is_valid():
            plasterType = form.cleaned_data['plasterType']
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            # Convert coverage_by_metre to Decimal
            coverage_by_metre = Decimal(str(plasterType.coverage_by_metre))

            # Convert length and width to Decimal
            length_decimal = Decimal(str(length))
            width_decimal = Decimal(str(width))

            # Perform division
            plaster_amount = (length_decimal * width_decimal) / \
                coverage_by_metre
            plaster_description = plasterType.description
    else:
        form = PlasterCalculatorForm()

    context = {
        'form': form,
        'plaster_amount': plaster_amount,
        'plaster_description': plaster_description,
    }

    return render(request, template_name, context)
