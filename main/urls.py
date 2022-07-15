from django.urls import path
from main.views import index, qr_maker, register, user_logout, login_user
urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='reg'),
    path('logout/', user_logout, name='logout'),
    path('login/', login_user, name='log'),
    path('qr/', qr_maker, name='qr'),
]