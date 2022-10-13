# Generated by Django 4.1.1 on 2022-10-10 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('fantasia', models.CharField(blank=True, max_length=60, verbose_name='Fantasia')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('logradouro', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('num', models.CharField(blank=True, max_length=10, verbose_name='Nro')),
                ('compl', models.CharField(blank=True, max_length=40, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=60, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('cpf', models.CharField(blank=True, max_length=11, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=14, verbose_name='CNPJ')),
                ('insc_estadual', models.CharField(blank=True, max_length=14, verbose_name='Inscrição estadual')),
                ('insc_municipal', models.CharField(blank=True, max_length=14, verbose_name='Inscrição municipal')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='Email')),
                ('email_nf', models.EmailField(blank=True, max_length=200, verbose_name='Email NF')),
                ('cod_area_celular_1', models.CharField(blank=True, max_length=2, verbose_name='Cód.área')),
                ('celular_1', models.CharField(blank=True, max_length=9, verbose_name='Celular')),
                ('credito_limite', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Limite de crédito')),
                ('observacao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=60, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome do Município')),
                ('cmun', models.CharField(max_length=7, verbose_name='Cód.Município')),
                ('siaf', models.CharField(blank=True, max_length=10, verbose_name='C.Siaf')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome da UF')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
                ('codmun', models.IntegerField(verbose_name='Código')),
                ('maskfone', models.CharField(blank=True, max_length=20, verbose_name='Formato fone')),
                ('aliq_mva', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Alíquota MVA')),
                ('carga_liq', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Carga líquida')),
                ('carga_imp', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Carga imposto')),
                ('carga_simples', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Carga simples')),
                ('tempo_carrego', models.IntegerField(blank=True, verbose_name='Tempo de carrego')),
                ('tempo_entrega', models.IntegerField(blank=True, verbose_name='Tempo de entrega')),
            ],
            options={
                'verbose_name': 'UF',
                'verbose_name_plural': 'UFs',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=60, verbose_name='Descrição')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Endereço')),
                ('num', models.CharField(max_length=10, verbose_name='Nro')),
                ('compl', models.CharField(blank=True, max_length=40, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=60, verbose_name='Bairro')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('perc_comissao', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='% Comissão')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('cod_area_celular_1', models.CharField(blank=True, max_length=2, null=True, verbose_name='Cód.área')),
                ('celular_1', models.CharField(blank=True, max_length=9, null=True, verbose_name='Celular')),
                ('cod_area_celular_2', models.CharField(blank=True, max_length=2, null=True, verbose_name='Cód.área')),
                ('celular_2', models.CharField(blank=True, max_length=9, null=True, verbose_name='Celular')),
                ('municipio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.municipio', verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedors',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=100, verbose_name='Nome')),
                ('compl', models.CharField(blank=True, max_length=60, verbose_name='Complemento')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Quantidade')),
                ('preco_custo', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Preço de custo')),
                ('preco_venda', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Preço de venda')),
                ('observacao', models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='Observação')),
                ('grupo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.grupo', verbose_name='Grupo')),
                ('unidade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.unidade', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='PedidoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('qtdparcelas', models.IntegerField(verbose_name='Quant.parcelas')),
                ('comissao', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Percentual comissão')),
                ('dataentrega', models.DateTimeField(null=True, verbose_name='Data da entrega')),
                ('datacancelamento', models.DateTimeField(null=True, verbose_name='Data de cancelamento')),
                ('observacao', models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='Observação')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
                ('vendedor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.vendedor', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'Pedido de Venda',
                'verbose_name_plural': 'Pedidos de Venda',
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uf', verbose_name='UF'),
        ),
        migrations.CreateModel(
            name='ItensPedidoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Quantidade')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Preço')),
                ('desconto_perc', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=12, verbose_name='Percentual de desconto')),
                ('detalhamento', models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='Detalhes/Obs')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PedidoVenda', to='core.pedidovenda')),
                ('prduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PedidoVenda', to='core.produto')),
            ],
            options={
                'verbose_name': 'Item de Pedido de Venda',
                'verbose_name_plural': 'Itens de Pedido de Venda',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('cod_area_fone', models.CharField(blank=True, max_length=2, null=True, verbose_name='Cód.área')),
                ('fone', models.CharField(blank=True, max_length=9, null=True, verbose_name='Fone')),
                ('cod_area_celular', models.CharField(blank=True, max_length=2, null=True, verbose_name='Cód.área')),
                ('celular', models.CharField(blank=True, max_length=9, null=True, verbose_name='Celular')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('obs', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='contato',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.municipio', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.uf', verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vendedor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.vendedor', verbose_name='Vendedor'),
        ),
    ]
