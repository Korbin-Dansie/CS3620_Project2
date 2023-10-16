from django.contrib import admin

# Register your models here.
from .models import Story
admin.site.register(Story)

from .models import Prompt
admin.site.register(Prompt)