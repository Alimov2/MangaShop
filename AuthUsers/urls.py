from django.urls import path, include
from AuthUsers import views

urlpatterns = [
    path('register/', views.register_user, name='my_register'),
    path('login/', views.login_user, name='my_login'),
    path('logout/', views.logout_user, name='cerrar-sesion')
]
