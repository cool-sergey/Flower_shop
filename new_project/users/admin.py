from django.contrib import admin

# Register your models here.
from users.models import User
from example.admin import BucketAdmin   

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BucketAdmin,)