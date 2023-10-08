from django.shortcuts import render
from .models import *




def index (request):
    
    home= Home.objects.latest('update')
    
    about=About.objects.latest('update')
    
    skills =Skills.objects.all()
    
    contact=Contact.objects.latest('update')
    
    
    
    context={
        
        'home':home,
        'about':about,
        'skills':skills,
        'contact':contact,
    }
    
    return render(request, 'index.html',context)




# Create your views here.
