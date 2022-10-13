from distutils.command.upload import upload
from email.policy import default
from random import choices
from tabnanny import verbose
from turtle import width
from unittest.util import _MAX_LENGTH
from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True
          
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo          
            
class Contato(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.PROTECT)
    email = models.EmailField('Email', max_length=200, blank=True, null=True)
    cod_area_fone = models.CharField('Cód.área', max_length=2, blank=True, null=True)
    fone = models.CharField('Fone', max_length=9, blank=True, null=True)    
    cod_area_celular = models.CharField('Cód.área', max_length=2, blank=True, null=True)
    celular = models.CharField('Celular', max_length=9, blank=True, null=True)       
    facebook = models.CharField('Facebook', max_length=100, blank=True, null=True)
    twitter = models.CharField('Twitter', max_length=100, blank=True)
    instagram = models.CharField('Instagram', max_length=100, blank=True, null=True)
    obs = models.CharField('Observação', max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    def __str__(self):
        return self.nome    
  
class Cliente(Base):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    nome = models.CharField('Nome', max_length=100)
    fantasia = models.CharField('Fantasia', max_length=60, blank=True)
    contato = models.ForeignKey('core.Contato', verbose_name='Contato', on_delete=models.PROTECT, blank=True, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    logradouro = models.CharField('Endereço', max_length=100, blank=True)
    num = models.CharField('Nro', max_length=10, blank=True)
    compl = models.CharField('Complemento', max_length=40, blank=True)
    bairro = models.CharField('Bairro', max_length=60)
    municipio = models.ForeignKey('core.Municipio', verbose_name='Município', on_delete=models.PROTECT)
    cep = models.CharField('CEP', max_length=8)
    uf = models.ForeignKey('Uf', verbose_name='UF', on_delete=models.PROTECT)
    cpf = models.CharField('CPF', max_length=11, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14, blank=True)
    insc_estadual = models.CharField('Inscrição estadual', max_length=14, blank=True)
    insc_municipal = models.CharField('Inscrição municipal', max_length=14, blank=True)
    vendedor = models.ForeignKey('core.Vendedor', verbose_name='Vendedor', on_delete=models.PROTECT, blank=True)
    email = models.EmailField('Email', max_length=200, blank = True)
    email_nf = models.EmailField('Email NF', max_length=200, blank = True)
    cod_area_celular_1 = models.CharField('Cód.área', max_length=2, blank=True)
    celular_1 = models.CharField('Celular', max_length=9, blank=True)
    cod_area_celular_1 = models.CharField('Cód.área', max_length=2, blank=True) 
    celular_1 = models.CharField('Celular', max_length=9, blank=True)
    cod_area_celular_1 = models.CharField('Cód.área', max_length=2, blank=True)
    celular_1 = models.CharField('Celular', max_length=9, blank=True)
    credito_limite = models.DecimalField('Limite de crédito', max_digits=12, decimal_places=2, blank=True)
    observacao = models.TextField('Observação', max_length=2000, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return self.nome  
  
class Municipio(Base):
    nome = models.CharField('Nome do Município', max_length=60)
    cmun = models.CharField('Cód.Município', max_length=7)
    uf = models.ForeignKey('core.Uf', verbose_name='UF', on_delete=models.CASCADE)
    siaf = models.CharField('C.Siaf', max_length=10, blank=True)
    
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        
    def __str__(self):
        return self.nome
    
class Uf(Base):
    nome = models.CharField('Nome da UF', max_length=60)
    sigla = models.CharField('Sigla', max_length=2)
    codmun = models.IntegerField("Código")
    maskfone = models.CharField('Formato fone', max_length=20, blank=True)
    aliq_mva = models.DecimalField('Alíquota MVA', max_digits=12, decimal_places=2, blank=True)
    carga_liq = models.DecimalField('Carga líquida', max_digits=12, decimal_places=2, blank=True)
    carga_imp = models.DecimalField('Carga imposto', max_digits=12, decimal_places=2, blank=True)
    carga_simples = models.DecimalField('Carga simples', max_digits=12, decimal_places=2, blank=True)
    tempo_carrego = models.IntegerField("Tempo de carrego", blank=True)
    tempo_entrega = models.IntegerField("Tempo de entrega", blank=True)
    
    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UFs'
        
    def __str__(self):
        return self.nome
    
class Vendedor(Base):
    nome = models.CharField('Nome', max_length=100)
    logradouro = models.CharField('Endereço', max_length=100)
    num = models.CharField('Nro', max_length=10)
    compl = models.CharField('Complemento', max_length=40, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=60, blank=True)
    municipio = models.ForeignKey('core.Municipio', verbose_name='Município', on_delete=models.PROTECT, blank=True)
    cep = models.CharField('CEP', max_length=8, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)
    perc_comissao = models.DecimalField('% Comissão', max_digits=8, decimal_places=2, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=11, blank = True, null=True)
    email = models.EmailField('Email', max_length=200, blank = True, null=True)
    cod_area_celular_1 = models.CharField('Cód.área', max_length=2, blank=True, null=True)
    celular_1 = models.CharField('Celular', max_length=9, blank=True, null=True)
    cod_area_celular_2 = models.CharField('Cód.área', max_length=2, blank=True, null=True)
    celular_2 = models.CharField('Celular', max_length=9, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedors'
        
    def __str__(self):
        return self.nome
    
class Produto(Base):
    descricao = models.CharField('Nome', max_length=100)
    compl = models.CharField('Complemento', max_length=60, blank=True)
    unidade = models.ForeignKey('core.Unidade', verbose_name='Unidade', on_delete=models.PROTECT, blank=True, null=False)
    grupo = models.ForeignKey('core.Grupo', verbose_name='Grupo', on_delete=models.PROTECT, blank=True, null=False)
    quantidade = models.DecimalField('Quantidade', max_digits=12, decimal_places=2, blank=True, default=None)
    preco_custo = models.DecimalField('Preço de custo', max_digits=12, decimal_places=2, blank=True, default=None)
    preco_venda = models.DecimalField('Preço de venda', max_digits=12, decimal_places=2, blank=True, default=None)
    observacao = models.TextField('Observação', max_length=2000, blank=True, null=True, default=None)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return self.descricao
    
class Unidade(Base):
    descricao = models.CharField('Descrição', max_length=60)
    sigla = models.CharField('Sigla', max_length=5)
    
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        
    def __str__(self):
        return self.descricao  
    
class Grupo(Base):
    descricao = models.CharField('Descrição', max_length=60)
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        
    def __str__(self):
        return self.descricao
    
class PedidoVenda(Base):
    cliente = models.ForeignKey('core.Cliente', null=True, blank=True, on_delete=models.PROTECT)
    qtdparcelas = models.IntegerField("Quant.parcelas")
    comissao = models.DecimalField('Percentual comissão', max_digits=12, decimal_places=2, blank=True, default=None)
    vendedor = models.ForeignKey('core.Vendedor', verbose_name='Vendedor', on_delete=models.PROTECT, blank=True, null=False)
    dataentrega = models.DateTimeField('Data da entrega', null=True)
    datacancelamento = models.DateTimeField('Data de cancelamento', null=True)
    observacao = models.TextField('Observação', max_length=2000, blank=True, null=True, default=None)
    
    class Meta:
        verbose_name = 'Pedido de Venda'
        verbose_name_plural = 'Pedidos de Venda'
        
    def __str__(self):
        return self.cliente
    
class ItensPedidoVenda(Base):
    pedido = models.ForeignKey('core.PedidoVenda', on_delete=models.CASCADE, related_name='PedidoVenda')
    prduto = models.ForeignKey('core.Produto', on_delete=models.CASCADE, related_name='PedidoVenda')
    quantidade = models.DecimalField('Quantidade', max_digits=12, decimal_places=2, blank=True, default=None)
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2, blank=True, default=None)
    desconto_perc = models.DecimalField('Percentual de desconto', max_digits=12, decimal_places=2, blank=True, default=None)
    detalhamento = models.TextField('Detalhes/Obs', max_length=2000, blank=True, null=True, default=None)
    
    class Meta:
        verbose_name = 'Item de Pedido de Venda'
        verbose_name_plural = 'Itens de Pedido de Venda'
        
    def __str__(self):
        return self.pedido