from django import forms
from django.core.exceptions import ValidationError
from .models import RulesSystem


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


class RulesRegisterModelForm(forms.ModelForm):
    class Meta:
        model = RulesSystem
        fields = '__all__'

    def clean_system_name(self):
        if len(self.cleaned_data['system_name']) < 1:
            raise ValidationError('System Name cannot be empty')
        # return self.clean_system_name
        # print(self.cleaned_data['system_name'])
        return self.cleaned_data['system_name']
    
    def clean_edition(self):
        if self.cleaned_data['edition'] < 0:
            raise ValidationError("The system's version cannot be negative")

        return self.cleaned_data['edition']

        