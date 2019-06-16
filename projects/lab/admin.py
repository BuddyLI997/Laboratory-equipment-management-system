from django.contrib import admin

# Register your models here.
from lab.models import Student,Manufactor,Device,LabAdmin,AdminRecord,Admincheck,StudentRecord,DeviceinRecord
admin.site.register([Student,Manufactor,Device,LabAdmin,AdminRecord,Admincheck,StudentRecord,DeviceinRecord])