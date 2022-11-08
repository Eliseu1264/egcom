
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ItensPedidoVendaFormSet, PedidoVendaForm
from .models import Cliente, PedidoVenda, Produto
from django.views.generic.base import TemplateView
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'index.html', context)


class vtreino(TemplateView): 
    template_name = 'treino.html'
    extra_context = {'produtos': Produto.objects.all()}

def print_rel(request, campo, conteudo):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'

        # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    if campo == None:
        lista_prod = Produto.objects.order_by('descricao')
    else:
        lista_prod = Produto.objects.filter(campo=conteudo)
    
    lin = 750
    p.drawString(200, lin, "LISTAGEM DE PRODUTOS")
    lin -= 20
    qtd = 0
    for lp in lista_prod:
       qtd += 1
       lin -= 20
       p.drawString(10, lin, lp.descricao) 
    
    lin -= 40   
    p.drawString(10, lin, 'TOTAL DE REGISTROS:  '+str(qtd))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


###############################################
### Clientes
###############################################
class ListClienteView(ListView):
    models = Cliente
    template_name = 'cliente_list.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    paginate_by = 8
    ordering = 'nome'

class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'fantasia', 'cnpj', 'cpf', 'contato', 'sexo', 'logradouro', 'compl', 'num', 'bairro',
	          'municipio', 'uf','cep', 'insc_estadual', 'insc_municipal', 'vendedor', 'email', 'email_nf',
              'cod_area_celular_1', 'celular_1', 'cod_area_celular_2', 'celular_2', 'cod_area_celular_3',
              'celular_3', 'credito_limite', 'observacao', 'ativo']   
    success_url = reverse_lazy('add_cliente')
    

class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'fantasia', 'cnpj', 'cpf', 'contato', 'sexo', 'logradouro', 'compl', 'num', 'bairro', 
	          'municipio', 'uf','cep', 'insc_estadual', 'insc_municipal', 'vendedor', 'email', 'email_nf',
              'cod_area_celular_1', 'celular_1', 'cod_area_celular_2', 'celular_2', 'cod_area_celular_3',
              'celular_3', 'credito_limite', 'observacao', 'ativo']  
    success_url = reverse_lazy('list_cliente')

class DeleteClienteView(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_del.html'
    success_url = reverse_lazy('list_cliente')

###############################################
### Produtos do estoque 
###################3###########################
class ListProdutoView(ListView):
    models = Produto
    template_name = 'produto_list.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    paginate_by = 8
    ordering = 'descricao'
    
    def get_queryset(self):
        p_valor = self.request.GET.get('descricao')
        if p_valor:
            produtos = Produto.objects.filter(descricao__icontains=p_valor)
        else:
            produtos = Produto.objects.all()
        return produtos

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

###############################################
### Pedidos de Venda
###################3###########################
class ListPedidoVendaView(ListView):
    models = PedidoVenda
    template_name = 'pedidovenda_list.html'
    queryset = PedidoVenda.objects.all()
    context_object_name = 'pedidovendas'
    paginate_by = 8
    ordering = 'id'

class CreatePedidoVendaView(CreateView):
    model = PedidoVenda
    template_name = 'pedidovenda_form.html'
    form_class = PedidoVendaForm
    fields = ['cliente', 'qtdparcelas', 'comissao', 'vendedor', 'dataentrega', 'datacancelamento', 'observacao', 'ativo']
    success_url = reverse_lazy('add_pedido_venda')

    def get(self, request, *args, **kwargs):
            self.object = None
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ItensPedidoVenda_form = ItensPedidoVendaFormSet()
            return self.render_to_response(
                self.get_context_data(form=form,
                                    ItensPedidoVenda_form=ItensPedidoVenda_form
                                     ))

    def post(self, request, *args, **kwargs):
            self.object = None
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ItensPedidoVenda_form = ItensPedidoVendaFormSet(self.request.POST)
            if (form.is_valid() and ItensPedidoVenda_form.is_valid()):
                return self.form_valid(form, ItensPedidoVenda_form)
            else:
                return self.form_invalid(form, ItensPedidoVenda_form)

    def form_valid(self, form, ItensPedidoVenda_form):
            self.object = form.save()
            ItensPedidoVenda_form.instance = self.object
            ItensPedidoVenda_form.save()
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ItensPedidoVenda_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ItensPedidoVenda_form=ItensPedidoVenda_form))

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