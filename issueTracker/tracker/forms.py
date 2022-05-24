from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description']

    def __init__(self,*args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
    
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

class UpdateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description', 'Status']