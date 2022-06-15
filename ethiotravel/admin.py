from django.contrib import admin
from .models import destination, best_tips, intros, testimony, discount

# Register your models here.

admin.site.register(destination)
admin.site.register(best_tips)
admin.site.register(intros)
admin.site.register(testimony)
admin.site.register(discount)