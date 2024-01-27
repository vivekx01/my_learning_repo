from django.shortcuts import render
from .models import Staff,Department,Service
# Create your views here.
def staffpageload(request):
    doctors = Staff.objects.all()
    context = {'doctors':doctors}
    return render(request,"doctors-staff.html",context)

def departmentspageload(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,"departments.html",context)

def dept_detailpageload(request,id):
    services = Service.objects.filter(dept=id)
    dept_name = Department.objects.get(id=id).dept_name
    dept_head = Department.objects.get(id=id).dept_head_name
    dept_contact = Department.objects.get(id=id).dept_contact
    context = {'services': services,'name':dept_name,'head':dept_head,'contact':dept_contact}
    return render (request,"dept_detail.html",context)