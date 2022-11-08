from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import PedidoVenda, ItensPedidoVenda

class PedidoVendaForm(ModelForm):
    class Meta:
        model = PedidoVenda
        fields = ['cliente', 'qtdparcelas', 'comissao', 'vendedor', 'dataentrega', 'datacancelamento', 'observacao', 'ativo']

ItensPedidoVendaFormSet = inlineformset_factory(                                                
                                                PedidoVenda, 
                                                ItensPedidoVenda, 
                                                form = PedidoVendaForm,                                              
                                                fields = ('pedido', 'produto', 'quantidade', 'preco', 'desconto_perc', 'detalhamento'),
                                                extra=0,
                                                can_delete=True
                                                )