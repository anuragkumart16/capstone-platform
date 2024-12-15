from rest_framework import serializers
from .models import MarksModel

class MarksModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = MarksModel
        fields = '__all__'