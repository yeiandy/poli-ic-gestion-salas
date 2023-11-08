from django.views.generic import ListView, DetailView, CreateView, UpdateView

class SalaListView(ListView):

    template_name = 'salas/sala_list.html'

class SalaDetailView(DetailView):

    template_name = 'salas/sala_detail.html'

class SalaCreateView(CreateView):
    template_name = 'salas/sala_form.html'

class SalaUpdateView(UpdateView):
    template_name = 'salas/sala_form.html'
