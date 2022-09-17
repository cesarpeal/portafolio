from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html', {
		'title':'Inicio'
	})

def about(request):
	return render(request, 'about.html', {
		'title':'Sobre mí'
	})