from rest_framework import serializers
from .models import User, Company, Client, ClientUsers
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'industry', 'revenue', 'employees']

class ClientSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Client
        fields = ['id', 'name', 'user', 'company', 'email', 'phone']

class ClientUsersSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ClientUsers
        fields = ['id', 'client', 'user', 'createdAt', 'updatedAt', 'deletedAt', 'active']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
