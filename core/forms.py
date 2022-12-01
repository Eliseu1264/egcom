from django.forms.models import inlineformset_factory
from django import forms
from core.models import PedidoVenda, ItensPedidoVenda

class PedidoVendaForms(forms.ModelForm):
    class Meta:
        model = PedidoVenda
        exclude = ['date']

class ItensPedidoVendaForms(forms.ModelForm):
    model = ItensPedidoVenda    
    # fields = ['produto', 'quantidade', 'preco', 'desconto_perc', 'detalhamento']   
    
    class Meta:
        exclude = ['pedidovenda']   
        

ItensPedidoVendaFormSet = inlineformset_factory(PedidoVenda, ItensPedidoVenda, form=ItensPedidoVendaForms, extra=1, labels=None )