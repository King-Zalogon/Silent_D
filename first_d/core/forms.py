from django import forms
from django.core.exceptions import ValidationError


class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all':('core/css/blue_background_text_input.css',)}


class CharacterResgister(forms.Form):
    char_name = forms.CharField(max_length=15, label="Character name: ", widget=forms.TextInput(attrs={'class':'red_background'}), required=True)
    
    concept = forms.CharField(max_length=30, label="Concept: ")

    # rules_system = forms.CharField(max_length=10, label="System: ", required=False)

    growth = forms.IntegerField(label="Current level or Exp: ", required=False)
    
    age = forms.IntegerField(label="Age (real o apparent): ", required=False)

    # owner_name = forms.CharField(max_length=15, label="Creator's name: ", widget=BlueBackgroundTextInput, required=False)

    is_player = forms.BooleanField(label="Is a player's character? ", required=False)

    alive = forms.BooleanField(label="Is alive? ", required=False)

    bio = forms.CharField(widget=forms.Textarea, label="Biography: ", required=False)

    portrait = forms.URLField(label = "Portrait's URL: ", required=False)

    def clean_age(self):
        if self.cleaned_data["age"] < 0:
            raise ValidationError("Character can't have a negative age")
        return self.cleaned_data["age"]

    def clean(self):
        if self.cleaned_data['growth'] < 0:
            raise ValidationError("Can't have a negative exp or level")
        return self.cleaned_data

