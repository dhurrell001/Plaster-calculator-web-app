from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import HttpResponse
import logging
from django.views.generic import TemplateView
from .forms import PlasterCalculatorForm, PlasterResultForm
from .models import Plaster
from decimal import Decimal
import math
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import Http404, FileResponse, HttpResponse
import os


def bagsNeeded(kg, bagWeight):
    return math.ceil(kg / bagWeight)


def CalculateArea(length, width):
    return length * width


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def plaster_calculator(request):
    template_name = 'home.html'
    plaster_description = ''
    total_metres = 0
    plasters = None
    selected_plaster = None

    if request.method == 'POST':
        plaster_form = PlasterCalculatorForm(request.POST)
        # Get a queryset of all plasters
        plasters = Plaster.objects.all()

        if plaster_form.is_valid():
            plasterType = plaster_form.cleaned_data['plasterType']
            length = plaster_form.cleaned_data['length']
            width = plaster_form.cleaned_data['width']
            thickness = plaster_form.cleaned_data['thickness']

            coverage_kg_per_mm_per_metre = Decimal(
                str(plasterType.coverage_kg_per_mm_per_metre))
            length_decimal = Decimal(str(length))
            width_decimal = Decimal(str(width))

            total_metres = (length_decimal * width_decimal)
            plaster_amount = (
                total_metres * coverage_kg_per_mm_per_metre) * thickness
            plaster_description = plasterType.description

            # Calculate bags needed
            if plaster_amount and plasterType.plasterweight:
                bags_needed = bagsNeeded(
                    plaster_amount, plasterType.plasterweight)
            selected_plaster = plasterType

            # Create a PlasterResultForm instance and populate it with the results
            result_form = PlasterResultForm({
                'plaster_amount': plaster_amount,
                'plaster_description': plaster_description,
                'bags_needed': bags_needed,
                'total_area': total_metres,




            })

    else:
        plaster_form = PlasterCalculatorForm()
        result_form = PlasterResultForm()

    context = {
        'plaster_form': plaster_form,
        'result_form': result_form,
        'plaster_description': plaster_description,
        'total_area': total_metres,
        'plasters': plasters,  # Include the plasters queryset in the context
        'selected_plaster': selected_plaster,


    }

    return render(request, template_name, context)


logger = logging.getLogger(__name__)


# def download_plaster_pdf(request, plaster_id):
#     plaster = get_object_or_404(Plaster, pk=plaster_id)

#     try:
#         with open(plaster.pdf_file.path, 'rb') as pdf_file:
#             logger.debug("PDF file opened successfully")
#             response = FileResponse(pdf_file)
#             response['Content-Type'] = 'application/pdf'
#             response['Content-Disposition'] = f'attachment; filename="{plaster.plaster_name}.pdf"'
#             logger.debug("PDF file response created")
#             print(response)
#             return response
#     except Exception as e:
#         logger.error(f"Error serving PDF file: {e}")

#     raise Http404("File not found")


def display_plaster_image(request, plaster_id):
    plaster = Plaster.objects.get(pk=plaster_id)
    return render(request, 'pdftest.html', {'plaster': plaster})


def view_pdf(request, plaster_id):
    # Retrieve the Plaster object with the specified 'plaster_id'
    plaster = get_object_or_404(Plaster, pk=plaster_id)

    # Ensure that the plaster has a PDF file associated with it
    if plaster.pdf_file:
        # Create a FileResponse object to serve the PDF file
        response = FileResponse(
            plaster.pdf_file, content_type='application/pdf')

        # Set the Content-Disposition header to 'inline'
        # This tells the browser to display the file in the browser window if possible
        response['Content-Disposition'] = f'inline; filename="{plaster.pdf_file.name}"'

        # Return the 'response' object to serve the PDF file
        return response
    else:
        # If the plaster doesn't have a PDF file, return an HTTP response
        # indicating that the PDF file was not found
        return HttpResponse("PDF not found")
