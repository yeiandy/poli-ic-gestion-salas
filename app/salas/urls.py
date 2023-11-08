from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalaListView.as_view(), name='sala-list'),
    path('<int:pk>/', views.SalaDetailView.as_view(), name='sala-detail'),
    # Más rutas para salas.
]
