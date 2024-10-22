from django.contrib import admin
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .models import Tarif,About,Event

class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_Julien','about_Chanth','about')  # Display this fields into the list 
    search_fields = ('about',)  

def check_passed_events(modeladmin, request, queryset):
    # Filter events that have passed
    passed_events = queryset.filter(date__lt=timezone.now().date())
    
    if passed_events.exists():
        # Create a list of passed events
        event_details = "\n".join([f"{event.title} on {event.date}" for event in passed_events])
        
        # Send an email to the admin
        send_mail(
            'Passed Events Check',
            f'The following events have passed:\n\n{event_details}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Send to the admin's email
            fail_silently=False,
        )
        
        # Inform the admin via Django's message framework
        modeladmin.message_user(request, f"Notification sent for {passed_events.count()} passed events.")
    else:
        modeladmin.message_user(request, "No passed events found.")

# Register the action in the admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'start_time', 'end_time', 'has_passed')
    actions = ['check_passed_events']  # Custom action to check passed events

    # Indicate in the list display whether the event has passed
    def has_passed(self, obj):
        return obj.has_passed()  # Use the updated logic from the model
    has_passed.boolean = True  # Show as a green checkmark or red cross
    has_passed.short_description = 'Event Passed'

# Register the Event model with the custom admin
admin.site.register(Event, EventAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Tarif)

# Register your models here.
