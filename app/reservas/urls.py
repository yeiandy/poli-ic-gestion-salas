from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='reserva-list'),
    path('<int:pk>/', views.ReservaDetailView.as_view(), name='reserva-detail'),
    # Aquí puedes agregar más rutas, por ejemplo para crear, actualizar o eliminar reservas.
]
