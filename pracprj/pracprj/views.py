from django.http import HttpResponse
from django.shortcuts import render

# routing functions
def home(request):
    # return HttpResponse("Web Applictaion working perfectly!!")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')