#Modeled after http://www.django-rest-framework.org/tutorial/1-serialization/

from django.forms import widgets #I think this import may not be necessary
from rest_framework import serializers
from ferment.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'brew_name', 'temperature')
    # def create(self, validated_data):
    #     """
    #     Create and return a new Data instance, given the validated data
    #     """
    #     return Data.objects.create(**validated_data)

    #Did not include update method because Data objects should not be modified
