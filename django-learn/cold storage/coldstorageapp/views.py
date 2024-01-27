from django.shortcuts import render

# Create your views here.
def homepageview(request):
    #code to load the homepage
    return render(request,'homepage.html')