from django.db import models


class Player(models.Model):
    player_name = models.CharField()
    player_handle = models.CharField()
    player_placement = models.IntegerField()
    primary_character = models.ImageField()
    secondary_character = models.ImageField()
    tertiary_character = models.ImageField()
    
    def __str__(self):
        return self.player_name

    