from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reserva
from .forms import ReservaForm

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reservas/reserva_list.html'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'reservas/reserva_detail.html'

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/reserva_confirm_delete.html'
    success_url = '/reservas/'
