from django.contrib import admin

# Register your models here.
from .models import AdoptInfo, AnimalInfo, AssistInfo, ManagerInfo, UserInfo,WaitAdopt
admin.site.register([AdoptInfo, AnimalInfo, AssistInfo, ManagerInfo, UserInfo,WaitAdopt])
