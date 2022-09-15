from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # necessary for modifying the admin dashboard
from . models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active') # fields to be displayed at the front page of the table in the database dashboard
    list_display_links = ('email', 'first_name', 'last_name') # clickable fields
    readonly_fields = ('last_login', 'date_joined') # read only should not be editable
    ordering = ('-date_joined',) # sorting using date_joined from the latest, note that the comma before the closing bracket is important

    filter_horizontal = () # this will display the "list_display" list in horizontal order
    list_filter = ()
    fieldsets = () # this will make the password field to be read only

admin.site.register(Account, AccountAdmin)
