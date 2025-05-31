from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Name terlalu pendek.")
        return value.strip().title()
    
    def create(self, validated_data):

        reversed_word = ""

        for i in range(len(validated_data['name']) - 1, -1, -1):  # Mulai dari indeks terakhir ke 0
            reversed_word += validated_data['name'][i]

        validated_data['name'] = reversed_word.upper()
        return super().create(validated_data)