from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm

from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'phone_number',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number',)}),
    )

admin.site.register(User, UserAdmin)