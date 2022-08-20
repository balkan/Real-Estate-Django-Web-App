from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name="Ekleyen")
  title = models.CharField(max_length=200, verbose_name="baslik")
  address = models.CharField(max_length=200, verbose_name="adres")
  city = models.CharField(max_length=100, verbose_name="sehir")
  state = models.CharField(max_length=100, verbose_name="sehir")
  zipcode = models.CharField(max_length=20, verbose_name="posta kodu")
  description = models.TextField(blank=True, verbose_name="aciklama")
  price = models.IntegerField(verbose_name="fiyat")
  bedrooms = models.IntegerField(verbose_name="yatak odasi sayisi")
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="mutfak sayisi")
  garage = models.IntegerField(default=0, verbose_name="garaj")
  sqft = models.IntegerField(verbose_name="metrekare")
  lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="tapu no")
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Ana resim")
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True, verbose_name="yayinda mi")
  list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Yayinlanma tarihi")
  def __str__(self):
    return self.title