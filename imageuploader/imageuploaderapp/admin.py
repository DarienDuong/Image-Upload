from django.contrib import admin

# Register your models here.
from imageuploaderapp.models import Topics, Images

admin.site.register(Topics)
admin.site.register(Images)