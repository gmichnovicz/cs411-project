from django.contrib import admin
from .models import Post
from .models import Show
# Register your models here.

admin.site.register(Show)
admin.site.register(Post)