<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>FASES RAD</th>
      <th>Ciclo</th>
      <th>Início</th>
      <th>Fim</th>
      <th>Objetivo Principal</th>
      <th>Entregas Esperadas</th>
      <th>Validação do Cliente</th>
    </tr>
  </thead>
  <tbody>
    <!-- Levantamento dos Requisitos -->
    <tr>
      <td rowspan="2">Levantamento dos Requisitos</td>
      <td>Ciclo 1</td>
      <td>22/04/25</td>
      <td>04/05/25</td>
      <td>Levantamento dos Requisitos</td>
      <td>
        - Documento com requisitos definidos
      </td>
      <td>Revisão e validação dos requisitos por videochamada</td>
    </tr>
    <tr>
      <td>Ciclo 2</td>
      <td>05/05/25</td>
      <td>24/05/25</td>
      <td>Definição e Priorização do Backlog</td>
      <td>
        - Documento com o backlog definido<br>
        - Priorização dos itens do backlog com MoSCoW
      </td>
      <td>Revisão do documento de backlog</td>
    </tr>
    <!-- User Design + Construção + Teste -->
    <tr>
      <td rowspan="10">User Design +<br>Construção + Teste</td>
      <td>Ciclo 3</td>
      <td>25/05/25</td>
      <td>03/06/25</td>
      <td>Catálogo dos produtos</td>
      <td>
        - Visualizar catálogo de produtos<br>
        - Visualizar descrição do produto
      </td>
      <td>Validação da interface inicial e do detalhamento dos produtos</td>
    </tr>
    <tr>
      <td>Ciclo 4</td>
      <td>04/06/25</td>
      <td>13/06/25</td>
      <td>Pedidos e pagamento através da plataforma</td>
      <td>
        - Ver o resumo da compra<br>
        - Selecionar meio de pagamento<br>
        - Integração com sistema de pagamento externo<br>
        - Visualizar situação do pedido (usuário)
      </td>
      <td>Validação do fluxo de pedidos e pagamentos</td>
    </tr>
    <tr>
      <td>Ciclo 5</td>
      <td>14/06/25</td>
      <td>23/06/25</td>
      <td>Interface do administrador</td>
      <td>
        - Gerenciamento de catálogo<br>
        - Gerenciamento de estoque<br>
        - Atualização automática do estoque<br>
        - Gerenciamento de situação dos pedidos
      </td>
      <td>Validação dos sistemas de gerenciamento de catálogo, estoque e pedidos pelo administrador</td>
    </tr>
    <tr>
      <td>Ciclo 6</td>
      <td>24/06/25</td>
      <td>03/07/25</td>
      <td>Troca/devolução de pedidos</td>
      <td>
        - Sistema de solicitação (e confirmação) de troca/devolução de produtos
      </td>
      <td>Validação do sistema de solicitação de troca/devolução</td>
    </tr>
    <tr>
      <td>Ciclo 7</td>
      <td>04/07/25</td>
      <td>13/07/25</td>
      <td>Lançamento do MVP e Monitoramento</td>
      <td>
        - Lançamento parcial do sistema para todos os usuários<br>
        - Monitoramento pós-lançamento e ajustes com base nos primeiros feedbacks
      </td>
      <td>
        Homologação pela cliente e aprovação do MVP.<br>
        Feedback dos primeiros usuários reais e ajustes pós-lançamento do MVP.
      </td>
    </tr>
    <tr>
      <td>Ciclo 8</td>
      <td>14/07/25</td>
      <td>23/07/25</td>
      <td>Notificação de compra realizada</td>
      <td>
        - Notificação de compra ao usuário<br>
        - Notificação de compra ao administrador
      </td>
      <td>Validação da funcionalidade de notificações</td>
    </tr>
    <tr>
      <td>Ciclo 9</td>
      <td>24/07/25</td>
      <td>02/08/25</td>
      <td>Personalização de produto</td>
      <td>- Personalização de produtos</td>
      <td>Validação do mecanismo de personalização de produto</td>
    </tr>
    <tr>
      <td>Ciclo 10</td>
      <td>03/08/25</td>
      <td>12/08/25</td>
      <td>Autenticação, carrinho</td>
      <td>
        - Implementação de sistema de autenticação de usuários<br>
        - Funcionalidade de carrinho de compras
      </td>
      <td>Validação do sistema de autenticação e carrinho de compras</td>
    </tr>
    <tr>
      <td>Ciclo 11</td>
      <td>13/08/25</td>
      <td>22/08/25</td>
      <td>Avaliação de produtos</td>
      <td>- Sistema de avaliação de produtos pelos usuários</td>
      <td>Validação do sistema de avaliações de produtos</td>
    </tr>
    <tr>
      <td>Ciclo 12</td>
      <td>23/08/25</td>
      <td>01/09/25</td>
      <td>Desconto em compras por divulgação da plataforma</td>
      <td>- Implementação de sistema de descontos para usuários que divulgarem a plataforma</td>
      <td>Validação do sistema de descontos por divulgação</td>
    </tr>
    <!-- Entrega Final -->
    <tr>
      <td>Entrega</td>
      <td>Ciclo 13</td>
      <td>02/09/25</td>
      <td>11/09/25</td>
      <td>Entrega Final</td>
      <td>- Lançamento final do sistema, para todos os usuários</td>
      <td>
        Homologação pela cliente e aprovação final.<br>
        Feedback dos primeiros usuários reais e ajustes pós-lançamento final.
      </td>
    </tr>
  </tbody>
</table>



**Considerações importantes:**

1. **Datas de início e fim:** Cada ciclo tem a duração de 9 dias, começando em 22/04/25 e finalizando em 24/08/25, distribuindo as entregas parciais ao longo do tempo, com exceção do ciclo 4, que, devido a uma quantidade maior de funcionalidades a serem desenvolvidas, possui 20 dias de duração (1 semana a mais).

2. **Etapas da metodologia RAD a cada ciclo:** Inicialmente, será realizada a etapa de **levantamento de requisitos**, em conjunto com a cliente. Em seguida, ocorrerá o **User Design** (prototipação), com foco na validação das necessidades e ajustes baseados em feedbacks. Em cada ciclo de entrega, serão realizadas a **construção** rápida e incremental de cada User Story, seguida de **testes** frequentes para validação e, posteriormente, a entrega das funcionalidades ao cliente. No último ciclo (cutover), será realizada a implantação completa do sistema.

3. **Ciclos:** O RAD é centrado na iteratividade, prototipação rápida, feedback constante dos usuários e ajustes contínuos, e o nosso ciclo ilustrado na figura 2 segue a seguinte lógica:

    >a. **Levantamento de Requisitos** - Corresponde à fase em que são resgatadas as necessidades dos stakeholders e traduzidas para implementações de software a fim de identificar e resolver problemas.
    >
    >b. **User Design + Construção + Teste** - User Design, Construção e Teste no RAD consistem em um ciclo integrado onde as necessidades do usuário são continuamente entendidas e refinadas por meio de protótipos funcionais, o desenvolvimento e a codificação dos componentes são realizados de forma rápida, e o produto é validado frequentemente com testes para identificar e corrigir falhas, garantindo ajustes constantes baseados no feedback dos usuários.
    >
    >c. **Entrega** - Diz respeito à fase em que todas as funcionalidades do software desenvolvido são entregues e prontas para uso.
    >



A sequência circular a sugere um **processo iterativo**:

![Ciclos do processo RAD](../assets/Ciclos.png)
 <center><strong>Figura 2:</strong> Ciclos do processo RAD</center>

