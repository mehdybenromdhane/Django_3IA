from django.shortcuts import render

from django.http.response import HttpResponse
# Create your views here.

from .models import Conference

from .models import Participant
def list(request):
    
    # conf= Conference.objects.get(id=1)
    
    
    
    
    p1 = Participant.objects.get(cin=7884)
    
    
    reservation = p1.confReserv.all()

     
    return HttpResponse(reservation)
    
    
    
    
  
        
        
        