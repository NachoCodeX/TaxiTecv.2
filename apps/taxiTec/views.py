
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,DetailView,View,ListView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import Owner,UserProfile,Driver


# Create your views here.
def logout_view(request):
	logout(request)
	return redirect('taxitec:login')

#views AM
class HomeViewAM(TemplateView):
	template_name='taxiTec/homeAM.html'

class ListPR(ListView):
	template_name='taxiTec/list_PR.html'
	def get_queryset(self):
		return Owner.objects.all()

class ListCH(ListView):
	template_name='taxiTec/list_CH.html'
	def get_queryset(self):
		return Driver.objects.all()



###############################
class HomeViewPR(TemplateView):
	template_name='taxiTec/homePR.html'


class HomeViewCH(TemplateView):
	template_name='taxiTec/homeCH.html'




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
			return redirect('taxitec:home'+type_user)

		else:
			form=self.form_class(None)
			return render(self.request,self.template_name,{'form':form})

class DeleteView(DeleteView):
	model=User
	template_name='taxiTec/delete.html'
	success_url=reverse_lazy('taxitec:AM-PR')


#REGISTRAR
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

class SignUpDriver(CreateView):
	form_class=FullDriverForm
	success_url=reverse_lazy('taxitec:homeAM')
	print('QUE PEDO')
	template_name='taxiTec/registrar.html'
	

	def form_valid(self,form):
		user=form['user'].save()
		profile=form['profile'].save(commit=False)
		profile.user_type='OW'
		profile.user=user
		profile.save()
		driver=form['driver'].save(commit=False)
		driver.profile=profile
		driver.save()
		return redirect(self.success_url)


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












