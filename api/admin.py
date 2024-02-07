from django.contrib import admin
from . models import Profile

@admin.register(Profile)
class Profilemodeladmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','state','gender','location','pimage','rdoc']
    

# Register your models here.
