from django.shortcuts import render
from django.http import HttpResponse

# TODO - downnload test_module.py and test your app
def index(request):
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'your_name' :'Adam Janca'}
	return render(request, 'rango/about.html', context=context_dict)