from django.db import models
from login.models import User
# Create your models here.

class Ticket(models.Model):
    STATUS_OPTION = (
        ("0", "COMPLETE"),
        ("1", "UNCOMPLETE"),
        ("2", "REQUIRE_REVIEW"),
    )
    TicketID = models.AutoField(primary_key=True)
    TicketName = models.CharField(max_length=100)
    Description = models.TextField(max_length=250)
    Status = models.CharField(max_length=1, choices=STATUS_OPTION)
    IssueDate = models.DateTimeField(auto_now_add=True)
    UserID = models.ForeignKey(
        User,
        on_delete= models.PROTECT
    )

class Chatroom(models.Model):
    ChatroomID = models.AutoField(primary_key=True)
    ChatMessage = models.CharField(max_length=200)
    SentTime = models.DateTimeField(auto_now_add=True)
    UserID = models.ForeignKey(
        User,
        on_delete= models.RESTRICT
    )
    TicketID = models.ForeignKey(
        'Ticket',
        on_delete= models.CASCADE
    )