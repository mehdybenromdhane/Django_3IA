from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.core.exceptions import ValidationError


def emailValidator(value):
       
    if not value.endswith('@esprit.tn'):
           raise ValidationError("Email must ends with @esprit.tn")
       
       
       

def cinValidator(value):
    
    if len(value)!=8:
        
        raise ValidationError("Cin must has 8 characters ")

class Participant(AbstractUser):
    category = (
        ('Etudiant','Etudiant'),
        ("Enseignant","Enseignant"),
        ("Chercheur", "Chercheur"),
        ("Doctorant","Doctorant")
    )
    cin = models.CharField(max_length=8 ,primary_key=True , validators=[cinValidator] )
    email = models.EmailField(max_length=50, validators=[emailValidator])    
    username= models.CharField(max_length=50, unique=True)
    USERNAME_FIELD="username"
    participant_categroy= models.CharField(max_length=50, choices=category)
    
    def __str__(self):
        
        return self.username
    class Meta:
        verbose_name="Participant"  