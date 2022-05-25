from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from snacks.models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    '''
    Lists Snacks
    '''
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    '''
    Gives a Detailed view of individual Snack Objects
    '''
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    '''
    Allows user to create Snack Object
    '''
    template_name = 'snack_create.html'
    model = Snack
    fields = ["name", "purchaser", "description"]

class SnackUpdateView(UpdateView):
    '''
    Allows user to update an existing Snack Object
    '''
    template_name = 'snack_update.html'
    model = Snack
    fields = ["name", "purchaser", "description"]

class SnackDeleteView(DeleteView):
    '''
    Allows user to Delete an existing Snack object
    '''
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy('snacks')
