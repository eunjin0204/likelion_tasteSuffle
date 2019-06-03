from django.db import models

# Create your models here.
class room(models.Model):
    title=models.CharField(max_length=200)
    team_number=models.IntegerField()
    per_team=models.IntegerField()
    leader_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class user_choice(models.Model):
    user_name=models.CharField(max_length=50)
    user_roomnum=models.IntegerField()
    user_select=models.IntegerField()
