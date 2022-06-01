from django.db import models
from rest_framework import serializers
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0.0)
    duration = models.FloatField(default=0.0)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
