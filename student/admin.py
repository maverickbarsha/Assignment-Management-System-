from django.contrib import admin
from django.contrib.auth.models import Group
from student.models import MyUser, Assignment, Submission

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email','full_name','teacher','student']
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.unregister(Group)
