from django import forms
from django.core.exceptions import ValidationError


class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all':('core/css/blue_background_text_input.css',)}


class ContactForm(forms.Form):
    f_name= forms.CharField( label="First name: ", widget=forms.TextInput(attrs={'class':'red_background'}), required=True)

    l_name= forms.CharField(label="Last name: ", widget=BlueBackgroundTextInput, required=True)

    mail= forms.EmailField(label="E-mail: ", required=True)

    pet_count= forms.IntegerField(label="How many pets do you have?")

    message= forms.CharField(widget=forms.Textarea, label="What's up?")

    date= forms.DateField()

    def clean_pet_count(self):
        if self.cleaned_data["pet_count"] < 0:
            raise ValidationError("User can't have a negative number of pets")
        return self.cleaned_data["pet_count"]

    def clean(self):
        if self.cleaned_data['mail'] == 'jp@email.com':
            raise ValidationError('User already registered')
        return self.cleaned_data

