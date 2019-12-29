from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.
from home.models import Slider

admin.site.register(Slider)
