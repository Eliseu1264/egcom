from django.urls import path
from django.contrib import admin

from .views import CreateProdutoView, UpdateProdutoView, DeleteProdutoView, ListProdutoView, UserLogoutView, index
from .views import CreatePedidoVendaView, UpdatePedidoVendaView, DeletePedidoVendaView, ListPedidoVendaView
#from .views import RelProd1_View

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    
    path('listprod/', ListProdutoView.as_view(), name='list_produto'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
    path('listpedven/', ListPedidoVendaView.as_view(), name='list_pedido_venda'),
    path('addpedven/', CreatePedidoVendaView.as_view(), name='add_pedido_venda'),
    path('<int:pk>/updatepedven/', UpdatePedidoVendaView.as_view(), name='upd_pedido_venda'),
    path('<int:pk>/deletepedven/', DeletePedidoVendaView.as_view(), name='del_pedido_venda'),
    path('logout/', UserLogoutView.as_view(), name='logoutview'),  
]
