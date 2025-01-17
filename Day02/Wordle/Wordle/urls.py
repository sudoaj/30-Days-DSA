from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                 # Admin site
    path('', include('frontend.urls')),              # Include app-level URLs for the 'frontend' app
]