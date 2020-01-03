# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import os
import uuid

from django.db import models


class StarterModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields is not None:
            update_fields.append('modified_date')
        super(StarterModel, self).save(*args, **kwargs)


def generate_slider_image_name(instance, filename):
    pk = str(instance.pk)
    filename = str(uuid.uuid4()) + ".jpg"
    datetime_str = datetime.datetime.now().strftime("%Y/%m/%d")
    return os.path.join("slider/", datetime_str, pk, filename)


class Slider(StarterModel):
    image = models.ImageField(upload_to=generate_slider_image_name)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "%s" % self.image


def generate_product_image_name_galerry(instance, filename):
    pk = str(instance.pk)
    filename = str(uuid.uuid4()) + ".jpg"
    datetime_str = datetime.datetime.now().strftime("%Y/%m/%d")
    return os.path.join("home_gallery/", datetime_str, pk, filename)


class HomeGallery(StarterModel):
    image = models.ImageField(upload_to=generate_product_image_name_galerry)
    main_title = models.CharField(max_length=255, verbose_name=u"Üst Başlık")
    sub_title = models.CharField(max_length=255, verbose_name=u"Alt Başlık")
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "%s - %s" % (self.image, self.main_title)
