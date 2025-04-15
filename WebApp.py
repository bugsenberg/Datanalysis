from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Lê os dados
    df = pd.read_csv('cancelamentos.csv')
    df = df.drop(columns='CustomerID')
    df = df.dropna()

    # Se o método for POST, significa que o usuário fez uma escolha no formulário
    if request.method == 'POST':
        # Recupera os valores escolhidos pelo usuário para as variáveis x e color
        x_variable = request.form.get('x_variable')
        color_variable = request.form.get('color_variable')

        # Cria o gráfico baseado nas variáveis escolhidas
        grafico = px.histogram(df, x=x_variable, color=color_variable, text_auto=True)

        # Converte o gráfico para HTML
        grafico_html = pio.to_html(grafico, full_html=False)
    else:
        # Se o método for GET, apenas exibe a página sem gráfico inicial
        grafico_html = None

    # Passa as colunas para o template, para que o usuário possa escolher
    colunas = df.columns.tolist()

    return render_template('index.html', grafico=grafico_html, colunas=colunas)

if __name__ == '__main__':
    app.run(debug=True)
