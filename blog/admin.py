from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.
from blog.models import Blog


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Blog, BlogAdmin)
