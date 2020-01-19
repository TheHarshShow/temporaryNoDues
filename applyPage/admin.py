from django.contrib import admin
from applyPage.models import Department, LabRequestEntry, Lab, Student,  BTP, Other,  BTPRequestEntry, OthersRequestEntry

# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Lab)
admin.site.register(BTP)
admin.site.register(Other)
admin.site.register(LabRequestEntry)
admin.site.register(BTPRequestEntry)
admin.site.register(OthersRequestEntry)
