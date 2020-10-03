from django.shortcuts import render, HttpResponse
from datetime import datetime
from Sample_app.models import Contact, Visit
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')
    
def contact(request):
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email= request.POST.get('email', '')
        contact=request.POST.get('contact', '')
        Query=request.POST.get('query', '')
        desc=request.POST.get('desc', '')
        contact = Contact(fname=fname, lname=lname, email=email, contact=contact, Query=Query, desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent')
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')


def visit(request):

    if request.method=="POST":
        Name = request.POST.get('V_Name', '')
        Company= request.POST.get('V_Company', '')
        Address=request.POST.get('V_Address', '')
        Contact=request.POST.get('V_Contact', '')
        Email=request.POST.get('V_email', '')
        Query=request.POST.get('V_query', '')
        desc=request.POST.get('V_desc', '')
        contact = Visit(Name=Name, Company=Company, Email=Email,Address=Address, Contact=Contact, Query=Query, desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Thanks For Your Enquiry, Will Contact You Soon')
    return render(request, 'visit.html')

def login(request):
    return render(request, 'login.html')

def project(request):
    return render(request, 'project.html')