from django.contrib import admin

# Register your models here.
from .models import User

#registered admin for the app to increase testing capabilities
admin.site.register(User)