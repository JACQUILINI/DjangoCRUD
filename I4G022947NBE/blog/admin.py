from atexit import register
from curses import meta
import site
from django.contrib import admin

from DjangoCrud.DjangoCRUD.I4G022947NBE.blog.models import Post

# Register your models here.

admin.site.register(Post)
