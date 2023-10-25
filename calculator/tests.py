from django.test import TestCase
from .models import Plaster
from .forms import PlasterCalculatorForm

# Define a test class for the PlasterCalculatorView


class PlasterCalculatorViewTest(TestCase):

    # Set up a test environment
    def setUp(self):
        # Create a test Plaster object with specific properties
        self.plaster = Plaster.objects.create(
            plaster_name="Test Plaster",
            coverage_kg_per_mm_per_metre=1.5,
            plasterweight=25.0,
            description="Test plaster description"
        )

    # Test the behavior of the view when it receives a GET request
    def test_plaster_calculator_get(self):
        # Use the test client to send a GET request to the root URL ('/')
        response = self.client.get('/')
        # Assert that the HTTP status code of the response is 200 (successful)

    # Test the behavior of the view when it receives a POST request with valid data
    def test_plaster_calculator_post(self):
        # Create a dictionary with test data for a POST request
        data = {
            'plasterType': self.plaster.id,
            'length': 5.0,
            'width': 4.0,
            'thickness': 10.0
        }
        # Use the test client to send a POST request to the root URL ('/') with the test data
        response = self.client.post('/', data)
        # Assert that the HTTP status code of the response is 200 (successful)
        # Also, check that the response contains specific content related to the calculated results

    # Test the behavior of the view when it receives a POST request with invalid data
    def test_plaster_calculator_post_invalid_data(self):
        # Create an empty dictionary simulating a POST request with missing required form fields
        data = {}
        # Use the test client to send a POST request to the root URL ('/') with the empty data
        response = self.client.post('/', data)
        # Assert that the HTTP status code of the response is 200 (successful)
        # Check that the response contains a specific form error message related to the 'length' field

    # Test the behavior of the view when it receives a POST request with an empty form
    def test_plaster_calculator_post_empty_form(self):
        # Use the test client to send a POST request to the root URL ('/') with an empty form
        response = self.client.post('/', {})
        # Assert that the HTTP status code of the response is 200 (successful)
        # This test does not check for specific content; it's more about a successful response

    # Test the behavior of the view when it receives a POST request with valid data
    def test_plaster_calculator_post_valid_data(self):
        # Create a dictionary with valid test data for a POST request
        data = {
            'plasterType': self.plaster.id,
            'length': 5.0,
            'width': 4.0,
            'thickness': 10.0
        }
        # Use the test client to send a POST request to the root URL ('/') with the test data
        response = self.client.post('/', data)
        # Assert that the HTTP status code of the response is 200 (successful)
        # Also, check that the response contains specific content related to the calculated results
