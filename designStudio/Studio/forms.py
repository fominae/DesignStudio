from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms


def validate_password_len(password):
    if len(password) < 6:
        raise ValidationError('Длина пароля не может быть меньше 6 символов')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               validators=[RegexValidator('[a-zA-Z0-9-]+$',
                                                          message="Разрешены только латиница, цифры или тире")],
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин занят'
                               })
    email = forms.EmailField(label='Адрес электронной почты',
                             error_messages={
                                 'invalid': 'Неправильный формат адреса',
                                 'unique': 'Данный адрес занят'})

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               validators=[validate_password_len],
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
        model = User
        fields = ('username',
                  'email',
                  'password', 'password2', 'rules')
