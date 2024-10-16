from django.contrib import admin

from .models import Conference,Reservation
# Register your models here.
from django.db.models import Count
    
from django.utils import timezone

    





class ReservationForm(admin.TabularInline):
    model=Reservation
    
    extra=2
    
    readonly_fields=['confirmed']
    

class PartcipantFilter(admin.SimpleListFilter):
    
    title="Number of participants"
    
    parameter_name="participants"
    
    def lookups(self , request,model_admin):
        
        return (
            
            ('No','No participants'),
            ('Yes','There are participants')
        )
        
    
    
    
    
    def queryset(self,request, queryset):
        if self.value()=='No':
            return queryset.annotate(participant_count = Count('reservation')).filter(participant_count__exact=0)

        if self.value()=='Yes':
                return queryset.annotate(participant_count = Count('reservation')).filter(participant_count__gt=0)








class DateFilter(admin.SimpleListFilter):
    
    title="Date"
    
    parameter_name="date"
    
    def lookups(self , request,model_admin):
        
        return (
            
            ('past','Past Conferences'),
            ('upcoming','Upcoming Conferences'),
            ('today','Today Conferences'),

        )
        
    
    
    
    
    def queryset(self,request, queryset):
        if self.value()=='past':
            return queryset.filter(start_date__lt=timezone.now().date())
        if self.value()=='upcoming':
            return queryset.filter(start_date__gt=timezone.now().date())

        if self.value()=='today':
            return queryset.filter(start_date__exact=timezone.now().date())

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display=('title','start_date','category','description','capacity','location','price',)
    
    search_fields=['title','price',]
    
    list_per_page=2
    
    list_filter=['title','price',PartcipantFilter,DateFilter]
    
    
    autocomplete_fields=['category']

    inlines=[ReservationForm]


    
    
    
   
@admin.register(Reservation) 
class ReservationAdmin(admin.ModelAdmin):
    
    list_display=('reservation_date','confirmed',)
    
    