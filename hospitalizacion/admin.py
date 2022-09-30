from django.contrib import admin
from .models.usuarios import User
from .models.roles import Roles

admin.site.register(User)
admin.site.register(Roles)

# Register your models here.
