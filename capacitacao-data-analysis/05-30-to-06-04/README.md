<h2>Propósito do projeto</h2>

<p>Foi desenvolido um sistema destinado a gerenciar todas as operações de uma academia de forma integrada, apoiado em um banco de dados <code>SQLite</code> e uma interface web construída com <code>Streamlit</code>. Nele, são definidos seis módulos principais de dados – clientes, instrutores, planos, exercícios, treinos e pagamentos – com tabelas que incluem campos como nome, email, especialidade, preço mensal, série e repetição, data de pagamento e status de quitação.</p>

<p>O fluxo de trabalho envolve:</p>

<ol>
	<li>
		<strong>Criação e população do banco</strong>
		<ul>
		<li>Gerar o esquema <code>SQLite</code> conforme especificado e importar registros iniciais a partir de arquivos <code>CSV</code>.</li>
		</ul>
	</li>
	<li>
		<strong>Visualização e análise</strong>
		<ul>
		<li>Listar clientes e seus planos;</li>
		<li>Filtrar treinos e exibir detalhes de cada rotina;</li>
		<li>Exibir, por cliente, o total de valores pagos e a data do último pagamento;</li>
		<li>Mostrar quantos alunos cada instrutor atende, facilitando o balanceamento de carga.</li>
		</ul>
	</li>
	<li>
		<strong>Formulários interativos</strong>
		<ul>
		<li>Cadastrar novos clientes, pagamentos e treinos, e inserir exercícios nos treinos diretamente pela interface.</li>
		</ul>
	</li>
	<li>
		<strong>Extra (autenticação)</strong>
		<ul>
		<li>Implementar, opcionalmente, um sistema de login e senha usando os recursos de autenticação nativos do <code>Streamlit</code>.</li>
		</ul>
	</li>
</ol>

<p>O projeto encontra-se em outro repositório, clique <a href="https://github.com/HeitorDalla/gym-system">aqui</a> para visualizá-lo.</p>
