from rest_framework import serializers


from api.models.conta import Conta


class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = '__all__'
