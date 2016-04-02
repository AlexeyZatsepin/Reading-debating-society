from django import forms
from django.core import validators


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))


class SearchForm(forms.Form):
    field = forms.CharField(required=False, max_length=50,
                            widget=forms.TextInput(attrs={'type': 'search', 'placeholder': 'Search',
                                                          'onkeydown': 'if (e)vent.keyCode==13)'
                                                                       '{this.form.submit();return false;}',
                                                          'id': 'main'}),
                            validators=[validators.RegexValidator(
                                regex="^[a-zA-z0-9!?- ]+$",
                                message='No XSS!'
                            )])


class SearchFormMobile(forms.Form):
    field = forms.CharField(required=False, max_length=50,
                            widget=forms.TextInput(attrs={'type': 'search', 'placeholder': 'Search',
                                                          'onkeydown': 'if (e)vent.keyCode==13;'
                                                                       '{this.form.submit();return false;}',
                                                          'id': 'mobile'}),
                            validators=[validators.RegexValidator(
                                regex="^[a-zA-z0-9!?- ]+$",
                                message='No XSS!'
                            )])
