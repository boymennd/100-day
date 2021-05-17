from django.shortcuts import render, HttpResponse
from .forms import ContactForms
# Create your views here.
def contact(request):
    context = {'cf': ContactForms}
    return render(request, "contact_app/contact.html", context)
def get_contact(request):
    if request.method == 'POST':
        cf = ContactForms(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("Successfully!!!")
    else:
        return HttpResponse("It not post")