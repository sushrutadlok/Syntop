from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    contact = models.CharField(max_length=70, default="")
    Query = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    date = models.DateField()

    def __str__(self):
        return self.fname
    
class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Contact = models.IntegerField(max_length=70, default="")
    Email = models.CharField(max_length=70, default="")
    Query = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    date = models.DateField()