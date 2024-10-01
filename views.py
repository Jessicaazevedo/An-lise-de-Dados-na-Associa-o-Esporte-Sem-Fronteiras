# jovens/views.py

from django.shortcuts import render
from .models import Jovem, Atividade
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def listar_jovens(request):
    jovens = Jovem.objects.all()
    return render(request, 'jovens/listar_jovens.html', {'jovens': jovens})

def detalhes_jovem(request, jovem_id):
    jovem = Jovem.objects.get(id=jovem_id)
    atividades = Atividade.objects.filter(jovem=jovem)
    return render(request, 'jovens/detalhes_jovem.html', {'jovem': jovem, 'atividades': atividades})

def gerar_grafico(request):
    jovens = Jovem.objects.all()
    nomes = [jovem.nome for jovem in jovens]
    desempenhos = [jovem.desempenho for jovem in jovens]

    plt.bar(nomes, desempenhos)
    plt.xlabel('Jovens')
    plt.ylabel('Desempenho')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return render(request, 'jovens/grafico.html', {'imagem': imagem})
