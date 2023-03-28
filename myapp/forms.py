from django import forms


class VideoCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    url = forms.URLField()
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'}))