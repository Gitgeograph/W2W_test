from rest_framework import serializers
from tapp.models import *

class TModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TModel
        fields = ('text',)