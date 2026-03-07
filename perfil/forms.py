from usuario.models import Persona
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from perfil.models import Perfil
from django.contrib.auth.password_validation import validate_password,\
    get_default_password_validators
 
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.models import User

class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Contraseña',
        help_text="La contraseña debe cumplir con los requisitos mínimos de seguridad.",
    )
    password2 = forms.CharField(widget=forms.PasswordInput)
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden. Por favor, asegúrate de que ambas contraseñas sean iguales.")
        return cleaned_data
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)  # Aplicar los validadores de contraseña de la configuración
        return password1
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Perfil.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso. Por favor, ingresá otro correo electrónico.")
        return email
    

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Repita la contraseña"
        password_validators_help_texts = get_default_password_validators()
        help_text_list = "<ul>"
        for validator in password_validators_help_texts:
            help_text_list += f"<li>{validator.get_help_text()}</li>"
        help_text_list += "</ul>"
        self.fields['password1'].help_text = f"La contraseña debe cumplir con los siguientes requisitos: {help_text_list}"

class PasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not Perfil.objects.filter(email__iexact=email, usuariois_active=True).exists():
            raise ValidationError("Correo electrónico inexistente. Verifique.")

        return email