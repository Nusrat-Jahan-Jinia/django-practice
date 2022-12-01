from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from django.core.paginator import Paginator

def home(request):
    data={
        "title":"hello nusrat",
        "courselist":["php","java","js"]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to my project")

def Course(request):
    return HttpResponse("hello course")    

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))  
            n2=eval(request.POST.get("num2"))
            n3=eval(request.POST.get("num3"))
            n4=eval(request.POST.get("num4"))
            n5=eval(request.POST.get("num5"))
            t=n1+n2+n3+n4+n5
            p=t*100/500
            if p>=60:
                d="First Division"
            elif p>=48:
                d="Second"
            elif p>=35:
                d="Second"
            else:
                d="Second"
            data={
                'total':t,
                'per':p,
                "div":d
            }
            return render(request, "calculator.html",data)
    except:
        data={
                'total':'',
                'per':'',
                "div":''
            }
        return render(request, "calculator.html",data)


def service(request):
    servicesData=Service.objects.all()
    paginator=Paginator(servicesData,1)
    page_number=request.GET.get('page')
    ServiceDataFinal=paginator.get_page(page_number)
    totalPage=ServiceDataFinal.paginator.num_pages

    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
         servicesData=Service.objects.filter(service_title__icontains=st)   
    data={
        'servicesData':ServiceDataFinal,
        'lastPage':totalPage,
        'totalPagelist':[n+1 for n in range(totalPage)]
    }
    return render(request,'service.html',data)

def serviceDetails(request,service_slug):
    singleService=Service.objects.get(service_slug=service_slug)
    data={
        'singleService':singleService
    }
    return render(request,"serviceDetails.html",data)