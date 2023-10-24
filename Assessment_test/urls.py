from django.urls import path
from .views import EmissionsListCreate

urlpatterns = [
    path('emissions/', EmissionsListCreate.as_view(), name='emissions-list-create'),
]
