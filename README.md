**Projeto: Sistema de Análise de Dados para Associação Esporte Sem Fronteiras**


Este projeto é uma aplicação web desenvolvida com Django que permite o gerenciamento de dados dos jovens participantes da Associação Esporte Sem Fronteiras, como o registro de atividades e o acompanhamento de desempenho. Além disso, o sistema gera gráficos de desempenho usando a biblioteca Matplotlib.


**Funcionalidades**

**Cadastro de Jovens:** Gerencia o cadastro dos jovens participantes da ONG.
Registro de Atividades: Cada jovem pode ter várias atividades registradas, com notas de desempenho.

**Visualização de Desempenho:** Exibe gráficos de barras com o desempenho dos jovens.

**Painel de Administração:** Inclui um painel administrativo para gerenciar os dados.
Requisitos

**Antes de executar o projeto, certifique-se de ter os seguintes softwares instalados em sua máquina:**

Python 3.x

Django 4.x

Pip

Matplotlib (para gráficos)

-------------------------------

**Instalação e Execução
Siga os passos abaixo para executar o projeto localmente:**

1. Clone o repositório
Clone o repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


2. Crie e ative um ambiente virtual
Crie um ambiente virtual para o projeto:

bash
Copiar código
python3 -m venv venv
Ative o ambiente virtual:

Linux/macOS:
bash
Copiar código
source venv/bin/activate
Windows:
bash
Copiar código
venv\Scripts\activate


3. Instale as dependências
Instale as dependências listadas no arquivo requirements.txt (ou instale manualmente as bibliotecas):

bash
Copiar código
pip install django matplotlib


4. Configure o banco de dados
Antes de executar o projeto, é necessário configurar o banco de dados. Este projeto utiliza o banco de dados SQLite por padrão, que já está configurado. Caso prefira outro banco de dados, como PostgreSQL, modifique o arquivo settings.py na seção DATABASES.

**Crie as migrações e aplique-as ao banco de dados:**

bash
Copiar código
python manage.py makemigrations
python manage.py migrate


5. Crie um superusuário
Para acessar o painel administrativo, crie um superusuário:

bash
Copiar código
python manage.py createsuperuser
Siga as instruções para definir nome de usuário, email e senha.


6. Execute o servidor de desenvolvimento
Execute o servidor Django localmente:

bash
Copiar código
python manage.py runserver
Agora, você pode acessar a aplicação no navegador em http://127.0.0.1:8000/.


7. Acesse o painel administrativo
Para gerenciar os dados dos jovens e atividades, acesse o painel administrativo em http://127.0.0.1:8000/admin e faça login com o superusuário que você criou.

Estrutura do Código
A seguir está a explicação de como o código está organizado:

models.py

------------------------

**Define dois modelos principais:**

**Jovem:** Armazena informações sobre os jovens, como nome, idade, escolaridade e desempenho.

**Atividade:** Registra as atividades realizadas pelos jovens, com descrição, data e nota.
views.py

**Contém as funções que renderizam as páginas e processam os dados:**


**listar_jovens:** Exibe a lista de todos os jovens cadastrados.

**detalhes_jovem:** Mostra os detalhes e as atividades de um jovem específico.

**gerar_grafico:** Gera um gráfico de barras usando Matplotlib para exibir o desempenho dos jovens.
urls.py


**Define as rotas da aplicação:**

/jovens/: Exibe a lista de jovens.
/jovens/<id>/: 

- Exibe os detalhes de um jovem específico.

/grafico/: 
- Gera e exibe o gráfico de desempenho.

*Templates HTML*

listar_jovens.html:
- Template que exibe a lista de jovens.
detalhes_jovem.html: 
- Template que exibe os detalhes de um jovem e suas atividades.
grafico.html: 
- Template que exibe o gráfico gerado.
Exemplos de Uso
Listar Jovens: Acesse http://127.0.0.1:8000/jovens/ para ver a lista de todos os jovens registrados no sistema.


Visualizar Atividades: Clique no nome de um jovem para visualizar suas atividades e detalhes.
Gerar Gráfico: Acesse http://127.0.0.1:8000/grafico/ para visualizar o gráfico de desempenho dos jovens.

-----------------------------------------------

Tecnologias Usadas
Django: Framework web Python usado para desenvolver a aplicação.
SQLite: Banco de dados padrão usado no projeto, fácil de configurar.
Matplotlib: Biblioteca Python usada para gerar gráficos.
