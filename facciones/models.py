from django.db import models

# Create your models here.
class Faction(models.Model):
    faction_name    =   models.CharField(max_length=50)
    image           =   models.ImageField(upload_to ='uploads/faction')

    def __str__(self):
        return self.faction_name

class Castle(models.Model):
    name        =   models.CharField(max_length=50,unique=True)
    image       =   models.ImageField(upload_to ='uploads/castle')
    

    def __str__(self):
        return self.name


class User(models.Model):
    username    =   models.CharField(max_length=50,unique=True)
    password    =   models.CharField(max_length=150)
    fullname    =   models.CharField(max_length=100)
    lastlogin   =   models.DateTimeField(null=True)
    apikey      =   models.CharField(max_length=100,null=True)
    castle      =   models.ForeignKey(Castle,on_delete=models.SET_NULL,null=True)
    faction     =   models.ForeignKey(Faction,on_delete=models.SET_NULL,null=True)
    active      =   models.BooleanField(default=True)

class ScoreHistory(models.Model):
    info        =   models.TextField()
    score       =   models.IntegerField()
    date        =   models.DateTimeField()
    
    user        =   models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    user        =   models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    text        =   models.TextField()    
    date        =   models.DateTimeField()







