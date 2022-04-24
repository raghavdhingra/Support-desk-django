from django.shortcuts import render, redirect
from .models import RESOLUTION_STATUS, Request

def redirectUser(request):
    if request.user.is_staff:
        return redirect("/supportdesk/all-request")
    return redirect("/supportdesk/my-request")

def allRequest(request): # AGENT
    if not request.user.is_authenticated:
        return redirect("/")
    
    if not request.user.is_staff:
        return redirect("/")

    all_requests = Request.objects.all().order_by("-id")
    context = {
        "requests": all_requests,
    }

    return render(request, "agent/all-request.html", context)

def viewRequest(request, num): # AGENT / CUSTOMER
    if not request.user.is_authenticated:
        return redirect("/")

    try:
        user_req = Request.objects.get(pk=num)
        context = {
            "request": user_req,
            "is_staff": request.user.is_staff
        }

        return render(request, "view-request.html", context)
    except Exception as e:
        print(e)
        return render(request, "404.html")

def myRequest(request): # CUSTOMER
    if not request.user.is_authenticated:
        return redirect("/")

    auth_user = request.user
    context = {}

    if auth_user.is_authenticated:
        req = Request.objects.filter(created_by=auth_user).order_by("-created_on")
        context['requests'] = req
        context['my_num_of_request'] = len(req)

    return render(request, "customer/my-request.html", context)

def createRequest(request): # CUSTOMER
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        Request.objects.create(title=title, description=description, created_by=request.user, is_priority=(priority == "on"))
        return redirect("/supportdesk/my-request")
        
    auth_user = request.user
    my_request_num = Request.objects.filter(assigned_to=auth_user)

    context = {
        "my_num_of_request": len(my_request_num)
    }
    return render(request, "customer/create-request.html", context)


def completeRequest(request, id):
    my_request = Request.objects.get(pk=id)
    my_request.status = RESOLUTION_STATUS.COMPLETED
    my_request.save()
    return redirect("/supportdesk/all-request")


def assignRequest(request, id):
    my_request = Request.objects.get(pk=id)
    my_request.assigned_to = request.user
    my_request.save()
    return redirect("/supportdesk/all-request")