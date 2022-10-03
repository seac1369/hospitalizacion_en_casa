from django.contrib import admin
from .models.usuarios import User
from .models.personal_medico import Personal

admin.site.register(User)
admin.site.register(Personal)

# Register your models here.
