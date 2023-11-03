import re
from django import forms
from .models import *


def clean_name(name):
    if not re.match(r'^[а-яА-ЯёЁ\s-]+$', name):
        raise ValidationError('Используйте кириллицу, дефис и пробелы')


def clean_username(username):
    if not re.match(r'^[a-zA-Z\s-]+$', username):
        raise ValidationError('Используйте латиницу и дефис')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               validators=[clean_username],
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин занят'
                               })
    name = forms.CharField(label='ФИО',
                               validators=[clean_name],
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    email = forms.EmailField(label='Адрес электронной почты',
                             error_messages={
                                 'invalid': 'Неправильный формат адреса',
                                 'unique': 'Данный адрес занят'})

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'Обязательное поле',
                                })
    rules = forms.BooleanField(required=True,
                               label='Согласие с правилами регистрации',
                               error_messages={
                                   'required': 'Обязательное поле',
                               })

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('name', 'username',
                  'email',
                  'password', 'password2', 'rules')
