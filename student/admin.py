from django.contrib import admin
from student.models import Contact,Profile,Course, Video,Profile,Contact

admin.site.site_header = "Kapil IT Skill HUB | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')  # Fields to be displayed in the admin list view
    search_fields = ('title', 'description')  # Fields to be searchable in the admin list view

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','images','videos')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Profile)


