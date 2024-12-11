from django.db import models
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError

# Regular expression pattern for email validation
def validate_email(value):
    # Define a pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, value):
        raise ValidationError("Invalid email format.")

# Company model
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    employees = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Client model with custom email validation
class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, validators=[validate_email])  # Custom email validator
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# ClientUsers relational model
class ClientUsers(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.deletedAt = now()
        self.active = False
        self.save()

    def __str__(self):
        return f'{self.client.name} - {self.user.username}'
