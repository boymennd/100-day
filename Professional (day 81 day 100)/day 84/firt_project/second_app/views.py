from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'second_app/home1.html')