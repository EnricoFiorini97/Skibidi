from django import forms
from .models import Kind, Anime, Episode
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions
from django.shortcuts import render


class EpisodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EpisodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    '''
    def clean_appelation(self):
        data = self.cleaned_data['appelation']
        if data.isdigit():
             # assume it's an id, and validate as such
             if not Appelation.objects.filter(pk=data):
                 raise forms.ValidationError('Invalid Appelation id')
        else:
             # assume it's a name
             if ...:
                 raise forms.ValidationError('Invalid Appelation name')
        return data'''

    class Meta:
        model = Episode
        fields = ['name', 'seen', 'e_anime', 'path']

class AnimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.form_class='submit'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Anime
        fields = ['name', 'plot', 'season', 'last_episode', 'start_number_episode', 'global_rating', 'path', 'last_update', 'autodownlodable', 'finished', 'img_source']

class KindForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KindForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.form_class='submit'
        self.helper.add_input(Submit('submit', 'Submit'))
        
    class Meta:
        model = Kind
        fields = ['kind_name']
        
