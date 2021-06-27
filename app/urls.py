from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('registrar/', views.registrar, name='registrar'),
   
]
