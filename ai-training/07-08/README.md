<h1>ChatBox local com llama3</h1>

<p align="justify">Este projeto consiste em uma interface simples e funcional construída com <code>Streamlit</code> que permite a interação com um modelo de linguagem da família <code>llama3</code>, hospedado localmente via API. O objetivo principal é proporcionar uma introdução prática à automação com <b>Inteligência Artificial</b>, com foco em capacitação técnica e exploração de tecnologias modernas voltadas para processamento de <b>linguagem natural (NLP)</b>.</p>

<hr>

<h2>Tecnologias utilizadas</h2>
<ul>
    <li><strong>Pytohn v3.11</strong>;</li>
    <br>
    <li><strong>Streamlit</strong>: para construção de interfaces web;</li>
    <br>
    <li><strong>Request</strong>: para consumo de API local;</li>
    <br>
    <li><strong>llama3:8B</strong>: modelo de linguagem de código aberto, executado via servidor local.</li>
    <br>
</ul>

<hr>

<h2>Estrutura do projeto</h2>

<pre>
07-08/
└── app.py    # script principal da aplicação (interface via Streamlit + consumo da API (llama3))
</pre>

<hr>

<h2>Funcionalidades</h2>
<img src="./img/demonstration.gif" alt="imagem animada demonstrando as funcionalidades da aplicação"/>
<ul>
  <li>Interface simples e intuitiva para digitar perguntas e receber respostas.</li>
  <li>Seleção de modelos disponíveis (atualmente limitado ao llama3:8b).</li>
  <li>Histórico de conversas mantido em sessão para contexto.</li>
  <li>Botão de limpeza de histórico.</li>
  <li>Sistema de alerta caso o campo de entrada esteja vazio.</li>
</ul>

<hr>

<h2>Como rodar esse projeto em seu ambiente</h2>

<h3>Pré-requisitos:</h3>
<ul>
  <li>
    <b>Python v3.11</b> ou superior
    <br>Caso não possua, acesse: 
    <a href="https://www.python.org/downloads/release/python-3110/" target="_blank">www.python.org/downloads/release/python-3110/</a> e instale
    <br>Para verificar a instalação, use o comando:
    <pre><code>python --version</code></pre>
  </li>
  <li>
    <b>pip</b> (gerenciador de pacotes do Python)
  </li>
  <li>
    <b>Ollama</b> instalado e rodando (para execução local do modelo Llama3)
    <ol>
      <li>
        Baixe e instale o <b>Ollama</b>:
        <br>Acesse: 
        <a href="https://ollama.com/download" target="_blank">ollama.com/download</a> e siga as instruções para o seu sistema operacional.
        <br>Para verificar a instalação, use o comando:
        <pre><code>ollama --version</code></pre>
      </li>
      <li>
        Baixe o modelo <b>llama3:8b</b>:
        <br>No terminal, execute:
        <pre><code>ollama pull llama3:8b</code></pre>
        Para confirmar que o modelo foi baixado, use:
        <pre><code>ollama list</code></pre>
      </li>
    </ol>
  </li>
  <li>
    <b>Git</b> instalado
    <br>Caso não possua, acesse: 
    <a href="https://git-scm.com/downloads" target="_blank">git-scm.com/downloads</a> e instale
    <br>Para verificar a instalação, use o comando:
    <pre><code>git --version</code></pre>
  </li>
  <li>
    Navegador moderno (Chrome, Firefox, Edge, etc.)
  </li>
</ul>

<h3>Passo a Passo:</h3>
<ol>
  <li>
    Baixe os arquivos do projeto:
    <br>Acesse diretamente o diretório do projeto no GitHub:
    <pre><code>https://github.com/MatheusVenturaNellessen/data-science-training/tree/main/ai-training/07-08</code></pre>
    Clique em <b>“Code” → “Download ZIP”</b>, extraia o conteúdo e acesse a pasta <code>07-08</code> no terminal:
    <pre><code>cd caminho/para/pasta/07-08</code></pre>
  </li>
  <li>
    Instale as dependências:
    <pre><code>pip install streamlit ollama</code></pre>
  </li>
  <li>
    Certifique-se de que o Ollama está rodando com o modelo:
    <pre><code>ollama run llama3:8b</code></pre>
    Isso manterá o modelo carregado e acessível localmente em: <b>http://localhost:11434</b>
  </li>
  <li>
    Execute a aplicação <b>Streamlit</b>:
    <pre><code>streamlit run app.py</code></pre>
    O navegador será aberto automaticamente. Caso não, acesse manualmente:
    <pre><code>http://localhost:8501</code></pre>
  </li>
</ol>

<hr>

<h2>Contribuições</h2>
<p align="justify">Este projeto está aberto para contribuições via <i>issues</i>. Se você encontrou um <i>bug</i>, deseja sugerir uma melhoria ou tem dúvidas sobre o funcionamento, siga as instruções abaixo:</p>
<ol>
    <li>Verifique se já existe uma <i>issue</i> sobre o assunto. Caso sim, adicione um comentário nela.</li>
    <li>Se não houver, abra uma nova <i>issue</i> com uma descrição clara e objetiva.</li>
</ol>

<hr>

<h2>Licença e Autoria</h2>
<p align="justify">Este projeto foi desenvolvido por <a href="https://github.com/MatheusVenturaNellessen">Matheus Ventura Nellessen</a> e está licenciado sob a licença MIT. Veja o <a href="../../LICENSE">documento</a> para mais detalhes.</p>
