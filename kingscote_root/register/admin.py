from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'en_level', 'submitted')
    list_filter = ('id', 'submitted')
    readonly_fields = ('submitted',)



admin.site.register(Student, StudentAdmin)

# Register your models here.
