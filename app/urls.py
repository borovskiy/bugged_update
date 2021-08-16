from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', get_schema_view()),
    path('api/clients/', include('clients.urls')),
]
