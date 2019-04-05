from django import forms


class UrlForm(forms.Form):
    full_url = forms.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_url'].label = ''
        self.fields['full_url'].widget.attrs.update({'placeholder': 'Full URL address'})
