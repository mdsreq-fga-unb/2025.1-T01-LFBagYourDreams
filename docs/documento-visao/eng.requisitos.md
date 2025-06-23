### 4.1 Atividades e Técnicas de ER
**Elicitação e descoberta**

* **BrainStorm** - Serão feitas reuniões iniciais com a equipe e cliente para levantar o máximo de ideias sobre funcionalidades, diferenciais e problemas comuns em e-commerce

* **Entrevista** - Serão realizadas entrevistas rápidas com a cliente para identificar suas necessidades

* **PromptIA** - Serão utilizadas IA’s generativas para gerar hipóteses de requisitos, exemplos de fluxos e levantamentos de dúvidas, acelerando processos

* **Análise de concorrente** - Serão feitas avaliações detalhadas de e-commerces concorrentes diretos ou líderes de mercado para identificar padrões, recursos e lacunas.

* **Análise de tarefas** - Serão analisadas as tarefas realizadas pelo cliente no cotidiano de seu negócio para a compreensão de requisitos do produto.

**Análise e Consenso**

* **Negociação** - As funcionalidades do software serão negociadas com a cliente, tendo em vista o equilíbrio entre os desejos da mesma e as possibilidades de desenvolvimento pela equipe, mas sempre de modo a garantir o atendimento às necessidades que podem ser resolvidas pelo sistema.

* **Análise de Custo / Benefício** - Para a definição de requisitos, a equipe realizará análises de quais requisitos, de diferentes complexidades de implementação, podem satisfazer uma mesma necessidade, a fim de estabelecer uma opção viável para o desenvolvimento pela equipe.

**Declaração de Requisitos**

* **Prompt IA** - Serão utilizadas IA’s generativas como auxílio na geração de textos de requisitos, como resumos de funcionalidades, user stories ou regras de negócio.

* **Documento de Visão de Produto** - Todo o contexto que envolve a declaração de requisitos estará descrito no Documento de Visão do Produto.

* **Histórias de usuário** - Serão elaboradas descrições simples e curtas das funcionalidades desejadas, a partir da perspectiva do usuário acerca do valor de negócio.

* **Épicos** - Serão identificadas histórias grandes, os épicos, que não cabem dentro de um ciclo e podem ser repartidas em histórias menores.

* **Temas** - Serão realizados agrupamentos de histórias de usuário, para declarar grandes funcionalidades desejadas.


**Representação de Requisitos**

* **Protótipos** - Com a prototipação interativa, a equipe irá criar versões iniciais do software, permitindo ao cliente uma visualização da solução e fornecer feedback rapidamente.  

* **Diagramas** - Envolve a criação de diagramas que apoiam, de forma visual, a entender o direcionamento e o entendimento dos requisitos.


**Verificação e Validação**

* **Revisão e Feedback de validação**- Por meio de reuniões de feedback com o cliente, a equipe valida as escolhas de design, garantindo que elas atendam às necessidades e expectativas do cliente.

* **Teste Usabilidade**- Realizaremos teste de interface onde a equipe identificará áreas problemáticas na interface.


**Organização e Atualização de Requisitos**

* **Organização e Atualização**:  Usando técnicas como a priorização baseada em valor, grooming, a equipe garante que o backlog seja organizado,atualizado e alinhado com as prioridades.

* **MoSCoW**: A equipe organizará os requisitos a partir da priorização de cada requisito com base na ferramenta MoSCoW (Must have, Should have, Could have, Won’t have). A priorização será obtida a partir do valor de negócio (ferramenta WSJF), do valor de produto (ferramenta RICE), e do esforço relativo de desenvolvimento do requisito pela equipe. 


