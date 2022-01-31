# Copyright 2007 Google, Inc. All Rights Reserved.
# Licens

from django.db import models

#고객 모델
class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers',default='no_picture.JPG')

    def __str__(self):
        return str(self.name)
