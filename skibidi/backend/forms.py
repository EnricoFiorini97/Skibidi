from django import forms
from .models import Kind, Anime, Episode
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import FormActions
from django.shortcuts import render


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
        

class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)
