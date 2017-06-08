
#from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,DetailView,View,ListView,DeleteView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import Owner,UserProfile,Driver,Car,Ingresos




# Create your views here.
class detailIncome(ListView):
	template_name='taxiTec/detailIncome.html'
	def get_queryset(self):
		pk=self.kwargs['pk']
		user=User.objects.get(pk=pk)
		userprofile=user.userprofile
		driver=Driver.objects.get(profile=userprofile)
		return Ingresos.objects.filter(driver=driver)
	def get_context_data(self,**kwargs):
		context=super(detailIncome,self).get_context_data(**kwargs)
		context['pk']=self.kwargs['pk']
		return context



class SetIncome(CreateView):
	model=Ingresos
	form_class=FormSetIncome
	template_name='taxiTec/setIncome.html'
	success_url=reverse_lazy('taxitec:homeCH')

	def form_valid(self,form):
		profile=self.request.user.userprofile
		driver=Driver.objects.get(profile=profile)
		income=form.save(commit=False)
		income.driver=driver
		return super(SetIncome,self).form_valid(form)

class getCar(DeleteView):
	template_name='taxiTec/getCar.html'
	model=Car
	def get_object(self,queryset=None):
		try:
			profile=self.request.user.userprofile
			driver=Driver.objects.get(profile=profile)
			car=Car.objects.get(driver=driver)
			return car
		except Car.DoesNotExist:
			return None

###########LISTAS################
class ListPR(ListView):
	template_name='taxiTec/list_PR.html'
	def get_queryset(self):
		return Owner.objects.all()

class ListCH(ListView):
	template_name='taxiTec/list_CH.html'
	def get_queryset(self):
		return Driver.objects.all()

class ListDrivers(ListView):
	template_name='taxiTec/list_CH.html'
	def get_queryset(self):
		owner=Owner.objects.get(profile=self.request.user.userprofile)
		return Driver.objects.filter(owner=owner)

class ListCars(ListView):
	template_name='taxiTec/list_car.html'
	def get_queryset(self):
		return Car.objects.all()

class ListCarPR(ListView):
	template_name='taxiTec/list_carPR.html'
	def get_queryset(self):
		owner=Owner.objects.get(profile=self.request.user.userprofile)
		return Car.objects.filter(owner=owner)
class ListIncome(ListView):
	template_name='taxiTec/ingresos.html'

	def get_queryset(self):
		return Ingresos.objects.all()

###########HOME################
class HomeViewAM(TemplateView):
	template_name='taxiTec/homeAM.html'
class HomeViewPR(TemplateView):
	template_name='taxiTec/homePR.html'
class HomeViewCH(TemplateView):
	template_name='taxiTec/homeCH.html'






###########DELETE################
class DeleteIncome(DeleteView):
	model=Ingresos
	success_url=reverse_lazy('taxitec:PR-IN')
		

class DeleteView(DeleteView):
	model=User
	template_name='taxiTec/delete.html'

	def get_success_url(self):
		if self.request.user.userprofile.user_type=='AM':
			return reverse_lazy('taxitec:homeAM')
		else:
			return reverse_lazy('taxitec:homePR')

class DeleteCar(DeleteView):
	model=Car
	template_name='taxiTec/deleteCar.html'
	
	def get_success_url(self):
		if self.request.user.userprofile.user_type =='AM':
			return reverse_lazy('taxitec:homeAM')
		else:
			return reverse_lazy('taxitec:homePR')



###########EDITAR################
class UpdatePR_AM(View):
	template_name='taxiTec/updatePR_AM.html'
	success_url=reverse_lazy('taxitec:AM-PR')

	def get(self,request,pk):
		instance=UserProfile.objects.get(pk=pk)
		instance2=Owner.objects.get(profile=instance)
		instance3=instance.user

		form=UserProfileForm(instance=instance)
		form2=OwnerForm(instance=instance2)
		form3=UserUpdateForm(instance=instance3)
		return render(request,self.template_name,{'form':form,'form2':form2,'form3':form3})


	def post(self,request,*args,**kwargs):
		instance=UserProfile.objects.get(pk=kwargs['pk'])
		instance2=Owner.objects.get(profile=instance)
		instance3=instance.user

		form=UserProfileForm(request.POST or None,instance=instance)
		form2=OwnerForm(request.POST or None,instance=instance2)
		form3=UserUpdateForm(request.POST or None,instance=instance3)

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			form.save()
			form2.save()
			form3.save()
			return redirect('taxitec:AM-PR')


