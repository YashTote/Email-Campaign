from django.contrib import admin
from endpoint.models import *
# Register your models here.

admin.site.register(Campaign)
admin.site.register(Subscriber)
admin.site.register(Category)
admin.site.register(CategoryRelationship)
admin.site.register(DeliveryRecord)