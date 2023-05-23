from django.shortcuts import render,redirect

# from .forms import detailsform
from .models import Member

# Create your views here.
def  index(request):
    print("Index")
    mem = Member.objects.all()
    return render(request , 'index.html',{'mem':mem})

def add(request):
        if request.method == "POST":
            firstname=request.POST['firstname']
            lastname=request.POST['last']
            countryname=request.POST['country']
            obj = Member.objects.create(firstname=firstname, lastname=lastname, countryname=countryname)
            obj.save()
            return(redirect('/'))
        return render(request,'add.html')

# def addrec(request):
#     if request.method == "POST":
#         name=request.POST['name']
#         age=request.POST['age']
#         country=request.POST['country']
#         obj = Member.objects.addrec(name=name, age=age, country=country)
#         obj.save()
#         return(redirect('/'))
    
#     return render(request,'add.html')

def delete(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")


def update(request,id):
    mem = Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request, id):
    firstname = request.POST["firstname"];
    lastname = request.POST["lastname"];
    countryname = request.POST["countryname"];
    mem=Member.objects.get(id=id)
    mem.firstname=firstname
    mem.lastname=lastname
    mem.countryname=countryname
    mem.save()
    
    return redirect("/")  
        
    

