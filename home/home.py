import streamlit as st
from streamlit.components.v1 import html

# Configuração opcional da página
st.set_page_config(page_title="Quem Somos", layout="centered")

# Substitua as URLs das imagens abaixo por links reais ou utilize base64 se precisar exibir imagens locais.
html_content = """
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {
      margin: 0; 
      padding: 0; 
      font-family: Arial, sans-serif;
      background-color: #F5F5F5;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
      background-color: #ffffff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      color: #003366;
      margin-bottom: 1.5rem;
    }
    p {
      text-align: justify;
      line-height: 1.6;
      margin-bottom: 1rem;
      color: #333333;
    }
    /* Seção com duas imagens lado a lado */
    .flex-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      margin-top: 2rem;
    }
    .card {
      flex: 1 1 300px;
      max-width: 400px;
      background-color: #ffffff;
      padding: 1rem;
      border-radius: 8px;
      box-shadow: 0 0 5px rgba(0,0,0,0.05);
    }
    .card img {
      width: 100%;
      height: auto;
      border-radius: 8px;
    }
    .card h3 {
      text-align: center;
      margin-top: 1rem;
      color: #003366;
    }
    .card p {
      text-align: justify;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Quem Somos</h1>
    
    <p>
      A <strong>Ativa Engenharia</strong> tem a missão de ser vista como a melhor escolha 
      para os clientes que buscam atender suas necessidades com serviços de qualidade. 
      Sob a perspectiva de um mercado em contínua mudança, nossa empresa busca alinhar 
      preço justo e qualidade, mantendo um ajuste viável entre os objetivos do cliente 
      e um serviço de excelência.
    </p>
    <p>
      Além de atender às suas exigências em ocorrências corretivas, trabalhamos sempre 
      com uma visão preventiva, buscando minimizar danos e agregar resultados em conjunto 
      aos nossos clientes e parceiros. Nosso diferencial se expressa na dinâmica na 
      prestação de nossos serviços, que podem ser prestados diretamente ao cliente final 
      ou em parceria com outros fornecedores e outros segmentos da área.
    </p>
    <p>
      Nosso principal objetivo é fornecer soluções integradas em diversas áreas da Engenharia. 
      Para tanto, contamos com corpo técnico qualificado em vários segmentos da engenharia. 
      Atualmente, nossa companhia vem se destacando no cenário estadual ao perseguir valores 
      de confiabilidade, qualidade e segurança nos serviços prestados. 
    </p>
    
    <!-- Seção com duas imagens lado a lado -->
    <div class="flex-container">
      <!-- Card 1 -->
      <div class="card">
        <img src="https://via.placeholder.com/400" alt="Imagem 1" />
        <h3>Profissionais Altamente Qualificados</h3>
        <p>
          Nosso corpo técnico conta com especialistas no segmento de engenharia 
          industrial mecânica, elétrica, clínica, segurança do trabalho e climatização.
        </p>
      </div>
      <!-- Card 2 -->
      <div class="card">
        <img src="https://via.placeholder.com/400" alt="Imagem 2" />
        <h3>Solicite Um Orçamento</h3>
        <p>
          Tenha sempre a garantia de serviços de qualidade, documentação certificada 
          e preço justo. Entre em contato para saber mais sobre nossas soluções 
          e solicitar seu orçamento.
        </p>
      </div>
    </div>
  </div>
</body>
</html>
"""

# Renderiza o HTML em um iframe, definindo altura e permitindo rolagem
html(
    html_content,
    width=900,     # Ajuste a largura desejada
    height=1200,   # Ajuste a altura do iframe
    scrolling=True
)
