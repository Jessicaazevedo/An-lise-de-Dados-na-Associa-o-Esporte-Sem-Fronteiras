# jovens/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jovens/', views.listar_jovens, name='listar_jovens'),
    path('jovens/<int:jovem_id>/', views.detalhes_jovem, name='detalhes_jovem'),
    path('grafico/', views.gerar_grafico, name='gerar_grafico'),
]
