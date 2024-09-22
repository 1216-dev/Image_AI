from django.urls import path
from .views import generate_image  # Import the view

urlpatterns = [
    path('generate-image/', generate_image, name='generate_image'),
]
