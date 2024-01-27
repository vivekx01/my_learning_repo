from django.shortcuts import render

# Create your views here.
def homepageload(request):
    return render(request,'homepage.html')

def aboutuspageload(request):
    return render(request,'aboutus.html')

def servicespageload(request):
    return render(request,'services.html')

def infosupportpageload(request):
    return render(request,'info-support.html')

def faqpageload(request):
    return render(request,'faq.html')

def patientguidespageload(request):
    return render (request,'patient-guides.html')