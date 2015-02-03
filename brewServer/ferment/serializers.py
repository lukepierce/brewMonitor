from rest_framework import serializers
from ferment.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'brew_name', 'temperature', 'time')
