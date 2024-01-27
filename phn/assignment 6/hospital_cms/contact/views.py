from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def contactpageload(request):
    return render(request,'contactus.html')

# handling user form
from django.http import JsonResponse
from .models import Contact

def submit_form(request):
    if request.method == 'POST':
        # Get the form data
        first = request.POST['first']
        last = request.POST['last']
        name = first +" "+ last
        email = request.POST['email']
        message = request.POST['message']

        # Create a new Contact instance
        contact = Contact(name=name, email=email, message=message)
        
        # Save the contact object
        contact.save()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Handle GET requests or other cases
        return render(request, 'contact.html')

