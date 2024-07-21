from django import forms

class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Enter new text for sentiment analysis', required=True)
