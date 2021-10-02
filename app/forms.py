from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import TractorDetail
from django.forms.fields import MultipleChoiceField
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Enter Again',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username','mobile_number', 'address')
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}) ,
        'mobile_number':forms.NumberInput(attrs={'class':'form-control'}) ,
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'})
         
    }

class MyUserChangeForm(UserChangeForm): 
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username','mobile_number', 'address')
    


IMPLEMENT_CHOICE=(
    ('Harrow', 'Harrow'),
    ('Cultivator', 'Cultivator'),
    ('Rotavator', 'Rotavator'),
    ('Plough', 'Plough'),
    ('Paddy Thrasher','Paddy Thrasher'),
    ('Dumping Trailer','Dumping Trailer'),
    ('4 Wheel Trailer','4 Wheel Trailer')
)


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class TractorForm(forms.ModelForm):
    implements=MultipleChoiceField(label='Implement', choices=IMPLEMENT_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=TractorDetail
        fields=['brand','model_no','hp_category','implements']
        widgets = {
        'brand':forms.Select(attrs={'class':'form-control'}),
        'model_no':forms.TextInput(attrs={'class':'form-control'}),
        'hp_category':forms.NumberInput(attrs={'class':'form-control'})  
    }
        