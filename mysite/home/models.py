from  django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Tarif(models.Model):
    formule = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.formule}"

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.content} {self.date}"
    

class About(models.Model):
    about_Julien = models.TextField()
    about_Chanth = models.TextField()
    about = models.TextField()

    def __str__(self):
        return f"{self.about} {self.about_Julien} {self.about_Chanth}"
    
class adress(models.Model):
    location = models.DecimalField(max_digits=10, decimal_places=10)
    adress = models.CharField(max_length=100)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User
    title = models.CharField(max_length=200)  # Event title
    date = models.DateField()  # Date of the event
    start_time = models.TimeField()  # Start time of the event
    end_time = models.TimeField()  # End time of the event
    description = models.TextField(blank=True, null=True)  # Optional event description

    def has_passed(self):
        # Get the current date and time
        now = timezone.now()

        # Check if the event's date and time have passed
        # if now.date() > self.date:
        #     return True  # The event's date has passed
        # elif now.date() == self.date and now.time() > self.end_time:
        #     return True  # The event's end time has passed today
        # return False
    
        return now.date() > self.date or (now.date() == self.date and now.time() > self.end_time)

    def __str__(self):
        return f"{self.title} ({self.date}) - {self.user.username}"

# Create your models here.
