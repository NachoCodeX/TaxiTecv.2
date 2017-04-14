from django.conf.urls import url
from .views import *
#from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
urlpatterns=[
	#url(r'^$',login,{'template_name':'taxiTec/index.html'},name='login'),
	url(r'^$',LoginView.as_view(),name='login'),

	#URLS para el ADMINISTRADOR-AM-
	url(r'^home/AM$',login_required(HomeViewAM.as_view()),name='homeAM'),
	url(r'^AM/PR$',login_required(ListPR.as_view()),name='AM-PR'),
	url(r'^AM/CH$',login_required(ListCH.as_view()),name='AM-CH'),
	url(r'^AM/registrarPR$',login_required(SignUpOwner.as_view()),name='registrarPR'),
	url(r'^AM/registrarOW$',login_required(SignUpDriver.as_view()),name='registrarCH'),
	url(r'^eliminar/(?P<pk>\d+)/$',DeleteView.as_view(),name='delete'),


	#URLS para el PROPIETARIO-PR-
	url(r'^home/PR$',login_required(HomeViewPR.as_view()),name='homePR'),
	
	#########GENERALES##########

	url(r'^home/CH$',login_required(HomeViewCH.as_view()),name='homeCH'),
	#url(r'^registrar$',SingUpView.as_view(),name='registrar'),
	url(r'^logout$',logout_view,name='logout'),
]