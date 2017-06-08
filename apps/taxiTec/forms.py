from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from .models import UserProfile,Owner,Driver,Car,Ingresos

class FormSetIncome(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(FormSetIncome,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({'class':'form__input'})
	class Meta:
		model=Ingresos
		exclude=['driver',]

class FormIncome(forms.ModelForm):
	
	def __init__(self,*args,**kwargs):
		super(FormIncome,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({'class':'form__input'})
	class Meta:
		model=Ingresos
		fields='__all__'


class FormCarAM(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super(FormCarAM,self).__init__(*args,**kwargs)
		self.fields['driver'].queryset=Driver.objects.all()

		for i in self.fields:
			self.fields[i].widget.attrs.update({'class':'form__input'})

	class Meta:
		model=Car
		fields='__all__'
		labels={
			'driver':'Chofer',
			'model':'Modelo',
			'number':'Numero',
			'plates':'Placas',
		}


class FormCarPR(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super(FormCarPR,self).__init__(*args,**kwargs)
		user=kwargs['initial']['user']

		owner=Owner.objects.get(profile=user.userprofile)
		
		self.fields['driver'].queryset=Driver.objects.filter(owner=owner)

		for i in self.fields:
			self.fields[i].widget.attrs.update({'class':'form__input'})

	class Meta:
		model=Car
		exclude=['owner',]
		labels={
			'driver':'Chofer',
			'model':'Modelo',
			'number':'Numero',
			'plates':'Placas',
		}


class UserUpdateForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UserUpdateForm,self).__init__(*args,**kwargs)
		self.fields['username'].help_text=None
		for i in self.fields:
			self.fields[i].widget.attrs.update({'class':'form__input' })
	class Meta:
		model = User
		fields=('first_name','last_name','username','email')
		labels={
			'username':'Nombre de usuario',
			'first_name':'Nombre',
			'last_name':'Apellidos',
			'email':'Correo electronico',
		}


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



class UpdateDriverForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UpdateDriverForm,self).__init__(*args,**kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})

	class Meta:
		model=Driver
		exclude=['profile']
		labels={
			'blood_type':'Tipo de sangre',
			'phone_number_2':'Numero telefono 2',
		}
		


class DriverForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super(DriverForm, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})
	class Meta:
		model=Driver
		exclude=['profile','owner']
		labels={
			'blood_type':'Tipo de sangre',
			'phone_number_2':'Numero telefono 2',
		}


class DriverFormAM(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(DriverFormAM, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({
				'class':'form__input'
			})
	class Meta:
		model=Driver
		exclude=['profile']
		labels={
			'blood_type':'Tipo de sangre',
			'phone_number_2':'Numero telefono 2',
			'owner':'Propietario',
		}
		

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

class FullDriverFormAM(MultiModelForm):
	form_classes={
		'profile':UserProfileForm,
		'driver':DriverFormAM,
		'user':RegistroUserForm,
	}





#LOGIN
class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','password']

