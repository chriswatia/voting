from django.contrib import admin
from .models import Category, County, Candidate


admin.site.register(Category)
admin.site.register(County)
admin.site.register(Candidate)
