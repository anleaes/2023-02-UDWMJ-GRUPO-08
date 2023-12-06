from django.urls import path
from . import views

app_name = 'inventories'

urlpatterns = [
    path('', views.list_inventories, name='list_inventories'),
    path('adicionar/<int:id_player>/', views.add_inventory, name='add_inventory'),
    path('excluir/<int:id_inventory>/', views.delete_inventory, name='delete_inventory'),
    path('excluir-item/<int:id_inventory_item>/', views.delete_inventory_item, name='delete_inventory_item'),
    path('adicionar-item/<int:id_inventory>/', views.add_inventory_item, name='add_inventory_item'),
    path('editar-status/<int:id_inventory>/', views.edit_inventory_status, name='edit_inventory_status'),
]
