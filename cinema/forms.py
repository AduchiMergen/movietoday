from cinema.models import MovieInCinema
from django import forms


class MovieInCinemaForm(forms.ModelForm):
    class Meta:
        model = MovieInCinema
        fields = '__all__'
        exclude = ['cinema', 'movie']
