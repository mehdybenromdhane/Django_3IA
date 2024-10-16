from django.urls import path

from .views import hello , list
urlpatterns = [

    path("" , hello),
    path('list/', list)
]
