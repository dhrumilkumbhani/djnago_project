from django.http import HttpResponse  
from django.shortcuts import render  
def helloworld(request):
	return HttpResponse("<h1>hy abhishek good morning</h1>")