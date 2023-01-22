from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContextForm,SnippetForm

# Create your views here.
def context(request):
	if request.method == 'POST':
		form = ContextForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email= form.cleaned_data['email']
			print(name,email)


	form = ContextForm()
	return render(request,'form.html',{'form':form})


def snippet_detail(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			form.save()


	form = SnippetForm()
	return render(request,'form.html',{'form':form})


