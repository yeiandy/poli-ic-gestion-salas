from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Sala
from .forms import SalaForm

class SalaListView(ListView):
    model = Sala
    template_name = 'salas/sala_list.html'

class SalaDetailView(DetailView):
    model = Sala
    template_name = 'salas/sala_detail.html'

class SalaCreateView(CreateView):
    model = Sala
    form_class = SalaForm
    template_name = 'salas/sala_form.html'

class SalaUpdateView(UpdateView):
    model = Sala
    form_class = SalaForm
    template_name = 'salas/sala_form.html'
