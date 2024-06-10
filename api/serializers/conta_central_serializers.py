from rest_framework import serializers


from api.models.conta_central import ContaCentral


class ContaCentralSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContaCentral
        fields = '__all__'
