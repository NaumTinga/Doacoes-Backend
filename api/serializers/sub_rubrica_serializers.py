from rest_framework import serializers

from api.models.sub_rubrica import SubRubrica


class SubRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRubrica
        fields = '__all__'

        