from django.db import models

class Modlist(models.Model):
    mod_id = models.CharField(null=True)
    name = models.CharField(null=True)
    installed_version = models.CharField(null=True)
    modloader = models.CharField(null=True)
    mc_version = models.CharField(null=True)
    last_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    