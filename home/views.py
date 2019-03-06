from django.shortcuts import render

# Create your views here.
def index(request):
    """ a vewi that displayes the index page """
    return render(request, 'index.html')