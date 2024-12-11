from django.test import TestCase
from .models import Company, Client
from django.contrib.auth.models import User

# Create your tests here.

class CompanyTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Amazon", industry="E-Commerce", employees=5000)

    def test_create_company(self):
        self.assertEqual(self.company.name, "Amazon")

    def test_employee_range(self):
        companies = Company.objects.filter(employees__gte=500, employees__lte=2000)
        self.assertNotIn(self.company, companies)
