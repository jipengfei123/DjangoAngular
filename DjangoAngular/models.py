from django.db import models


class Hotel(models.Model):
    room = models.CharField(max_length=30, verbose_name="名称")
    cf = models.IntegerField(verbose_name="cf")
    br = models.IntegerField(verbose_name="br")

    class Meta:
        verbose_name_plural = "Hotel"

    def __str__(self):
        return self.room


class Mysite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField(max_length=100)
    num = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Student(object):
    # 有点类似其它高级语言的构造函数
    def __init__(self, name, score):
        self.name = name
        self.score = score
