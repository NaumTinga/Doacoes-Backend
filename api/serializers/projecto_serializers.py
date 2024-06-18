from rest_framework import serializers

from api.models.projecto import Projecto


class ProjectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecto
        fields = '__all__'