### 4.2 Engenharia de Requisitos e o Rapid Application Development(RAD)
<table border="5">
  <tr style="background-color:rgb(194, 194, 194); color: black;">
    <th style="vertical-align:middle;">Fases do RAD</th>
    <th style="vertical-align:middle;">Atividades de ER</th>
    <th style="vertical-align:middle;">Prática</th>
    <th style="vertical-align:middle;">Técnica</th>
    <th style="vertical-align:middle;">Resultado Esperado</th>
  </tr>

  <!-- Tema 1 -->
  <tr>
    <td rowspan="7" style="vertical-align:middle;"><strong>Levantamento dos Requisitos</strong></td>
    <td rowspan="4" style="vertical-align:middle;"><strong>Elicitação e Descoberta</strong></td>
    <td style="vertical-align:middle;">Levantamento de ideias por meio de reuniões</td>
    <td style="vertical-align:middle;"><strong>Brainstorm</strong></td>
    <td style="vertical-align:middle;">Identificação de prioridades, registro de ideias, sugestões e preocupação</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Entrevistas rápidas com a cliente para captar necessidades</td>
    <td style="vertical-align:middle;"><strong>Entrevista</strong></td>
    <td style="vertical-align:middle;">Requisitos priorizados e viáveis, com consenso entre cliente e equipe</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Análise de concorrentes do mercado</td>
    <td style="vertical-align:middle;"><strong>Análise de concorrentes</strong></td>
    <td style="vertical-align:middle;">Identificação de padrões, boas práticas e diferenciais competitivos do mercado</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Análise de tarefas do cotidiano do negócio</td>
    <td style="vertical-align:middle;"><strong>Análise de tarefas</strong></td>
    <td style="vertical-align:middle;">Identificação de oportunidades de facilitação/organização das tarefas por solução de software</td>
  </tr>
  <tr>
    <td rowspan="3" style="vertical-align:middle;"><strong>Declaração de Requisitos</strong></td>
    <td style="vertical-align:middle;">Utilização de IA generativa para criar esboços de requisitos e user stories</td>
    <td style="vertical-align:middle;"><strong>Prompt IA</strong></td>
    <td style="vertical-align:middle;">Textos preliminares de requisitos claros e organizados</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Criação de um documento que descreve a visão geral do sistema, seus objetivos e stakeholders</td>
    <td style="vertical-align:middle;"><strong>Documento de Visão de Produto</strong></td>
    <td style="vertical-align:middle;">Documento formal com visão compartilhada sobre o produto</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Listagem e organização de funcionalidades principais por módulos</td>
    <td style="vertical-align:middle;"><strong>Features</strong></td>
    <td style="vertical-align:middle;">Lista funcional organizada por módulos, servindo como base para desenvolvimento</td>
  </tr>

  <!-- Tema 2 -->
  <tr>
    <td rowspan="6" style="vertical-align:middle;"><strong>User Design</strong></td>
    <td style="vertical-align:middle;"><strong>Elicitação e Descoberta</strong></td>
    <td style="vertical-align:middle;">Realização de entrevistas com cliente</td>
    <td style="vertical-align:middle;"><strong>Entrevista </strong></td>
    <td style="vertical-align:middle;">Confirmar e alinhar expectativas</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;"><strong>Verificação e Validação</strong></td>
    <td style="vertical-align:middle;">Testes de Interface com cliente</td>
    <td style="vertical-align:middle;"><strong>Teste Usabilidade</strong></td>
    <td style="vertical-align:middle;">Identificação de áreas problemáticas na interface</td>
  </tr>
  <tr>
    <td rowspan="2" style="vertical-align:middle;"><strong>Representação de Requisitos</strong></td>
    <td style="vertical-align:middle;">Desenvolvimento de protótipos de interface para facilitar entendimento</td>
    <td style="vertical-align:middle;"><strong>Prototipagem</strong></td>
    <td style="vertical-align:middle;">Maior clareza dos requisitos e validação visual prévia</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Elaboração de diagramas (caso de uso, fluxo de dados) para representar lógica do sistema</td>
    <td style="vertical-align:middle;"><strong>Diagramas</strong></td>
    <td style="vertical-align:middle;">Representações estruturadas que ajudam na compreensão técnica dos requisitos</td>
  </tr>
  <tr>
    <td rowspan="2" style="vertical-align:middle;"><strong>Análise e Consenso</strong></td>
    <td style="vertical-align:middle;">Discussão de prioridades e viabilidade com cliente e equipe</td>
    <td style="vertical-align:middle;"><strong>Negociação </strong></td>
    <td style="vertical-align:middle;">Requisitos priorizados e viáveis, com consenso entre cliente e equipe</td>
  </tr>
  <tr>
    <td style="vertical-align:middle;">Avaliação do custo e do benefício de cada funcionalidade</td>
    <td style="vertical-align:middle;"><strong>Análise de Custo / Benefício</strong></td>
    <td style="vertical-align:middle;">Lista de funcionalidades priorizadas com base em valor e viabilidade</td>
  </tr>

  <!-- Tema 5 -->
  <tr>
    <td rowspan="1" style="vertical-align:middle;"><strong>Entrega</strong></td>
    <td rowspan="1" style="vertical-align:middle;"><strong>Verificação e Validação</strong></td>
    <td style="vertical-align:middle;">Realização de reuniões com cliente para revisar protótipos e funcionalidades entregues</td>
    <td style="vertical-align:middle;"><strong>Revisão e Feedback de validação</strong></td>
    <td style="vertical-align:middle;">Confirmação de que os requisitos foram atendidos e validação das soluções</td>
  </tr>
</table>
