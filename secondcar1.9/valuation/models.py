# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CarBrand(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_brand'


class CarmodelInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    p_id = models.IntegerField()
    name = models.CharField(max_length=150)
    onsale = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carmodel_info'


class DistrictInfo(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    p_id = models.SmallIntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'district_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class SecCarinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=200)
    first_time = models.CharField(max_length=20, blank=True, null=True)
    mileage = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sec_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    new_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    re_addr = models.CharField(max_length=20, blank=True, null=True)
    displacement = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_carinfo'


class Users(models.Model):
    # 电话号码 - CharField()
    uphone = models.CharField(max_length=11)
    # 密码 - CharField()
    upwd = models.CharField(max_length=20)
    # 电子邮件 - EmailField()
    uemail = models.EmailField()
    # 用户名 - CharField()
    uname = models.CharField(max_length=20)
    # 启用/禁用 - BooleanField() 默认值为:
    isActive = models.BooleanField(default=True)