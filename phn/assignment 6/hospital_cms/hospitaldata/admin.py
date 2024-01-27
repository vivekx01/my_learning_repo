from django.contrib import admin
from .models import Staff,Service,Department
# Register your models here.
admin.site.register(Department)
admin.site.register(Service)
admin.site.register(Staff)
