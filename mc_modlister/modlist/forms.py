from django import forms

from .models import Modlist

class ModlistForm(forms.ModelForm):
    class Meta:
        model = Modlist
        fields = [
            'mod_id',
            'installed_version',
            'mc_version',
        ]