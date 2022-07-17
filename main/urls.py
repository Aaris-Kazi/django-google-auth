from django.urls import path
from main.views import data_reveal, index, register, reveal_secret, user_logout, login_user, logingo
urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='reg'),
    path('logout/', user_logout, name='logout'),
    path('login/', login_user, name='log'),
    path('qr/', logingo, name='qr'),
    path('secret_reveal/', reveal_secret, name='secret'),
    path('secret-code/<id>', data_reveal, name='reveal'),
    # path('secret-code/', data_reveal, name='reveal'),
]