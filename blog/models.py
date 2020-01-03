from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

from home.models import StarterModel


class Blog(StarterModel):
    content = RichTextField(config_name='default')
    is_active = models.BooleanField(default=True)
