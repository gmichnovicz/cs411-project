# make sure this is at the top if it isn't already
from django import forms

# our new form
class QueryForm(forms.Form):
    artist = forms.CharField(required=True)
    location = forms.CharField(required=True)
    
