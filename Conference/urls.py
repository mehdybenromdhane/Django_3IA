from django.urls import path

from .views import  *
urlpatterns = [

    path('', list , ),
    path('details/<int:ide>', detailsConf , name="details"),

    path('listclass/', ListConf.as_view() , name="list"),
    
    path('detailsclass/<int:pk>', Details.as_view() , name="detailsClass"),
    path('add/', AddConference.as_view() , name="add"),
    path('updateclass/<int:pk>', UpdateConference.as_view() , name="updateClass"),
    path('deleteclass/<int:pk>', DeleteConference.as_view() , name="deleteClass"),

]
