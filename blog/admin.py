from django.contrib import admin
from .models import Post
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',         {'fields': ['title']}),
        ('Content', {'fields': ['content']}),
        ('Date information', {'fields': ['date_posted']}),
        ('Author', {'fields': ['author']}),
    ]
    

#     # list_display = ('question_text', 'pub_date', 'was_published_recently')
#     # list_filter = ['pub_date']
#     # search_fields = ['question_text']



admin.site.register(Post, PostAdmin)