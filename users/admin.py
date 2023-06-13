from django.contrib import admin
from .models import Profile, PointReport, Event

admin.site.register(Profile)
admin.site.register(PointReport)
admin.site.register(Event)

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the KOA Portal"
