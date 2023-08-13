from django.shortcuts import HttpResponse, render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    # context = {
    #     "variable": "This is a variable.",
    #     "variable2": "This is second variable."
    # }
    # return render(request, "index.html", context)
    return render(request, "index.html")
    # return HttpResponse("This is home page.")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

