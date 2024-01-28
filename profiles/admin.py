from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('user', )
    search_fields = ['user']
    summernote_fields = ('content',)
# Register your models here.
