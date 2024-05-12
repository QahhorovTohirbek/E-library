from . import models
from django.contrib import admin


admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Press)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Review)
admin.site.register(models.Cart)
admin.site.register(models.Wishlist)
