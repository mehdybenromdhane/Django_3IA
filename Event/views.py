from django.shortcuts import render


from  django.http import HttpResponse
# Create your views here.

from Conference.models import Conference

from User.models import Participant
def hello(req):

    return HttpResponse("<h1> Hello 3IA3 </h1>")
    
    

# Create your views here.

def list(request):
    
    conf = Conference.objects.get(id=1)
    
    
    
    p= Participant.objects.get(cin=7884)
    
    conf = p.conf_reserv.get(id=1)
    
  
    print(conf)
        
    return HttpResponse(conf.title)
        
        
        
        