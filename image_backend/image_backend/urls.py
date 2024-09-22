from django.contrib import admin
from django.urls import path, include
from api.views import home  # Import the new home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # API routes
    path('', home),  # Root URL handler
]
