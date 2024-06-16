from django.db import models

class Graphic(models.Model):
    image = models.ImageField()
    title = models.TextField(max_length=20)
    user_id = models.TextField(max_length=9)
    models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

"""class Player(models.Model):
    player_name = models.CharField(max_length=40)
    player_handle = models.CharField(max_length=16, null=True)
    player_placement = models.IntegerField()
    primary_character = models.ImageField()
    secondary_character = models.ImageField(null=True)
    tertiary_character = models.ImageField(null=True)
    
    class Meta:
        app_label = 'mysite'
    
    def __str__(self):
        return self.player_name
    

class Event(models.Model):
    event_title = models.CharField(max_length=20)
    event_participants = models.IntegerField()
    event_date = models.CharField(max_length=10)
    side_title = models.CharField(max_length=30, null=True)
    side_winner = models.CharField(max_length=80, null=True)
    redemption_winner = models.CharField(max_length=4, null=True)
    redemption_render = models.ImageField(null=True)

    class Meta:
        app_label = 'mysite'
    
    def __str__(self):
        return self.event_title"""

    