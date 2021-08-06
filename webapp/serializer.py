from typing import Set
from django.db.models import fields
from rest_framework import serializers
from .models import employees


class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'
