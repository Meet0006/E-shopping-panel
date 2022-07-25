from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
	return HttpResponse('Welcome to Django')


def demo(request):
	return HttpResponse('I am Demo Function')


def myhello(request):
	return HttpResponse('<h1>I am myhello function</h1>')


def html_design(request):
	return render(request, 'customer/design.html')


def mydata(request):
	context = {
				  'name'   :'Alkesh Kaba',
				  'company':'CreArt Solutions',
				  'city'   :'Ahmedabad',
				  'state'  :'Gujarat'
	          }
	return render(request, 'customer/mydata.html',context)