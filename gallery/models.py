from __future__ import unicode_literals

import datetime
import os
import uuid

from django.db import models

# Create your models here.
from home.models import StarterModel


def generate_slider_image_name(instance, filename):
    pk = str(instance.pk)
    filename = str(uuid.uuid4()) + ".jpg"
    datetime_str = datetime.datetime.now().strftime("%Y/%m/%d")
    return os.path.join("gallery/", datetime_str, pk, filename)


class Gallery(StarterModel):
    image = models.ImageField(upload_to=generate_slider_image_name)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "%s" % self.image
