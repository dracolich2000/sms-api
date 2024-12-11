from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Client, ClientUsers
from .serializers import CompanySerializer, ClientSerializer, ClientUsersSerializer
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .permissions import IsAdmin
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter

# View for Company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# View for Client
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdmin]

    @action(detail=False, methods=['post'])
    def create_client(self, request):
        # Check for the company being unique for the client
        company = request.data.get('company')
        if Client.objects.filter(company=company).exists():
            return Response({"error": "Company already taken"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request)

    @action(detail=False, methods=['put'])
    def update_client(self, request):
        client = Client.objects.get(id=request.data.get('id'))
        for field, value in request.data.items():
            setattr(client, field, value)
        client.save()
        return Response(ClientSerializer(client).data)

# View for ClientUsers
class ClientUsersViewSet(viewsets.ModelViewSet):
    queryset = ClientUsers.objects.all()
    serializer_class = ClientUsersSerializer

    @action(detail=False, methods=['get'])
    def search_by_user(self, request):
        user_id = request.query_params.get('user_id')
        clients = ClientUsers.objects.filter(user_id=user_id)
        return Response(ClientUsersSerializer(clients, many=True).data)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Retrieves all users
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)  # Add the SearchFilter backend
    search_fields = ['username']
