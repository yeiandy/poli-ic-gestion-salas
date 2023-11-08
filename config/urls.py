from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí puedes incluir las URLconf de tus aplicaciones
    path('reservas/', include('app.reservas.urls')),
    path('salas/', include('app.salas.urls')),
    path('usuarios/', include('app.usuarios.urls')),
]
