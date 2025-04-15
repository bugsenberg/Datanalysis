📊 Análise de Cancelamentos com Flask
Este projeto é uma aplicação web desenvolvida com Flask para análise de dados de cancelamentos de clientes. A aplicação permite que o usuário escolha variáveis para gerar gráficos interativos utilizando a biblioteca Plotly. O objetivo é facilitar a análise visual dos dados e oferecer uma interface simples e intuitiva para interações rápidas com o conjunto de dados.

🚀 Funcionalidades
Seleção de variáveis: O usuário pode escolher quais variáveis usar para criar o gráfico, selecionando uma variável para o eixo X e outra para a cor do gráfico.

Visualização de gráficos: A aplicação gera gráficos interativos de acordo com as variáveis escolhidas pelo usuário.

Interface amigável: A página é responsiva, fácil de usar e com um layout moderno para uma melhor experiência de visualização.

🛠️ Tecnologias Utilizadas
Flask: Framework web em Python utilizado para criar a aplicação.

Plotly: Biblioteca de visualização de dados para criar gráficos interativos.

Jinja2: Motor de template utilizado pelo Flask para renderizar HTML dinâmico.

Pandas: Biblioteca Python para manipulação de dados.

HTML/CSS: Para estruturar e estilizar a página web.

⚙️ Como Rodar o Projeto Localmente
1. 🖥️ Clonar o Repositório
Primeiro, clone o repositório para sua máquina local:

bash
Copiar
Editar
git clone https://github.com/SEU_USUARIO/analise_cancelamentos.git
2. 📦 Instalar as Dependências
Dentro do diretório do projeto, crie um ambiente virtual e instale as dependências necessárias.

Criar e ativar o ambiente virtual:
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
Instalar as bibliotecas necessárias:
bash
Copiar
Editar
pip install -r requirements.txt
3. 🚀 Rodar a Aplicação
Com o ambiente configurado, você pode rodar a aplicação Flask com o seguinte comando:

bash
Copiar
Editar
python app.py
Isso iniciará o servidor local na URL: http://127.0.0.1:5000/

4. 🌐 Acessar a Aplicação
Abra seu navegador e vá até o endereço http://127.0.0.1:5000/ para visualizar a aplicação em funcionamento.

🖱️ Como Usar
Na página inicial, você verá o título "Análise de Cancelamentos".

Abaixo do título, há uma explicação sobre como selecionar as variáveis para o gráfico.

Você pode selecionar:

Variável para o eixo X: Escolha uma variável para o eixo horizontal do gráfico.

Variável para a cor: Escolha uma variável para colorir os dados no gráfico.

Após selecionar as variáveis, clique em "Gerar Gráfico".

O gráfico será gerado logo abaixo, com base nas variáveis que você escolheu.

🗂️ Estrutura de Arquivos
graphql
Copiar
Editar
/analise_cancelamentos
    ├── app.py              # Código principal da aplicação Flask
    ├── templates/
    │   └── index.html      # Template HTML que define o layout da página
    ├── static/
    │   └── style.css       # Arquivo CSS para personalização da página
    ├── cancelamentos.csv   # Arquivo CSV contendo os dados de cancelamentos
    ├── requirements.txt    # Arquivo de dependências do projeto
    └── README.md           # Este arquivo de documentação


📜 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

feito com 💻☕ por [bugsenberg]