from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import PedidoVenda, Produto

def index(request):
    context = {}
    return render(request, 'index.html', context)

class ListProdutoView(ListView):
    models = Produto
    template_name = 'produto_list.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = 'id'

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['descricao', 'compl', 'unidade', 'grupo', 'ativo', 'quantidade', 'preco_custo', 'preco_venda', 'observacao']
    success_url = reverse_lazy('add_produto')

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['descricao', 'compl', 'unidade', 'grupo', 'ativo', 'quantidade', 'preco_custo', 'preco_venda', 'observacao']
    success_url = reverse_lazy('list_produto')

class DeleteProdutoView(DeleteView):
    model = Produto
    queryset = Produto.objects.all()
    template_name = 'produto_del.html'
    success_url = reverse_lazy('list_produto')

class ListPedidoVendaView(ListView):
    models = PedidoVenda
    template_name = 'pedidovenda_list.html'
    queryset = PedidoVenda.objects.all()
    context_object_name = 'pedidovendas'
    paginate_by = 10
    ordering = 'id'

class CreatePedidoVendaView(CreateView):
    model = PedidoVenda
    template_name = 'pedidovenda_form.html'
    fields = ['cliente', 'qtdparcelas', 'comissao', 'vendedor', 'dataentrega', 'datacancelamento', 'observacao', 'ativo']
    success_url = reverse_lazy('add_pedido_venda')

class UpdatePedidoVendaView(UpdateView):
    model = PedidoVenda
    template_name = 'pedidovenda_form.html'
    fields = ['cliente', 'qtdparcelas', 'comissao', 'vendedor', 'dataentrega', 'datacancelamento', 'observacao', 'ativo']
    success_url = reverse_lazy('list_pedido_venda')

class DeletePedidoVendaView(DeleteView):
    model = PedidoVenda
    template_name = 'pedidovenda_del.html'
    success_url = reverse_lazy('list_pedido_venda')
    
class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login:loginview")