from django.contrib import admin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser,TractorDetail
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username','mobile_number', 'address']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number', 'address')}),
    ) #this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)
# Register your models here.
@admin.register(TractorDetail)
class TractorDetailAdmin(admin.ModelAdmin):
    list_display=['id','user','brand','model_no','hp_category','implements']
