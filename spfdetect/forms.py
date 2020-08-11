from django import forms

from .models import Post

class input(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('providedZip', 'providedLocation')
