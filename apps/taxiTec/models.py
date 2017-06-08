from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	type_choices=(
		('AM','ADMINISTRADOR'),
		('PR','PROPIETARIO'),
		('CH','CHOFER'),
	)
	age=models.PositiveIntegerField(default=0,blank=True)
	user_type=models.CharField(max_length=50,choices=type_choices,default='CH',blank=True)
	image = models.ImageField(upload_to='profile-images/',default='/profile-images/empty.jpg',blank=True)
	phone_number = models.CharField(max_length=10,default="XXXXXXXXXX", blank=True)
	
	def getImage(self):
		return self.user.userprofile.image.url

	def __str__(self):
		return (self.user.username)

	def delete(self,*args,**kwargs):
		pass


class Owner(models.Model):
	profile=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
	def __str__(self):
		return self.profile.user.first_name
	def getLastName(self):
		return self.profile.user.last_name
	def getAge(self):
		return self.profile.age
	def getImage(self):
		return self.profile.user.userprofile.image.url
	def getNumber(self):
		return self.profile.phone_number
	def getUserPK(self):
		return self.profile.user.pk
	def getUserProfilePK(self):
		return self.profile.pk


class Driver(models.Model):
	blood_choices=(
		('O+','Tipo O+'),('O-','Tipo O-'),('A+','Tipo A+'),
		('A-','Tipo A-'),('B+','Tipo B+'),('B-','Tipo B-'),
		('AB+','Tipo AB+'),('AB-','Tipo AB-'),
	)

	profile=models.OneToOneField(UserProfile)
	
	owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
	phone_number_2=models.CharField(max_length=10,default="XXXXXXXXXX",blank=True)
	blood_type=models.CharField(max_length=4,choices=blood_choices,default='O-',blank=True)

	def __str__(self):
		return self.profile.user.first_name
	def getLastName(self):
		return self.profile.user.last_name
	def getAge(self):
		return self.profile.age
	def getImage(self):
		return self.profile.user.userprofile.image.url
	def getNumber(self):
		return self.profile.phone_number
	def getNumber2(self):
		return self.phone_number_2
	def getBloodType(self):
		return self.blood_type
	def getUserPK(self):
		return self.profile.user.pk
	def getUserProfilePK(self):
		return self.profile.pk

class Car(models.Model):
	driver=models.ForeignKey(Driver, on_delete=models.CASCADE)
	owner=models.ForeignKey(Owner,blank=True,null=True,on_delete=models.CASCADE)
	model = models.CharField(max_length=50)
	number=models.PositiveIntegerField(default=0)
	plates=models.CharField(max_length=7, default='XXX-XXX')
	km=models.PositiveIntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.model)
		
class Ingresos(models.Model):
	date = models.DateField(auto_now_add=False, auto_now=False)
	ingreso=models.FloatField(default=0)
	driver=models.ForeignKey(Driver,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{}'.format(self.date)