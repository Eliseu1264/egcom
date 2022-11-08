from dataclasses import fields
from django.contrib import admin
from .models import Cargo, Cliente, ItensPedidoVenda, PedidoVenda, Produto, Vendedor, Contato, Municipio, Uf
from .models import Unidade, Grupo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fantasia', 'cpf', 'cnpj', 'email', 'uf')                
    search_fields = ['id', 'nome', 'fantasia', 'cpf', 'cnpj', 'email']
    list_display_links = ('id', 'nome')
    list_filter = ('contato','uf', 'municipio', 'vendedor')
    list_per_page = 8

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'email','cod_area_fone', 'fone', 'cod_area_celular', 
                    'celular', 'facebook', 'twitter', 'instagram', 'ativo', 'modificado')
    search_fields = ['id', 'nome', 'email']
    list_display_links = ('id', 'nome')
 
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'logradouro', 'num', 'compl', 'bairro', 'municipio', 
                    'cep', 'uf', 'email', 'cod_area_celular_1', 'celular_1', 
                    'cod_area_celular_2', 'celular_2', 'ativo', 'modificado')
    list_display_links = ('id', 'nome')
    search_fields = ['id', 'nome']

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo', 'ativo', 'modificado')
    search_fields = ['id', 'cargo']
    
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cmun', 'uf', 'siaf', 'ativo', 'modificado')
    search_fields = ['id', 'nome', 'cmun', 'uf']
    
@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'codmun', 'maskfone', 'aliq_mva', 'carga_liq', 
                    'carga_imp', 'carga_simples','tempo_carrego', 'tempo_entrega', 'ativo', 'modificado')
    search_fields = ['id', 'nome', 'sigla', 'codmun']
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'compl', 'unidade', 'quantidade', 'grupo')
    search_fields = ['id', 'descricao']
    list_display_links = ('id', 'descricao')
    list_filter = ('grupo', 'unidade')
    list_per_page = 8
    ordering = ('descricao',)

    @admin.display(description='Valor Total')
    def valorproduto(self, obj):
        return obj.quantidade*obj.preco_venda
    
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'ativo', 'modificado')
    search_fields = ['id', 'descricao', 'sigla']
    
    
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'ativo', 'modificado')
    search_fields = ['id', 'descricao']
 
class ItensPedidoVendaInline(admin.TabularInline):
    model = ItensPedidoVenda
    extra = 0
    fields = ['produto', 'quantidade', 'preco',
              'desconto_perc', 'detalhamento']   
    
@admin.register(PedidoVenda)
class PedidoVendaAdmin(admin.ModelAdmin):
    inlines = [ItensPedidoVendaInline]
    list_display = ('id', 'cliente', 'emissao', 'vendedor', 'qtdparcelas', 'comissao', 'dataentrega', 
                    'datacancelamento', 'observacao', 'modificado')
    fields = [('cliente', 'vendedor', 'emissao', 'qtdparcelas'),
              ('comissao', 'dataentrega', 'datacancelamento'), 
               'observacao']       
    search_fields = ['id', 'emissao']
    list_display_links = ('id', 'cliente')
    list_filter = ('cliente', 'vendedor')
    list_per_page = 8
    
@admin.register(ItensPedidoVenda)
class ItensPedidoVendaAdmin(admin.ModelAdmin):    
    list_display = ('id', 'pedido', 'produto') 
    
admin.site.site_title = 'Administração do Sistema'
admin.site.site_header = 'Administração de dados do Sistema'
admin.site.index_title = 'Administração eGCom'

