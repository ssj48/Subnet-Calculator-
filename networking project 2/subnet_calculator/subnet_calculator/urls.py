# subnet_calculator/urls.py

from django.urls import path
from subnet_app.views import subnet_calculator  # Updated import

urlpatterns = [
    path('', subnet_calculator, name='subnet_calculator'),
]
