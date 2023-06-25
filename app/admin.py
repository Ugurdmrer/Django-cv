from django.contrib import admin
from .models import project, About , Service , Portfolio, Comment, Blog
# Register your models here.
admin.site.register(project)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(Blog)