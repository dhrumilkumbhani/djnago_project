from django.shortcuts import render
from django.http import HttpResponse  
from django.views.decorators.http import require_http_methods  #restriction about get and post request
from abhi.form import EmpForm,StudentForm      #form file add karvi empform lava mate
from abhi.functions import handle_uploaded_file           #handle_uploaded_file  file upload mate add karvu
import csv #csv throgh csv file banava maye
from abhi.models import * 
from reportlab.pdfgen import canvas #pdf file banava mate  
# Create your views here.
def hello1(request):
	return HttpResponse("<h1><center>abhishek is a bca student")

@require_http_methods(["GET"])
def test(request):
	import datetime
	now=datetime.datetime.now()
	return HttpResponse(f"date time is: {now}")	

def test2(request):
	name3={'desc':"dfuhed","date":"12345"} 
	return render(request,'abhi.html',name3)	

def index(request):
	if request.method == "POST":
		form=EmpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("ok")	
		else:
			return HttpResponse("not ok")	
	else:	
		form = EmpForm()
		return render(request,"index.html",{'form':form})  


	

def index1(request):
	if request.method == "POST":
		form=StudentForm(request.POST,request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file']) 
			firstname= form.cleaned_data["firstname"]
			lastname= form.cleaned_data["lastname"]
			mobile= form.cleaned_data["mobile"]
			date = form.cleaned_data["date"]
			file= form.cleaned_data["file"]
			student.objects.create(firstname=firstname,lastname=lastname,date=date,mobile=mobile,file=file)
			return HttpResponse("ok")	
		else:
			return HttpResponse("not ok")	
	else:	
		form = StudentForm()
		return render(request,"index1.html",{'form':form})  


def setsession(request):
	request.session["email"]="abhidhameliya94271@"
	request.session["name"]="Abhishek"
	return HttpResponse("session set")


def setcookie(request):
	response = HttpResponse("Cookie Set")  
	response.set_cookie("java","python")
	return response

def getcookie(request):
	tutorial  = request.COOKIES['java']
	return HttpResponse(tutorial)  

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  


def getfilefromdatabase(request):  #for database mathi lava mate
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = employee1.objects.all()  
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.id,employee.f_name,employee.l_name,employee.email])  
    return response  


def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.drawString(100,800 ,"abhishek int.")  
    p.showPage()  
    p.save()  
    return response      


def boot(request):
	return render(request,"boot.html")