class UpdateCH_PR(View):
	template_name='taxiTec/updateCH_PR.html'
	success_url=reverse_lazy('taxitec:PR-CH')
	def get(self,request,pk):
		
		instance=UserProfile.objects.get(pk=pk)
		instance2=Driver.objects.get(profile=instance)
		instance3=instance.user
		form=UserProfileForm(instance=instance)
		form3=UserUpdateForm(instance=instance3)
		
		if request.user.userprofile.user_type == 'AM':
			form2=UpdateDriverForm(request.POST or None,instance=instance2)
		else:
			form2=DriverForm(request.POST or None,instance=instance2)		
		return render(request,self.template_name,{'form':form,'form2':form2,'form3':form3})

	def post(self,request,*args,**kwargs):
		instance=UserProfile.objects.get(pk=kwargs['pk'])
		instance2=Driver.objects.get(profile=instance)
		instance3=instance.user
		form=UserProfileForm(request.POST or None,instance=instance)
		form3=UserUpdateForm(request.POST or None,instance=instance3)
		
		if request.user.userprofile.user_type == 'AM':
			form2=UpdateDriverForm(request.POST or None,instance=instance2)
		else:
			form2=DriverForm(request.POST or None,instance=instance2)

		print
		if form.is_valid() and form2.is_valid() and form3.is_valid():
			form.save()
			form2.save()
			form3.save()
			if request.user.userprofile.user_type == 'AM':
				return redirect('taxitec:AM-CH')
			else:
				return redirect('taxitec:PR-CH')


class UpdateCar(UpdateView):
	model=Car
	template_name='taxiTec/updateCar.html'
	form_class=FormCarPR
	success_url=reverse_lazy('taxitec:PR-VH')
	def get_initial(self):
		super(UpdateCar,self).get_initial()
		user=self.request.user
		self.initial={'user':user}

		return self.initial

###########LOGIN################
class LoginView(View):
	template_name='taxiTec/index.html'
	form_class=UserForm
	#success_url='taxiTec/home.html'
	def get(self, request):
		form=self.form_class(None)
		return render(self.request,self.template_name,{'form':form})
	def post(self,request):
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(username=username,password=password)
		
		if user is not None:
			login(request,user)
			type_user=user.userprofile.user_type 
			print("QUE PEDOOOOO::::::"+type_user)
			return redirect('taxitec:home'+type_user)

		else:
			form=self.form_class(None)
			error='Escriba correctamente el usuario y la contraseña.'
			return render(self.request,self.template_name,{'form':form,'error':error})




###########LOGOUT################
def logout_view(request):
	logout(request)
	return redirect('taxitec:login')



###########REGISTRAR################
class AddIncome(CreateView):
	model=Ingresos
	template_name='taxiTec/addIncome.html'
	success_url=reverse_lazy('taxitec:PR-IN')
	form_class=FormIncome

class AddCarAM(CreateView):
	template_name='taxiTec/addCar.html'
	success_url=reverse_lazy('taxitec:AM-VH')
	model=Car
	form_class=FormCarAM

class AddCarPR(CreateView):
	template_name='taxiTec/addCar.html'
	success_url=reverse_lazy('taxitec:PR-VH')
	model=Car
	form_class=FormCarPR

	def get_initial(self):
		super(AddCarPR,self).get_initial()
		user=self.request.user
		self.initial={'user':user}
		return self.initial

	def form_valid(self,form):
		profile=self.request.user.userprofile
		owner=Owner.objects.get(profile=profile)
		car=form.save(commit=False)
		car.owner=owner
		return super(AddCarPR,self).form_valid(form)


class SignUpOwner(CreateView):
	form_class=UserProfileForm2
	success_url=reverse_lazy('taxitec:homeAM')

	template_name='taxiTec/registrar2.html'
	

	def form_valid(self,form):
		user=form['user'].save()
		profile=form['profile'].save(commit=False)
		profile.user_type='PR'
		profile.user=user
		profile.save()
		owner=form['owner'].save(commit=False)
		owner.profile=profile
		owner.save()
		return redirect(self.success_url)


class SignUpDriverAM(CreateView):
	form_class=FullDriverFormAM
	success_url=reverse_lazy('taxitec:homeAM')
	template_name='taxiTec/registrar.html'

	def form_valid(self,form):
		user=form['user'].save()
		profile=form['profile'].save(commit=False)
		profile.user_type='CH'
		profile.user=user
		profile.save()
		driver=form['driver'].save(commit=False)
		driver.profile=profile
		driver.save()
		return redirect('taxitec:homeAM')		


class SignUpDriver(CreateView):
	form_class=FullDriverForm
	success_url=reverse_lazy('taxitec:homePR')
	template_name='taxiTec/registrar.html'
	

	def form_valid(self,form):
		user_profile=self.request.user.userprofile
		user=form['user'].save()
		profile=form['profile'].save(commit=False)
		profile.user_type='CH'
		profile.user=user
		profile.save()
		driver=form['driver'].save(commit=False)
		driver.profile=profile
		driver.owner=Owner.objects.get(profile=user_profile)
		driver.save()
		if user_profile.user_type =='PR':
			return redirect(self.success_url)
		else:
			return redirect(reverse_lazy('taxitec:homeAM'))


'''
class SingUpView(CreateView):
	#User
	model=User
	form_class=RegistroUserForm
	second_form_class=UserProfileForm

	template_name='taxiTec/registrar.html'
	success_url=reverse_lazy('taxitec:homeAM')
	
	def get_context_data(self,**kwargs):
		context=super(SingUpView,self).get_context_data(**kwargs)

		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)

		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)

		return context

	def post (self,request,*args,**kwargs):
		self.object=self.get_object

		form=self.form_class(request.POST)
		form2=self.second_form_class(request.POST,request.FILES)

		if form.is_valid() and form2.is_valid():
			profile=form2.save(commit=False)
			profile.user=form.save()
			profile.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form,form2=form2))


'''












