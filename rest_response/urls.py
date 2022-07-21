from django.urls import path
from .views import show_data , user_data
urlpatterns = [
    path('', show_data),
    path('user-secret-code/<id>', user_data),
    
]
