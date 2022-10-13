from django.contrib import admin
from .models import Cargo, Cliente, PedidoVenda, Produto, Vendedor, Contato, Municipio, Uf
from .models import Unidade, Grupo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fantasia', 'cpf', 'cnpj', 'logradouro', 'num', 'compl', 'bairro',
                    'municipio', 'cep', 'uf', 'insc_estadual', 'insc_municipal', 'ativo', 
                    'vendedor', 'email', 'email_nf', 'modificado')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'email','cod_area_fone', 'fone', 'cod_area_celular', 
                    'celular', 'facebook', 'twitter', 'instagram', 'ativo', 'modificado')
 
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'logradouro', 'num', 'compl', 'bairro', 'municipio', 
                    'cep', 'uf', 'email', 'cod_area_celular_1', 'celular_1', 
                    'cod_area_celular_2', 'celular_2', 'ativo', 'modificado')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cmun', 'uf', 'siaf', 'ativo', 'modificado')
    
@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'codmun', 'maskfone', 'aliq_mva', 'carga_liq', 
                    'carga_imp', 'carga_simples','tempo_carrego', 'tempo_entrega', 'ativo', 'modificado')
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'compl', 'unidade', 'grupo', 'quantidade', 
                    'preco_custo', 'preco_venda', 'observacao', 'ativo', 'modificado')
    
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'ativo', 'modificado')
    
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ativo', 'modificado')
    
@admin.register(PedidoVenda)
class PedidoVendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vendedor', 'qtdparcelas', 'comissao', 'dataentrega', 
                    'datacancelamento', 'observacao', 'ativo', 'modificado')

admin.site.site_title = 'Administração do Sistema'
admin.site.site_header = 'Administração de dados do Sistema'
admin.site.index_title = 'Administração de dados'

