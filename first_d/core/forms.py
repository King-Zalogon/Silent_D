from django import forms

class ContactForm(forms.Form):
    f_name= forms.CharField(label="First name: ", required=True)
    l_name= forms.CharField(label="Last name: ", required=True)
    mail= forms.EmailField(label="E-mail: ", required=True)
    message= forms.CharField(widget=forms.Textarea, label="What's up?")

