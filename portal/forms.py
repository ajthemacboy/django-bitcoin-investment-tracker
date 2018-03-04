from django import forms
from .models import INVESTMENT


class Investment(forms.ModelForm):
    class Meta:
        model = INVESTMENT
        fields = ('investment_date', 'investment_time', 'investment_price', 'investment_amount')

        widgets = {
            'investment_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'investment_time': forms.TimeInput(
                attrs={'type': 'time'}
            )
        }

        labels = {
            'investment_date': "Investment date",
            'investment_time': "Investment time",
            'investment_price': "Investment price",
            'investment_amount': "Investment amount"
        }
