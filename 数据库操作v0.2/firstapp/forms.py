from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    content = forms.CharField(
        widget=forms.Textarea(),
        )
