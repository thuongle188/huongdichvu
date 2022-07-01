from django.contrib import admin
from .models import doctor, registererForm
from .models import customer
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display =('id','name','time')
    search_fields = ['name','time']
    list_filter =('id','name','time')
class CusAdmin(admin.ModelAdmin):
    list_display =('id','name','phone')
    search_fields = ['name','phone']
    list_filter =('id','name','phone')
class RegisteredFormdmin(admin.ModelAdmin):
    list_display =('id','customer_name','phone','doctor','schedule')
    search_fields = ['customer_name','phone','doctor','schedule']
    list_filter =('id','customer_name','phone','doctor','schedule')   
     
admin.site.register(doctor,DoctorAdmin)
admin.site.register(registererForm,RegisteredFormdmin)
admin.site.register(customer,CusAdmin)

