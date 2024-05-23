from rest_framework import serializers
from .models import SubjectScore

class SubjectScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectScore
        fields = '__all__'