from django.urls import path, include
from .views import *

urlpatterns = [
    path('', readme),
    #path('', show_date_table),
]