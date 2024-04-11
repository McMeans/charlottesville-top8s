from django.db import models


class Player(models.Model):
    player_name = models.CharField(max_length=40)
    player_handle = models.CharField(max_length=16)
    player_placement = models.IntegerField()
    primary_character = models.ImageField()
    secondary_character = models.ImageField()
    tertiary_character = models.ImageField()
    
    class Meta:
        app_label = 'mysite'
    
    def __str__(self):
        return self.player_name
    

class Event(models.Model):
    event_title = models.CharField(max_length=20)
    event_participants = models.IntegerField()
    event_date = models.CharField()

    class Meta:
        app_label = 'mysite'
    
    def __str__(self):
        return self.event_title

    