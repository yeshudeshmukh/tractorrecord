from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    address=models.CharField(max_length=100)
    


TRACTOR_CHOICE=(
    ('Mahindra','Mahindra'),
    ('Sonalika',' Sonalika'),
    ('John Deere','John Deere'),
    ('New Holland','New Holland'),
    ('Kubota','Kubota'),
    ('Massey Ferguson',' Massey Ferguson'),
    ('Powertrac','Powertrac'),
    ('swaraj','swaraj'),
    ('Eicher','Eicher')
)

class TractorDetail(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,default=True)
    brand=models.CharField(choices=TRACTOR_CHOICE,max_length=100)
    model_no=models.CharField(max_length=100,null=True)
    hp_category=models.IntegerField()
    implements=models.CharField(max_length=100)
