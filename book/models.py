from django.db import models

# Create your models here.

class all_list(models.Model):
  title = models.CharField(max_length = 255)
  bookfaceimg = models.CharField(max_length = 255)
  panelimg = models.CharField(max_length = 255)
  price = models.CharField(max_length = 500)
  desc = models.CharField(max_length = 500)
  link = models.CharField(max_length = 255)
  click = models.CharField(max_length = 255)

class detail(models.Model):
  bookname = models.CharField(max_length = 255)
  sample = models.CharField(max_length = 255)
  dt = models.CharField(max_length = 500)
  dd = models.CharField(max_length = 500)
  link = models.CharField(max_length = 255)