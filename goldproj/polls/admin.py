from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Signal)
admin.site.register(Material)
admin.site.register(Wrapper)
admin.site.register(NewsWrapper)
admin.site.register(News)
