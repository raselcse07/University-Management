from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import USERNAME_REGEX
from django.core.validators import RegexValidator





User=get_user_model()



class LoginForm(forms.Form):

    username    =forms.CharField(
                                label="Username",
                                validators=[
                                RegexValidator(
                                    regex=USERNAME_REGEX,
                                    message='Username must be Alphanumeric and contain any of the following : ". @ + - _ "',
                                    code='invalid username'

                                )
                            ],)

    password  = forms.CharField(label='Password', widget=forms.PasswordInput)


    def clean(self,*args,**kwargs):

        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user_obj=User.objects.filter(username=username).first()

        if not user_obj:
            raise forms.ValidationError("Username doesn't exist")

        else:

            if not user_obj.check_password(password):

                raise forms.ValidationError("Invalid Password")
            return super(LoginForm,self).clean(*args,**kwargs)





class UserCreationForm(forms.ModelForm):
  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email', 'reg_number')

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
  

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'reg_number', 'is_active', 'is_admin')

    def clean_password(self):
        
        return self.initial["password"]