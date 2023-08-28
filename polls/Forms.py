from django import forms
from .models import MyModel

class TestForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["my_boolean_field", "name"]

