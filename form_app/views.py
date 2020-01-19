# Create your views here.
from django.shortcuts import render,redirect
def index(request):
    return render(request,"index.html")

def create_user(request):
    name_from_form = request.POST['name']
    strnum = request.POST['strawberry']
    rosnum =  request.POST['roseberry']
    appnum = request.POST['apple']
    total = int(strnum) + int(rosnum) + int(appnum)
    context = {
        "name_on_template" : name_from_form,
        "strberry" : strnum,
        "rosberry": rosnum,
        "apple": appnum,
        "total": total,
    }
    return render(request,"show.html",context)


    