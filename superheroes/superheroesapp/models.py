from django.db import models

# Create your models here.
class Superhero(models.Model):
    superhero_name = models.CharField(max_length=50)
    alter_ego_name = models.CharField(max_length=50)
    primary_hero_ability = models.CharField(max_length=50)
    secondary_hero_ability = models.CharField(max_length=50)
    superhero_catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.superhero_name