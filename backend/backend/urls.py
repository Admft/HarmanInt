from django.contrib import admin  # Import the admin module from django.contrib
from django.urls import path, include  # Import the path and include functions from django.urls
from api.views import CreateUserView  # Import the CreateUserView from the api.views module
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Import views for JWT token handling

# Define the URL patterns for the application

urlpatterns = [
    path("admin/", admin.site.urls),  # URL pattern for the admin interface
    path("api/user/register/", CreateUserView.as_view(), name="register"),  # URL pattern for user registration endpoint, mapped to CreateUserView
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),  # URL pattern for obtaining JWT token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),  # URL pattern for refreshing JWT token
    path("api-auth/", include("rest_framework.urls")),  # URL pattern for built-in DRF authentication views
    path("api/", include("api.urls")),
]
