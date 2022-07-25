from django.contrib import admin
from customer.models import Register

admin.site.site_header = 'E-Shopping'
admin.site.index_title = 'Master Admin'


class RegisterAdmin(admin.ModelAdmin):
	list_display = ['id', 'name','email','contact']
	search_fields = ['name','email']


admin.site.register(Register,RegisterAdmin)

