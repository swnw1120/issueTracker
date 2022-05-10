from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from tracker.models import User, Ticket, Chatroom
from .forms import TicketForm, UpdateForm

def index(request):
    return render(request, 'homepage.html')

def showTicketData(request):
    tickets = Ticket.objects.all()
    return render(request, 'homepage.html', {'tickets': tickets})

def addTicket(request):
    # Render the form page
    if request.method == 'GET':
        ticketForm = TicketForm()
        return render(request, 'addTicketpage.html', {'ticketForm': ticketForm})
    # Submit form to the database
    elif request.method == 'POST':
        form = TicketForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # Set up insert query with the data entered in the form
            record = Ticket()
            record.TicketName = form.cleaned_data['TicketName']
            record.Description = form.cleaned_data['Description']
            record.Status = 1

            userInstance = User.objects.get(UserID = 1)
            record.UserID = userInstance
            record.save()
            # Return to the homepage after inserting
            return redirect('homepage')

def deleteTicket(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        return render(request, 'deleteTicketpage.html', {'tickets': tickets})
    elif request.method == 'POST':
        recordsToDelete = request.POST.getlist("selected_options")
        for record in recordsToDelete:
            r = Ticket.objects.filter(TicketID=record)
            r.delete()
        return redirect('homepage')

def updateTicket(request):
    if request.method == 'POST':
        selected_ticket_id = request.POST.get('ticketID')
        selected_ticket = Ticket.objects.get(TicketID=selected_ticket_id)
        updateform = UpdateForm(instance=selected_ticket)
        return render(request, 'updateTicketpage.html', {'updateForm': updateform, 'ticketID': selected_ticket_id})
    return None

def confirmUpdate(request):
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            selected_ticket_id = request.POST.get('TicketID')
            ticket = Ticket.objects.get(TicketID=selected_ticket_id)
            ticket.TicketName = form.cleaned_data['TicketName']
            ticket.Description = form.cleaned_data['Description']
            ticket.Status = form.cleaned_data['Status']
            ticket.save()
            return redirect('homepage')
        else:
            print("Error:")
            print(form.errors)
    return None

def viewTicket(request):
    if request.method == 'POST':
        selected_ticket_id = request.POST.get('ticketID')
        selected_ticket = Ticket.objects.get(TicketID=selected_ticket_id)
        return render(request, 'viewTicketDetailpage.html', {'ticket': selected_ticket})
    return None