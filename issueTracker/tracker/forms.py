from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description']

class UpdateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description', 'Status']