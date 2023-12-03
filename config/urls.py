from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('app.reservas.urls')),  # Asegúrate de que la ruta coincide con el directorio de la aplicación.
    path('salas/', include('app.salas.urls')),
    path('usuarios/', include('app.usuarios.urls')),
]
