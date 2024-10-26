from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator,FileExtensionValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


from User.models import Participant
from categorie.models import Category
def startDateValidator(value):
    if value< timezone.now().date():
        
        raise ValidationError("start_date must be in future")

class Conference(models.Model):
    
    title= models.CharField(max_length=50)
    description=models.TextField()
    program = models.FileField(upload_to="files/" , validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'] , message="only pdf and jpg files allowed")])
    capacity= models.IntegerField(validators=[MaxValueValidator(limit_value=1000 ,message="Capacity cannot exceed 1000" )])
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    
    start_date=models.DateField(validators=[startDateValidator])
    end_date=models.DateField()
    
    location =models.CharField(max_length=50)
    price=models.FloatField()
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    reservation= models.ManyToManyField(Participant,through="Reservation", related_name="confReserv")
    
    class Meta:
        constraints = [
            
            models.CheckConstraint(
                check=models.Q(start_date__gt=timezone.now().date()),
                name="The conference start date must be greater than today"
            )
        ]
        
    def __str__(self):
        
        return self.title
    
    
    def clean(self):
        
        if self.start_date >= self.end_date:
            
            raise ValidationError("End date must be greater than start date")
    
    
    
     
    
class Reservation(models.Model):
    conference = models.ForeignKey(Conference , on_delete=models.CASCADE , related_name="reservations" )
    participant = models.ForeignKey(Participant , on_delete=models.CASCADE )
    confirmed = models.BooleanField(default=False)
    reservation_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f' reservation confirmed : {self.confirmed}  '
    
    
    def clean(self):
        
        if (self.conference.start_date < timezone.now().date()):
            
            raise ValidationError("you can only reserve upcoming conference")
        
        reservation_count = Reservation.objects.filter(participant=self.participant,reservation_date =timezone.now().date()).count()

         
        if reservation_count >= 3:
            raise ValidationError("You can only reserve 3 conferences per day")
        
    class Meta:
        unique_together=('conference','participant')