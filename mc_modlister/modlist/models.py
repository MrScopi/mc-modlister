from django.db import models

class Modlist(models.Model):
    mod_id = models.CharField()
    installed_version = models.CharField()
    modloader = models.CharField()
    mc_version = models.CharField()
    last_updated = models.DateTimeField()