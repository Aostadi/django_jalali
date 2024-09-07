from xml.dom import VALIDATION_ERR

from django import forms
from Users.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    def clean_national_code(self):
        national_code = self.cleaned_data['national_code']
        if national_code is not None:
            if len(national_code) != 10:
                raise VALIDATION_ERR
        return national_code
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if full_name.istitle() :
            return full_name
        else:
            raise VALIDATION_ERR