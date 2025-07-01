from django.urls import path, include
from .views import home  # หรือ from .views import *

urlpatterns = [
    path('', home),  # ไม่ต้องมี views.
]