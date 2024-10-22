from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import About, Event, Tarif
from home.forms import ContactForm
from mysite import settings
from django.core.mail import send_mail


def homepage(request):
    return render(request, 'pages/index.html')

def about(request):
    about_info = About.objects.first()  # Assuming you have only one About object
    if about_info:
        about_data = {
            'about': about_info.about,
            'about_Julien': about_info.about_Julien,
            'about_Chanth': about_info.about_Chanth,
        }
    else:
        about_data = {
            'about': '',
            'about_Julien': '',
            'about_Chanth': ''
        }
    return render(request, 'pages/about.html', {'about_data': about_data})

def tarif(request):
    tarifs = Tarif.objects.all()
    tarifs_json = list(tarifs.values('formule','name','description','price'))
    return render(request, 'pages/tarif.html', {'tarifs_json':tarifs_json})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail( 
                subject,
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            # Redirect to a success page or display a success message
            success_message = "Your message has been sent successfully. We will get back to you soon."
    else:
        success_message = ''
        form = ContactForm()
    return render(request, 'pages/contact.html',{'form': form,'success_message': success_message})


@login_required
def user_agenda(request):
    # Get events for the currently logged-in user
    events = Event.objects.filter(user=request.user).order_by('date', 'start_time')
    return render(request, 'pages/agenda.html', {'events': events})