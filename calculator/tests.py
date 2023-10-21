from django.test import TestCase
from .models import Plaster
from .forms import PlasterCalculatorForm


class PlasterCalculatorViewTest(TestCase):
    def setUp(self):
        self.plaster = Plaster.objects.create(
            plaster_name="Test Plaster",
            coverage_kg_per_mm_per_metre=1.5,
            plasterweight=25.0,
            description="Test plaster description"
        )

    def test_plaster_calculator_get(self):
        # Use the correct URL for the root page
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_plaster_calculator_post(self):
        data = {
            'plasterType': self.plaster.id,
            'length': 5.0,
            'width': 4.0,
            'thickness': 10.0
        }
        # Use the correct URL for the root page
        response = self.client.post('/', data)
        self.assertEqual(response.status_code, 200)

        # Test that the context contains the expected data
        self.assertContains(response, 'Plaster Amount Needed in KG')
        self.assertContains(response, 'Bags Needed')
        self.assertContains(response, 'Total area in square metres')

    def test_plaster_calculator_post_invalid_data(self):
        data = {}  # Missing required form fields
        # Use the correct URL for the root page
        response = self.client.post('/', data)
        self.assertEqual(response.status_code, 200)

        # Test that the response contains form errors
        self.assertFormError(response, 'plaster_form',
                             'length', 'This field is required.')

    def test_plaster_calculator_post_empty_form(self):
        # Use the correct URL for the root page
        response = self.client.post('/', {})
        self.assertEqual(response.status_code, 200)

        # Test that the response contains the default form

    def test_plaster_calculator_post_valid_data(self):
        data = {
            'plasterType': self.plaster.id,
            'length': 5.0,
            'width': 4.0,
            'thickness': 10.0
        }
        # Use the correct URL for the root page
        response = self.client.post('/', data)
        self.assertEqual(response.status_code, 200)

        # Test that the response contains the calculated results
        self.assertContains(response, 'Plaster Amount Needed in KG')
        self.assertContains(response, 'Bags Needed')
        self.assertContains(response, 'Total area in square metres')
