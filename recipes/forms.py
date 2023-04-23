from .models import Comment
from djanngo import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
