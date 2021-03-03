from django.contrib import admin

from .models import Post, Parts
# Register your models here.
admin.site.register(Post)
admin.site.register(Parts)


'''class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    list_display = ['username', 'email', 'age']


admin.site.register(CustomUser, CustomUserAdmin)
'''
