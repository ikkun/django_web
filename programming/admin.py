from django.contrib import admin
from .models import Programming_Authors

# Register your models here.
class AdminProgrammingAuthors(admin.ModelAdmin):
    list_display = ['programming_languages','authors','date_of_birth']
admin.site.register(Programming_Authors,AdminProgrammingAuthors)
