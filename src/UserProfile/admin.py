from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from .models import MyUser,Profile



class UserAdmin(BaseUserAdmin):
   
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email', 'reg_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('reg_number',)}),
        ('Permissions', {'fields': ('is_admin','is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'reg_number', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','email','reg_number',)
    ordering = ('username','email','reg_number',)
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)
