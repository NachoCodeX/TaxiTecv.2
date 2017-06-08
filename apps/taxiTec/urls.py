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
	url(r'^AM/registrarCH$',login_required(SignUpDriverAM.as_view()),name='registrarCH'),
	url(r'^editarPR/(?P<pk>\d+)/$',UpdatePR_AM.as_view(),name='updatePR_AM'),
	url(r'^AM/vehiculos$',login_required(ListCars.as_view()),name='AM-VH'),
	url(r'^AM/addCar$',login_required(AddCarAM.as_view()),name='add-carAM'),



	#URLS para el PROPIETARIO-PR-
	url(r'^home/PR$',login_required(HomeViewPR.as_view()),name='homePR'),
	url(r'^editarCH/(?P<pk>\d+)/$',UpdateCH_PR.as_view(),name='updateCH_PR'),
	url(r'^PR/CH$',login_required(ListDrivers.as_view()),name='PR-CH'),
	url(r'^PR/registrarCH$',login_required(SignUpDriver.as_view()),name='registrarCH2'),
	url(r'^PR/vehiculos$',login_required(ListCarPR.as_view()),name='PR-VH'),
	url(r'^PR/addCar$',login_required(AddCarPR.as_view()),name='add-carPR'),
	url(r'^PR/income$',login_required(ListIncome.as_view()),name='PR-IN'),
	url(r'^PR/add/income$',login_required(AddIncome.as_view()),name='addincome'),
	url(r'^eliminarIncome/(?P<pk>\d+)/$',DeleteIncome.as_view(),name='deleteIN'),
	url(r'^editarCar/(?P<pk>\d+)/$',UpdateCar.as_view(),name='updateCar'),
	url(r'^detailIncome/(?P<pk>\d+)$',detailIncome.as_view(),name='in-detail'),



	#########CHOFERES-OW##########
	
	url(r'^home/CH$',login_required(HomeViewCH.as_view()),name='homeCH'),
	url(r'^getCar$',login_required(getCar.as_view()),name='getCar'),
	url(r'^setIncome$',login_required(SetIncome.as_view()),name='setIncome'),

	#########GENERALES##########
	#url(r'^registrar$',SingUpView.as_view(),name='registrar'),
	url(r'^eliminar/(?P<pk>\d+)/$',DeleteView.as_view(),name='delete'),
	url(r'^eliminarCar/(?P<pk>\d+)/$',DeleteCar.as_view(),name='deleteCar'),

	url(r'^logout$',logout_view,name='logout'),
]