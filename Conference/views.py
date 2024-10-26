from django.shortcuts import render


from django.views.generic import *
from django.http.response import HttpResponse
# Create your views here.

from .models import Conference,Reservation

from categorie.models import Category

from .forms import ConferenceModelForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy


@login_required
def list(request):
     
    conferences = Conference.objects.all().order_by('-capacity')
    
    return render(request ,'conference/list.html' , {"data" :conferences})
    
    
    
    
    
class ListConf(ListView):
    model=Conference
    template_name="conference/list.html"
    context_object_name="data"
    
    
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        
        context['category']= Category.objects.all()
        
        return context
    

    def get_queryset(self):
        queryset = Conference.objects.all()
        
        category_id =self.request.GET.get('category')
        
        if category_id:
            queryset = Conference.objects.filter(category=category_id)
        else:
            queryset = Conference.objects.all()

        
        return queryset




class Details(LoginRequiredMixin,DetailView):
    model=Conference
    
    template_name="conference/details.html"
    
    context_object_name="c"



    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        
        conference = self.get_object()
        
        context['reservations'] = Reservation.objects.filter(conference=conference)
        return context
    




def detailsConf(request,ide):
    
    conference= Conference.objects.get(id=ide)
    
    return render(request,"conference/details.html",{"conf":conference})

    


class AddConference(CreateView):
    
    model=Conference
    template_name="conference/add.html"
    
    form_class=ConferenceModelForm
    success_url = reverse_lazy('list')
    
    
    

class UpdateConference(UpdateView):
    model=Conference
    template_name="conference/add.html"
    form_class=ConferenceModelForm
    success_url=reverse_lazy('list')
    
     
     
     
     
class DeleteConference(DeleteView):
    
    model=Conference
    template_name="conference/delete.html"
    success_url=reverse_lazy('list')

    
    
    
    
  
        
        
        