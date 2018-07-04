#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from django.contrib import admin
from .models import Profile, News, Reader, System, Change

#---------------------------------------------------------
#    Custom Admins
#---------------------------------------------------------

class ProfileAdmin(admin.ModelAdmin):
    """
    Profile Admin
    """
    fieldsets = [
        ('Personal Information', {
                'fields': ['username','nickname','about','photo']
            }
        ),
        ('Contact Information', {
                'fields': ['telegram','skype','hipchat','phone']
            }
        ),
        ('System Information', {
                'fields': ['agent']
            }
        ),
    ]
    list_display = ('username','nickname','agent','created')
    search_fields = ('username','nickname')
    list_filter = ['created','agent']
    ordering = ('-created', )

class ReaderInline(admin.TabularInline):
    """
    Readers Inline
    """
    fieldsets = [
        (None, {
                'fields': ('reader', 'read_date',)
            }
        ),
    ]
    model = Reader
    readonly_fields=('read_date',)

class NewsAdmin(admin.ModelAdmin):
    """
    News Admin
    """
    fieldsets = [
        ('Notification Information', {
                'fields': ['subject','message','author']
            }
        ),
    ]
    inlines = [
        ReaderInline,
    ]
    list_display = ('subject','author','created')
    search_fields = ('subject','message')
    list_filter = ['created']
    ordering = ('-created', )

class SystemAdmin(admin.ModelAdmin):
    """
    System Admin
    """
    fieldsets = [
        ('System Information', {
                'fields': ['message','reader','link','read','created']
            }
        ),
    ]
    list_display = ('message','reader','link','read','created')
    search_fields = ('message','reader')
    list_filter = ['created','read']
    ordering = ('-created', )
    readonly_fields=('created',)

class ChangeAdmin(admin.ModelAdmin):
    """
    Change Admin
    """
    fieldsets = [
        ('Change Information', {
                'fields': ['subject','message','ticket','uol','rdm','impact','validate']
            }
        ),
        ('Date Information', {
                'fields': ['start_date','close_date','created']
            }
        ),
    ]
    list_display = ('subject','start_date','close_date','impact','validate')
    search_fields = ('ticket','uol','rdm')
    list_filter = ['created','impact','validate']
    ordering = ('-start_date', )
    readonly_fields=('created',)

# Register Custom Admins
admin.site.register(Profile, ProfileAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Change, ChangeAdmin)
