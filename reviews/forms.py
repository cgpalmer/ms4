from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'product',)

    review_rating = forms.IntegerField(label='Rating / 5', widget=forms.NumberInput(attrs={'min': 0, 'max': 5,
                                                                                    'class': 'text-center'}))
