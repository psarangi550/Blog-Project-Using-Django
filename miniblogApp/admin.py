from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)#here registering the models
class PostAdmin(admin.ModelAdmin):
    list_display=["title","desc"]
