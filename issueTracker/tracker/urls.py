from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path('', views.showTicketData, name='homepage'),
    path('addTicketpage', views.addTicket, name='addTicketpage'),
    path('deleteTicketpage', views.deleteTicket, name='deleteTicketpage'),
    path('updateTicketpage', views.updateTicket, name='updateTicketpage'),
    path('confirmUpdate', views.confirmUpdate, name='updateConfirmation'),
    path('viewTicketDetail', views.viewTicket, name='viewTicketDetail'),
]