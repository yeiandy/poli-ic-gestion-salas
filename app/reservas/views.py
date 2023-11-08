from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ReservaListView(ListView):
    template_name = 'reservas/reserva_list.html'

class ReservaDetailView(DetailView):
    template_name = 'reservas/reserva_detail.html'

class ReservaCreateView(CreateView):
    template_name = 'reservas/reserva_form.html'

class ReservaUpdateView(UpdateView):
    template_name = 'reservas/reserva_form.html'

class ReservaDeleteView(DeleteView):
    template_name = 'reservas/reserva_confirm_delete.html'
    success_url = '/reservas/'
