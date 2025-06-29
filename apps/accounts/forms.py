from django.forms import ModelForm
from .models import CustomUser

class CustomUserRegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone')


        
