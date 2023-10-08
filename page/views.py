from django.shortcuts import render, redirect
from .models import *
from .foms import ContactForms
from django.core.mail import send_mail
from django.conf import settings



def index (request):
    
    home= Home.objects.latest('update')
    
    about=About.objects.latest('update')
    
    skills =Skills.objects.all()
    
    contact=Contact.objects.latest('update')
    contacts=ContactForms()
    
    
    
    context={
        
        'home':home,
        'about':about,
        'skills':skills,
        'contact':contact,
        'contacts':contacts,
    
        
    }
    
    return render(request, 'index.html',context)

def save_contacts(request):
    contact_forms = ContactForms(request.POST)
    
    if contact_forms.is_valid():
        subject= "contact form sumbitted"
        
        body ={
            'name': contact_forms.cleaned_data['name'],
            'email': contact_forms.cleaned_data['email'],
            'message': contact_forms.cleaned_data['message'],
            
        }
        
        message='\n'.join(body.values())
        
        send_mail(subject, message, 'test@gmail.com', ['turannebizade11@gmail.com'], fail_silently=False)
        
    return redirect('index' )





# Create your views here.
