from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('listar_hotel/', views.listar_hotel, name='listar_hotel'),
    path('agregar_hotel/', views.agregar_hotel, name='agregar_hotel'),
    path('eliminar_hotel/<id>/', views.eliminar_hotel, name='eliminar_hotel'),
    path('modificar_hotel/<id>/', views.modificar_hotel, name='modificar_hotel'),
    path('mapa_valpo/', views.mapa_valpo, name='mapa_valpo'),
    path('lista_categoria/', views.lista_categoria, name='lista_categoria'),
    path('categoria_hotel/<star>/', views.categoria_hotel, name='categoria_hotel'),
    path('hotel/<id>/', views.pagina_hotel, name='pagina_hotel'),
    path('commit/', views.webpay_plus_commit, name='webpay_commit' ),
]
