from django.shortcuts import HttpResponse, render

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
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

