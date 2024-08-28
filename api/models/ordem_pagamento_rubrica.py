from django.db import models
import uuid
from api.models import conta, assinante, fornecedor, beneficiario, actividade, requisicao_rubrica, sub_rubrica


class TipoOperacao(models.TextChoices):
    TRANSFERENCIA_BANCARIA = 'TRANSFERÊNCIA BANCÁRIA'
    LEVANTAMENTO_NUMERARIO = 'LEVANTAMENTO NUMERÁRIO'
    CHEQUE = 'CHEQUE'


class OrderPagamentoRubrica(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    conta_ordenador = models.ForeignKey(conta.Conta, on_delete=models.PROTECT,
                                        related_name='op_rubrica_conta_ordenador')
    conta_destino = models.ForeignKey(conta.Conta, on_delete=models.PROTECT,
                                      related_name='op_rubrica_conta_destino', null=True)
    assinante_principal = models.ForeignKey(assinante.Assinante, on_delete=models.PROTECT, null=True,
                                            related_name='op_rubrica_assinante_principal')
    assinante_secundario = models.ForeignKey(assinante.Assinante, on_delete=models.PROTECT, null=True,
                                             related_name='op_rubrica_assinante_secundario')
    fornecedor = models.ForeignKey(fornecedor.Fornecedor, on_delete=models.PROTECT, null=True,
                                   related_name='op_rubrica_fornecedor')
    beneficiario = models.ForeignKey(beneficiario.Beneficiario, on_delete=models.PROTECT, null=True,
                                     related_name='op_rubrica_beneficiario')
    actividade = models.ForeignKey(actividade.Actividade, on_delete=models.PROTECT, null=True,
                                   related_name='op_rubrica_actividade')
    sub_rubrica = models.ForeignKey(sub_rubrica.SubRubrica, on_delete=models.PROTECT, null=True,
                                    related_name='op_rubrica_sub_rubrica')
    requisicoes_rubricas = models.ManyToManyField(requisicao_rubrica.RequisicaoRubrica,
                                                  blank=True,
                                                  related_name='op_rubrica_requisicoes_rubricas')
    tipo_operacao = models.TextField(choices=TipoOperacao.choices, null=True, max_length=300)
    descricao = models.TextField(null=True, max_length=500)
    # Somatorio do valor das requisicoes selecionadas
    valor_extenso = models.TextField(null=True, max_length=500)
    valor = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
