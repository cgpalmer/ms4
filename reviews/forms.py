from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    review_rating = forms.IntegerField(label='Rating', widget=forms.NumberInput(attrs={'min': 0, 'max': 5}))
