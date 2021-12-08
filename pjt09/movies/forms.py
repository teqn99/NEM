from django import forms
from .models import Movie, Review


# added all
class ReviewForm(forms.ModelForm):
    score = forms.IntegerField(
        label='평점',
        min_value=0,
        max_value=10,
    )
    class Meta:
        model = Review
        fields = ('content', 'score')


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'