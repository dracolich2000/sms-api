from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, ClientViewSet, ClientUsersViewSet, UserViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'clientusers', ClientUsersViewSet)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
