from django.db import models

class VersionType(models.TextChoices):
    
    RELEASE = 'release', 'Release'
    BETA = 'beta', 'Beta'
    ALPHA = 'alpha', 'Alpha'

class TrackedMods(models.Model):

    # Data we store, not fetch at refresh
    project_id = models.CharField(null=True)
    mod_name = models.CharField(null=True)
    installed_version = models.CharField(null=True)
    installed_version_type = models.CharField(null=True, choices=VersionType.choices)
    installed_mc_version = models.CharField(null=True)

    # Data we fetch at refresh
    latest_version = models.CharField(null=True)
    latest_version_type = models.CharField(null=True, choices=VersionType.choices)
    latest_mc_version = models.CharField(null=True)
    last_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.mod_name
    