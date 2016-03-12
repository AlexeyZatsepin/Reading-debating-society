from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget = forms.Textarea(attrs = {'class': 'form-control','rows':6}))

