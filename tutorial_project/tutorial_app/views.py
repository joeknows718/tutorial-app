from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context_dict = {'boldmessage':'Tutorials Here' }


	return render(request, 'index.html', context_dict)

def about(request):
	return HttpResponse('About Us')