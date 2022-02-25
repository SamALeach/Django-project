from django import forms
from .models import User

class UserAddForm(forms.ModelForm):
    class Meta: #describes the rest of the model form class
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
    def clean(self):
        cleaned_data = self.cleaned_data #clean data
        return



    
