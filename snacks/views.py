from django.views.generic import ListView
from snacks.models import Snack

class SnackListView(ListView):
    '''
    Lists Snacks
    '''
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(ListView):
    '''
    Gives a Detailed view of individual Snack Objects
    '''
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView():
    '''
    Allows user to create Snack Object
    '''
    pass
class SnackUpdateView():
    '''
    Allows user to update an existing Snack Object
    '''
    pass
class SnackDeleteView():
    '''
    Allows user to Delete an existing Snack object
    '''
    pass