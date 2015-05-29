from django.contrib import admin

from .models import Join


# Register your models here.
class JoinAdmin(admin.ModelAdmin):
    '''
        Admin View for Join
    '''
    list_display = ['email', 'ref_id', 'friend', 'timestamp', 'updated']

    class meta:
        model = Join


admin.site.register(Join, JoinAdmin)
