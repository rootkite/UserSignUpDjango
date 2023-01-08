from django import forms
from main.models import SiteUser

# class NewUserForm(forms.ModelForm):
#     # if i need custom validation i will be here
#     class Meta():
#         model = User
#         fields = '__all__'


class SiteUserForm(forms.ModelForm):
    class Meta():
        model = SiteUser
        fields = '__all__'

        