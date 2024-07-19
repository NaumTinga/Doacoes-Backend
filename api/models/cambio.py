from django.db import models
import uuid

from rest_framework.exceptions import ValidationError
from wheel.metadata import _

from api.models import moeda


class Cambio(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    taxa = models.DecimalField(max_digits=20, decimal_places=3)
    moeda_base = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, null=True, related_name='moeda_base')
    moeda_alvo = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, null=True, related_name='moeda_alvo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taxa

    # Method to convert the currency when creating Requisicao
    @staticmethod
    def get_exchange_rate(moeda_base, moeda_alvo):

        try:
            cambio = Cambio.objects.get(moeda_base=moeda_base, moeda_alvo=moeda_alvo)
            return cambio.taxa
        except Cambio.DoesNotExist:
            raise ValidationError(_('Exchange rate not found for the given currencies.'))

