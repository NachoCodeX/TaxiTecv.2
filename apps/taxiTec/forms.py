from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from .models import UserProfile,Owner,Driver



class RegistroUserForm(UserCreationForm):

	def __init__(self,*args,**kwargs):
		super(RegistroUserForm,self).__init__(*args,**kwargs)
		self.fields['username'].help_text=None
		self.fields['password1'].label='Contraseña'
		self.fields['password2'].label='Cofirma tu contraseña'
		self.fields['password2'].help_text=None
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})

	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		]

		labels={
			'username': 'Nombre de usuario',
			'first_name':'Nombre',
			'last_name':'Apellidos',
			'email':'Correo Electronico',
		}




class UserProfileForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})

	class Meta:
		model=UserProfile
		fields=['age','phone_number','image']
		labels={
			'age':'Edad',
			'phone_number':'Numero de telefono',
			'image':'Foto de perfil',
		}


class OwnerForm(forms.ModelForm):
	class Meta:
		model=Owner
		exclude=['profile',]


class DriverForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super(DriverForm, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})
	class Meta:
		model=Driver
		exclude=['profile',]
		

class UserProfileForm2(MultiModelForm):
	form_classes={
		'profile':UserProfileForm,
		'owner':OwnerForm,
		'user':RegistroUserForm,
	}


class FullDriverForm(MultiModelForm):
	form_classes={
		'profile':UserProfileForm,
		'driver':DriverForm,
		'user':RegistroUserForm,
	}


#LOGIN
class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','password']

