from django.urls import path
from . import views
urlpatterns = [
	path('',views.hello1,name="hello1"),
	path('test',views.test,name="test"),
	path('test2',views.test2,name="test2"),
	path('index',views.index,name="index"),
	path('index1',views.index1,name="index1"),
	path('setsession',views.setsession,name="setsession"),
	path('setcookie',views.setcookie,name="setcookie"),
	path('getcookie',views.getcookie,name="getcookie"),
	path('getfile',views.getfile,name="getfile"),
	path('getfilefromdatabase',views.getfilefromdatabase,name="getfilefromdatabase"),
	path('getpdf',views.getpdf,name="getpdf"),
	path('boot',views.boot,name="boot"),
	
]  

