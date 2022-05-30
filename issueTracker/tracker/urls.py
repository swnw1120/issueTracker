from django.urls import path, re_path

from . import views

app_name = "tracker"
urlpatterns = [
    path('', views.showTicketData, name='homepage'),
    path('addTicketpage', views.addTicket, name='addTicketpage'),
    path('deleteTicketpage', views.deleteTicket, name='deleteTicketpage'),
    path('updateTicketpage', views.updateTicket, name='updateTicketpage'),
    path('confirmUpdate', views.confirmUpdate, name='updateConfirmation'),
    re_path(r'viewticket/(?P<ticketID>[0-9]+)', views.viewTicket, name='ticket'),
    path('addConvo', views.addConvo, name='addConvo'),
]