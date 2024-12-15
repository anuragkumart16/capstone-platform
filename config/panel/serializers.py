from rest_framework import serializers
from .models import MentorModel

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorModel
        fields = '__all__'