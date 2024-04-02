from django import forms
from datetime import timezone
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Customer,Feedback,Payment
from django.core.exceptions import ValidationError

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'Pass1'}))
    password2 = forms.CharField(label=' Conform Password', widget=forms.PasswordInput(attrs={'class': 'Pass2'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'Email1'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'User1'})}
class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'login-username'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'login-password'}))

class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'Old-Pass'}))
    new_password1 = forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'New-Pass1'}),help_text=password_validation._password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'New-Pass2'}))

class Password_Reset(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput (attrs={'autocomplete':'email','class':'reset-password-email'}))

class Password_Set(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'Pass1'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'Pass2'}),
    )
class Customer_Profile(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','location','city','state','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'name1'}),
                 'location': forms.TextInput(attrs={'class': 'location1'}),
                 'city': forms.TextInput(attrs={'class': 'city1'}),
                 'state': forms.Select(attrs={'class': 'state1'}),
                 'zipcode': forms.NumberInput(attrs={'class': 'zipcode1'}),
                 }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['message']
        widgets={'message':forms.Textarea(attrs={'class':'feedback-message'})}

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['id','card_number','cvv','expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'})
        }

        def clean_card_number(self):
            card_number = self.cleaned_data['card_number']
            if len(str(card_number)) > 12:
                raise ValidationError('Card number should be maximum 12 digits.')
            return card_number

        def clean_cvv(self):
            cvv = self.cleaned_data['cvv']
            if len(str(cvv)) != 3:
                raise ValidationError('CVV should be 3 digits.')
            return cvv

        def clean_expiry_date(self):
            expiry_date = self.cleaned_data['expiry_date']
            if expiry_date <= timezone.now():
                raise ValidationError('Expiry date should be in the future.')
            return expiry_date