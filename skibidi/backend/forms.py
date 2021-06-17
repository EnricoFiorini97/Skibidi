from django import forms
from .models import Kind, Anime, Episode
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class EpisodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EpisodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.form_name = "Inserisci un Episodio"
        self.helper.add_input(Submit('submit', 'Submit', css_class="uk-button uk-button-large uk-button-danger"))
    
    class Meta:
        model = Episode
        fields = ['name', 'seen', 'e_anime', 'path']

class AnimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.form_class='submit'
        self.form_name = "Inserisci un anime"
        self.helper.add_input(Submit('submit', 'Submit', css_class="uk-button uk-button-large uk-button-danger"))

    class Meta:
        model = Anime
        fields = ['name', 'plot', 'season', 'last_episode', 'start_number_episode', 'global_rating', 'path', 'last_update', 'autodownlodable', 'finished', 'img_source']

class KindForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KindForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.form_class='submit'
        self.form_name = "Inserisci un genere"
        self.helper.add_input(Submit('submit', 'Submit', css_class="uk-button uk-button-large uk-button-danger"))
        
    class Meta:
        model = Kind
        fields = ['kind_name']
        

class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class':"uk-width-1-1", 'placeholder':"Username"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':"uk-width-1-1", 'placeholder':"Password"}),
    )
    error_messages = {
        'invalid_login': ("Username o password non corretti"),
        'inactive': ("Account inattivo."),
    }
    

class UserCreateForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("Le password non corrispondono"),
        'username_not_unique': ('Nome utente non disponibile'),
        'email_not_unique': ('Indirizzo email già utilizzato'),
    }
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class':"uk-width-1-1", 'placeholder':"Username"}))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True, 'class':"uk-width-1-1", 'placeholder':"E-mail"}))
    
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':"uk-width-1-1", 'placeholder':"Password"}),
        )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':"uk-width-1-1", 'placeholder':"Conferma password"}),
        strip=False,
        help_text=("Inserisci di nuovo la password"),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            print(email)
            raise ValidationError(self.error_messages['email_not_unique'], code='email_not_unique')
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError(self.error_messages['username_not_unique'], code='username_not_unique')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    
    def _post_clean(self):
        super()._post_clean()
        

