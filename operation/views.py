

from django.shortcuts import render, redirect
from .models import crud

# Create your views here.
def index(request):
    users = crud.objects.all()
    return render(request, 'index.html' , {'users':users})

def create(request):
    return render(request,'create.html')

def addusers(request):
    nameValue = request.POST.get("name")
    emailValue = request.POST.get("email")
    countryValue = request.POST.get("country")
    stateValue = request.POST.get("state")
    cityValue = request.POST.get("city")
    crud(uname=nameValue,email=emailValue,country=countryValue,state=stateValue,city=cityValue).save()
    return redirect('/')

def edit(request,id):
    user = crud.objects.filter(id=id)[0]
    return render(request, 'edit.html', {"user":user})

def view(request,id):
    user = crud.objects.filter(id=id)[0]
    return render(request, 'view.html', {"user":user})

def updateuser(request,id):
    nameValue = request.POST.get("name")
    emailValue = request.POST.get("email")
    countryValue = request.POST.get("country")
    stateValue = request.POST.get("state")
    cityValue = request.POST.get("city")
    crud(id=id,uname=nameValue,email=emailValue,country=countryValue,state=stateValue,city=cityValue).save()
    return redirect('/')

def deleteuser(request,id):
    crud.objects.filter(id=id).delete()
    return redirect('/')