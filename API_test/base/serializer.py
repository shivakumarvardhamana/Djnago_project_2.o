
from rest_framework import serializers
from . models import employe,test

class itemserializ(serializers.ModelSerializer):
    class Meta:
        model=test
        fields='__all__'