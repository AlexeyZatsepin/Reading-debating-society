# coding=utf-8
from django.core.validators import RegexValidator

from .models import Alumni
from django.forms import CharField, ModelForm, Form, URLField, EmailField,ImageField
from django.core import validators


class Registration(Form):
    # class Meta():
    # model = Alumni
    # fields = ['first_name', 'last_name', 'email', 'linkedin', 'time_in_society', 'courses', 'current_occupation',
    #         'current_company']
    # widgets={
    #    'email': CharField(),
    # }
    class Media():
        css = {'all': ('alumni.css',)}
        js = ()

    first_name = CharField(max_length=20, required=True, validators=[validators.RegexValidator(
        regex="^([A-Za-z]+[,.]?[ ]?|[A-Za-z]+['-]?)+$",
        message='Enter valid name'
    )])
    last_name = CharField(max_length=20, required=True, validators=[validators.RegexValidator(
        regex="^([A-Za-z]+[,.]?[ ]?|[A-Za-z]+['-]?)+$",
        message='Enter valid name'
    )])
    email = CharField(validators=[validators.validate_email], required=True)
    facebook = CharField(validators=[validators.RegexValidator(
        regex='(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?',
        message="Enter valid url"
    )], required=False)
    linkedin = CharField(validators=[RegexValidator(
        regex='(ftp|http|https):\/\/?((www|\w\w)\.)?linkedin.com(\w+:{0,1}\w*@)?(\S+)(:([0-9])+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?',
        message="Enter valid url"
    )], required=False)
    time_in_society = CharField(max_length=10, validators=[RegexValidator(
        regex='[2]\d{3}-[2]\d{3}',
        message='Must be in this type 2xxx-2xxx',
        code='invalid_duration'
    ), ], required=False)
    courses = CharField(max_length=100, required=False)
    current_occupation = CharField(max_length=60, required=False)
    image = ImageField(required=False)