from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField()
    news = forms.CharField()
    site = forms.CharField()