from django.db import models

VERSION_TYPE = [    
    ('release', 'Release'),
    ('beta', 'Beta'),
    ('alpha', 'Alpha'),
]

MC_VERSIONS = [
    ('1.21.5', '1.21.5'),
    ('1.21.6', '1.21.6'),
    ('1.21.7', '1.21.7'),
]  

class TrackedMods(models.Model):

    # Data we store, not fetch at refresh
    project_id = models.CharField(null=True, max_length=8)
    mod_name = models.CharField(null=True)
    installed_version = models.CharField(null=True)
    installed_version_type = models.CharField(null=True, choices=VERSION_TYPE)
    installed_mc_version = models.CharField(null=True, choices=MC_VERSIONS)

    # Data we fetch at refresh
    latest_version = models.CharField(null=True)
    latest_version_type = models.CharField(null=True, choices=VERSION_TYPE)
    latest_mc_version = models.CharField(null=True, choices=MC_VERSIONS)
    last_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.mod_name
    