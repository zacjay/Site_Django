from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        contact = Contact(fname=fname, lname=lname, uname=uname, date=datetime.today())
        contact.save()
        messages.success(request, 'Updated.')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
