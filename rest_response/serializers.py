from rest_framework import serializers
from main.models import loginfo

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginfo
        fields = '__all__'