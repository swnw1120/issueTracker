from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from tracker.models import User, Ticket, Chatroom
from login.models import Session
from .forms import TicketForm, UpdateForm, ConvoForm

# Display all tickets in the database on the homepage
def showTicketData(request):
    tickets = Ticket.objects.all()
    return render(request, 'homepage.html', {'tickets': tickets})

# With GET request, generate a form for adding a ticket
# With POST request, add the ticket onto the database
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

            user_key = request.COOKIES.get("session_key")
            user = Session.objects.get(SessionKey = user_key)

            record.UserID = user.UserID
            record.save()
            # Return to the homepage after inserting
            return redirect('tracker:homepage')

# With GET request, allow the user to select tickets to delete
# With POST request, remove the selected tickets from the database
def deleteTicket(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        return render(request, 'deleteTicketpage.html', {'tickets': tickets})
    elif request.method == 'POST':
        recordsToDelete = request.POST.getlist("selected_options")
        for record in recordsToDelete:
            r = Ticket.objects.filter(TicketID=record)
            r.delete()
        return redirect('tracker:homepage')

# Generate a form with preset values for the user to edit
def updateTicket(request):
    if request.method == 'POST':
        selected_ticket_id = request.POST.get('ticketID')
        selected_ticket = Ticket.objects.get(TicketID=selected_ticket_id)
        updateform = UpdateForm(instance=selected_ticket)
        return render(request, 'updateTicketpage.html', {'updateForm': updateform, 'ticketID': selected_ticket_id, 'ticketName': selected_ticket.TicketName})
    return None

# Check if the edited data is valid and make the changes on the database
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
            return redirect('tracker:homepage')
        else:
            print("Error:")
            print(form.errors)
    return None

# Display ticket data in an organised format
def viewTicket(request, ticketID):
    selected_ticket = Ticket.objects.get(TicketID=ticketID)
    form = ConvoForm()
    current_convo = Chatroom.objects.filter(TicketID=ticketID)
    return render(request, 'viewTicketDetailpage.html', {'ticket': selected_ticket, 'form': form, 'message': current_convo})

# Adding a message to the database when the form is submitted
def addConvo(request):
    form = ConvoForm(request.POST)
    if form.is_valid():
        ticket_id = request.POST.get('TicketID')
        user_id = request.POST.get('UserID')
        new_message = Chatroom()
        new_message.ChatMessage = form.cleaned_data['ChatMessage']
        new_message.TicketID = Ticket.objects.get(TicketID = ticket_id)
        new_message.UserID = User.objects.get(UserID = user_id)
        new_message.save()
        # Refresh the current page to see the new message
        return redirect('tracker:ticket', ticketID = ticket_id)
    return None