#Modeled after http://www.django-rest-framework.org/tutorial/1-serialization/

from django.forms import widgets #I think this import may not be necessary
from rest_framework import serializers
from ferment.models import Data

class DataSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    brew_name = serializers.CharField(max_length=100)
    time = serializers.TimeField()
    temperature = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        """
        Create and return a new Data instance, given the validated data
        """
        return Data.objects.create(**validated_data)

    #Did not include update method because Data objects should not be modified
