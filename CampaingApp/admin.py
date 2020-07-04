from django.contrib import admin

from .models import (
    Campaing, 
    Quest, 
    Pj, 
    Race,
)


admin.site.register(Campaing)
admin.site.register(Quest)
admin.site.register(Pj)
admin.site.register(Race)