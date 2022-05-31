from django.forms import ModelForm
from .models import Chatroom, Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description']

    def __init__(self,*args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
    
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
        
        self.fields['Description'].required = False

class UpdateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['TicketName', 'Description', 'Status']
    
    def __init__(self,*args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        
        self.fields['Description'].required = False

class ConvoForm(ModelForm):
    class Meta:
        model = Chatroom
        fields = ['ChatMessage']

    def __init__(self,*args, **kwargs):
        super(ConvoForm, self).__init__(*args, **kwargs)
    
        self.fields['ChatMessage'].widget.attrs['placeholder'] = "Enter new comment here."