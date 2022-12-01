from django.urls import path
from django.contrib import admin
from core.views import CreateProdutoView, UpdateProdutoView, DeleteProdutoView, ListProdutoView, UserLogoutView
from core.views import index
from .views import CreatePedidoVendaView, UpdatePedidoVendaView, DeletePedidoVendaView, ListPedidoVendaView, print_rel, vtreino
from .views import CreateClienteView, UpdateClienteView, DeleteClienteView, ListClienteView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    
    path('listtreino/', vtreino.as_view(), name='list_treino'),
     path('printrel/', print_rel, name='print_rel'),
    
    path('listprod/', ListProdutoView.as_view(), name='list_produto'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
    
    path('listpedven/', ListPedidoVendaView.as_view(), name='list_pedido_venda'),
    path('addpedven/', CreatePedidoVendaView.as_view(), name='add_pedido_venda'),
    path('<int:pk>/updatepedven/', UpdatePedidoVendaView.as_view(), name='upd_pedido_venda'),
    path('<int:pk>/deletepedven/', DeletePedidoVendaView.as_view(), name='del_pedido_venda'),
    
    path('listcli/', ListClienteView.as_view(), name='list_cliente'),
    path('addcli/', CreateClienteView.as_view(), name='add_cliente'),
    path('<int:pk>/updatecli/', UpdateClienteView.as_view(), name='upd_cliente'),
    path('<int:pk>/deletecli/', DeleteClienteView.as_view(), name='del_cliente'),
    
    path('logout/', UserLogoutView.as_view(), name='logoutview'),  
]