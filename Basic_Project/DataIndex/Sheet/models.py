from django.db import models

# Create your models here.
class student(models.Model):
    Name= models.CharField(max_length=30)
    Serial= models.CharField(max_length=8,primary_key=True)
    Birth_Date = models.DateField()
    Email= models.CharField(max_length=30, unique=True)
    Phone= models.CharField(max_length=11, unique=True)
    Address= models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Student Data'

    def __str__(self):
        return f"{self.Name}({self.Serial})"
    