from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    body_text = forms.CharField(
            widget=forms.Textarea(attrs={"rows":2, "cols":30})
    )
    class Meta:
        model = Email
        fields = ('to_email', 'body_text', 'delay')
