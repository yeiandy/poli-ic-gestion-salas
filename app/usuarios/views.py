from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioListView(ListView):
    model = User
    template_name = 'usuarios/usuario_list.html'

class UsuarioCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'usuarios/usuario_form.html'

class UsuarioDetailView(DetailView):
    model = User
    template_name = 'usuarios/usuario_detail.html'

class UsuarioUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'usuarios/usuario_form.html'
