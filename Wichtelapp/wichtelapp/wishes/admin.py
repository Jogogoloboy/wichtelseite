from django.contrib import admin

# Register your models here.
from .models import Wish
admin.site.register(Wish)
from .models import Phase
admin.site.register(Phase)
