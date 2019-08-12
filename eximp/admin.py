from django.contrib import admin

# Register your models here.
from .models import ExImp
admin.site.register(ExImp)

from .models import Language
admin.site.register(Language)