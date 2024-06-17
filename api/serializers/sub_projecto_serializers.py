from rest_framework import serializers

from api.models.sub_projecto import SubProjecto


class SubProjectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProjecto
        fields = '__all__'
