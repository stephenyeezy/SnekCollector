from django.contrib import admin

# import your models here
from .models import Snake, Feeding

# Register your models here.
admin.site.register(Snake)
admin.site.register(Feeding)
