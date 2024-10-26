from django.db import models

# Create your models here.

#company models
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'),
                                                   ('Non IT','Non IT'),
                                                   ('Mobile Phones','Mobile Phones'),
                                                   ))  
    added=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
         return self.name+" -- "+self.location


# Employee model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,db_index=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()  
    position=models.CharField(max_length=100,choices=(
        ('Manager','Manager'),
        ('Software Developer','Software Developer'),
        ('Software Tester','Software Tester'),
        ('Project Leader','Project Leader'),
    ))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)  
    def __str__(self):
         return self.name+" -- "+self.company.name