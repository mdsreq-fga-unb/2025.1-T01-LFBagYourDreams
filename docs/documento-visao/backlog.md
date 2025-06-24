### 9.1 Backlog Geral

# Gestão de Clientes e Usuários

## 1.1 Épico: Cadastro e Acesso do Usuário

**US01**: Como usuário, eu quero poder cadastrar os meus dados pessoais, para que eu possa realizar compras sem ter que preencher minhas informações toda vez que realizar um pedido.

**US02**: Como usuário, eu quero fazer login no sistema com as minhas credenciais, para que eu possa acessar minha conta e todas as suas funcionalidades.

**US03**: Como usuário, eu quero poder realizar o logoff, para proteger meus dados pessoais.

**US04**: Como usuário, eu quero poder recuperar minha senha, para acessar minha conta caso eu a perca.

## 1.2 Épico: Gerenciamento de Perfil do Usuário

**US05**: Como usuário, eu quero poder editar meus dados como “e-mail” e “senha”, para manter minhas informações atualizadas.

**US06**: Como usuário, eu quero poder deletar a minha conta, para quando eu não possuir mais interesse em continuar na plataforma.

# Vendas e Experiência do Cliente

## 2.1 Épico: Processo de Compra

**US07**: Como usuário, eu gostaria de buscar por produtos, para visualizar informações específicas deles.

**US08**: Como usuário, eu gostaria de personalizar e escolher cada um dos componentes das bolsas, para garantir que a bolsa seja do jeito que eu quero.

**Regras de Negócio**:
    - Para todos os tipos de produto, poderá ser modificada apenas a **cor do material**.
    - Para bolsas, além da **cor do material**, também poderá ser personalizada a **alça**.

## 2.2 Épico: Gerenciamento do Carrinho

**US09**: Como usuário, eu quero poder adicionar itens a um carrinho de compras a partir de um catálogo de produtos, para organizar e selecionar mais de um produto na minha compra.

**US10**: Como usuário, eu quero poder editar itens de um carrinho de compras, para que esses itens reflitam corretamente o que desejo comprar.

**Critério de Aceitação**:
- O sistema deve permitir que eu altere a **cor** e a **quantidade** de um item no carrinho de compras.

**US11**: Como usuário, eu quero poder remover itens de um carrinho de compras, para que esses itens não sejam incluídos na minha próxima compra.

## 2.3 Épico: Finalização da Compra e Pagamento

**US12**: Como usuário, eu quero poder visualizar um resumo de uma compra a ser finalizada, para confirmar os itens selecionados antes de pagar.

**US13**: Como usuário, quero confirmar a compra dos produtos no carrinho, para que o pedido seja registrado no sistema e processado corretamente.

**Critérios de Aceitação**:
- O sistema deve permitir que eu informe meus dados de entrega, incluindo:
  - CPF
  - CEP
- O sistema deve oferecer opções de pagamento, permitindo que eu escolha entre:
  - Cartão de crédito/débito
  - Pix
  - Boleto bancário

**Regras de Negócio**:
- Se uma compra for finalizada com sucesso, então o **administrador deve ser notificado** com as informações da transação.

## 2.4 Épico: Engajamento e Pós-Venda

**US14**: Como usuário, eu quero receber desconto ao compartilhar o site com outras pessoas, para que eu possa obter benefícios em compras por indicar o site para meus contatos.

**US15**: Como usuário, eu quero poder adicionar avaliação de produtos que adquiri (usando estrelas e comentários), para que eu possa compartilhar minha experiência e dar meu feedback com outros clientes e com a loja.

**US16**: Como usuário, quero poder remover minha avaliação de um produto adquirido (incluindo estrelas e comentários), para que eu possa gerenciar meu feedback e controlar as informações que compartilho com outros clientes e com a loja.

**US17**: Como usuário, eu quero ser capaz de iniciar um processo de devolução ou troca de um item comprado, para que eu possa resolver problemas com produtos recebidos de forma prática e eficiente.

# Gestão Interna e Otimização de Processos

## 3.1 Épico: Gerenciamento de Produtos pelo Administrador

**US18**: Como administrador, eu quero adicionar novos produtos ao catálogo, para disponibilizá-los aos clientes.

**US19**: Como administrador, eu quero editar produtos existentes no catálogo, para corrigir ou atualizar informações.

**US20**: Como administrador, eu quero remover produtos do catálogo, para manter apenas itens disponíveis à venda.

## 3.2 Épico: Gestão de Estoque e Pedidos

**US21**: Como administrador, eu quero editar as quantidades em estoque de cada produto, para que eu possa corrigir erros ou atualizar após reabastecimento.

**US22**: Como administrador, eu quero poder alterar o status de uma compra (em processamento, enviado, entregue ou cancelado), para que o cliente acompanhe o andamento do pedido.

**Regras de Negócio**:
- Sempre que a situação de um pedido for atualizada, o **cliente deve ser notificado imediatamente** sobre a nova situação.


### 9.2 Priorização do Backlog Geral

# Priorização do Backlog - Técnica MoSCoW

Nesta seção, realizamos a priorização dos itens do backlog utilizando a técnica **MoSCoW**, que organiza as funcionalidades em três categorias principais:

  1. **Must have (deve ter)**: Aquilo que é considerado obrigatório ou imprescindível para o projeto ou negócio;
  2. **Should have (deveria ter)**: Tudo aquilo que è importante ter, mas não é imprescindível para o projeto ou negócio;
  3. **Could have (poderia ter)**: Tudo aquilo que não é essencial, mas seria bom ter ou poderia ser um referencial;
  4. **Won’t have (não terá - por enquanto)**: Não agrega valor ao negócio no momento e, por enquanto, não será feito.

# Critérios de priorização

Como base para a priorização objetiva dos requisitos, a equipe selecionou a ferramenta WSJF (Weighted Shortest Job First), que considera critérios referentes ao valor para o negócio, a ferramenta RICE (Reach, Impact, Confidence, Effort), que considera critérios referentes ao valor para o usuário, e a pontuação de esforço relativo pela equipe.
Para calcular os valores WSJF, utilizamos a fórmula:
        
<center><strong>WSJF = Cost of Delay (CoD) / Job Duration</strong></center><br>

Para obter-se o custo de atraso (Cost of Delay - CoD), atribui-se um valor de 0 a 5 para os seguintes critérios. Posteriormente, somam-se esses valores:

  - **Valor para o negócio**: Qual o potencial valor ou impacto negativo para o negócio? (0: mínimo valor de negócio; 5: máximo valor de negócio);

  - **Criticidade temporal**: Como o valor comercial diminui ao longo do tempo? Os usuários esperarão por nós ou buscarão outra solução (0: mínima criticidade temporal; 5: máxima criticidade temporal);

  - **Redução de risco**: Qual o risco de adiar essa iniciativa para o negócio? (0: mínima redução de risco; 5: máxima redução de risco).

Para a atribuição de valor à duração ou ao tamanho do trabalho, considera-se o valor constante 3 (CAROLI, 2023).

Para calcular Os valores **RICE**, utilizamos a fórmula:
        
<center><strong>RICE = (Alcance + Impacto + Confiança ) / 3</strong></center><br>

Os critérios RICE, aos quais se deve atribuir um valor de 0 a 5, definem-se como:

- **Alcance**: Quantas pessoas serão impactadas por essa iniciativa? (Considerar para o mesmo período) (0: mínimo alcance; 5: máximo alcance);

- **Impacto**: Quanto essa iniciativa afetará cada uma dessas pessoas? (0: mínimo impacto; 5: máximo impacto);

- **Confiança**: Quão confiante a equipe está nesses números? (0: confiança mínima; 5: confiança máxima).

Para obter a pontuação do esforço relativo pela equipe, estima-se, de 1 a 10, o esforço necessário para o desenvolvimento de cada requisito pela equipe. A iniciativa com menos esforço é classificada como 1. Todas as outras são comparadas ao esforço canônico - 1 (CAROLI, 2023).

Por fim, a priorização de cada requisito se dará com base na divisão da soma dos valores de **WSJF** e **RICE** pelo valor do Esforço Relativo: **(WSJF * RICE) / Esforço Relativo**. As classificações MosCoW são atribuídas a cada requisito a partir dos seguintes intervalos:

- 0 - 0.5: Won't have (1);

- 0.6 - 1.5: Could have (2);

- 1.6 - 2.5: Should have (3);

- 2.6 - 25: Must have (4).

## Objetivos Específicos (OE)

```
1. Ampliar o alcance de vendas / Expandir o negócio
2. Facilitar o processo de vendas
3. Otimizar processos de gestão
4. Integrar canais de venda e estoque
```

# Tabela de Backlog com Priorização


<table border="1" cellpadding="4" cellspacing="0" style="border-collapse:collapse; width:100%; font-size:13px;">
  <thead style="background:#f2f2f2;">
    <tr>
      <th>Tema</th>
      <th>Épico</th>
      <th>User Story</th>
      <th>Descrição</th>
      <th>OE</th>
      <th>RF</th>
      <th>WSJF</th>
      <th>RICE</th>
      <th>Esforço relativo</th>
      <th>Prioridade</th>
      <th>MVP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3. Gestão Interna e Otimização de Processos</td>
      <td>3.1 Gerenciamento de Produtos pelo Administrador</td>
      <td>US18</td>
      <td>Adicionar produtos ao catálogo</td>
      <td>OE4</td>
      <td>RF18</td>
      <td>4,33</td>
      <td>5,00</td>
      <td>4</td>
      <td style="background:#f8d7da;">5,41</td>
      <td>X</td>
    </tr>
    <tr>
      <td>3. Gestão Interna e Otimização de Processos</td>
      <td>3.2 Gestão de Estoque e Pedidos</td>
      <td>US21</td>
      <td>Editar quantidade em estoque</td>
      <td>OE3</td>
      <td>RF21</td>
      <td>4,00</td>
      <td>5,00</td>
      <td>4</td>
      <td style="background:#f8d7da;">5,00</td>
      <td>X</td>
    </tr>
    <tr>
      <td>3. Gestão Interna e Otimização de Processos</td>
      <td>3.1 Gerenciamento de Produtos pelo Administrador</td>
      <td>US20</td>
      <td>Remover produtos do catálogo</td>
      <td>OE3</td>
      <td>RF20</td>
      <td>3,67</td>
      <td>5,00</td>
      <td>4</td>
      <td style="background:#f8d7da;">4,58</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.1 Processo de compra</td>
      <td>US07</td>
      <td>Buscar Produtos</td>
      <td>OE2</td>
      <td>RF07</td>
      <td>4,67</td>
      <td>4,67</td>
      <td>5</td>
      <td style="background:#fff3cd;">4,36</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.4 Engajamento e Pós-Venda</td>
      <td>US17</td>
      <td>Solicitar devolução/troca</td>
      <td>OE3</td>
      <td>RF17</td>
      <td>4,00</td>
      <td>4,33</td>
      <td>4</td>
      <td style="background:#fff3cd;">4,33</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.2 Gerenciamento do Carrinho</td>
      <td>US09</td>
      <td>Adicionar produtos ao carrinho</td>
      <td>OE2</td>
      <td>RF09</td>
      <td>3,33</td>
      <td>3,33</td>
      <td>4</td>
      <td style="background:#fff3cd;">2,78</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td></td>
      <td>US10</td>
      <td>Editar produtos do carrinho</td>
      <td>OE2</td>
      <td>RF10</td>
      <td>3,33</td>
      <td>3,33</td>
      <td>4</td>
      <td style="background:#fff3cd;">2,78</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td></td>
      <td>US11</td>
      <td>Remover produtos do carrinho</td>
      <td>OE2</td>
      <td>RF11</td>
      <td>3,33</td>
      <td>3,33</td>
      <td>4</td>
      <td style="background:#fff3cd;">2,78</td>
      <td>X</td>
    </tr>
    <tr>
      <td>3. Gestão Interna e Otimização de Processos</td>
      <td>3.2 Gestão de Estoque e Pedidos</td>
      <td>US22</td>
      <td>Gerenciar situação dos pedidos</td>
      <td>OE3</td>
      <td>RF22</td>
      <td>3,00</td>
      <td>3,67</td>
      <td>4</td>
      <td style="background:#fff3cd;">2,75</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.3 Finalização da Compra e Pagamento</td>
      <td>US13</td>
      <td>Finalizar compra</td>
      <td>OE2</td>
      <td>RF13</td>
      <td>4,00</td>
      <td>4,67</td>
      <td>7</td>
      <td style="background:#fff3cd;">2,67</td>
      <td>X</td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td></td>
      <td>US11</td>
      <td>Visualizar resumo da compra</td>
      <td>OE2</td>
      <td>RF11</td>
      <td>3,33</td>
      <td>3,67</td>
      <td>5</td>
      <td style="background:#d4edda;">2,44</td>
      <td>X</td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.2 Gerenciamento de perfil do usuário</td>
      <td>US05</td>
      <td>Editar dados da conta</td>
      <td>OE2</td>
      <td>RF05</td>
      <td>3,00</td>
      <td>4,00</td>
      <td>5</td>
      <td style="background:#d4edda;">2,40</td>
      <td></td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.1 Cadastro e Acesso do Usuário</td>
      <td>US04</td>
      <td>Recuperar senha</td>
      <td>OE3</td>
      <td>RF04</td>
      <td>4,00</td>
      <td>4,00</td>
      <td>7</td>
      <td style="background:#d4edda;">2,29</td>
      <td></td>
    </tr>
    <tr>
      <td>3. Gestão Interna e Otimização de Processos</td>
      <td>3.1 Gerenciamento de Produtos pelo Administrador</td>
      <td>US18</td>
      <td>Editar produtos no catálogo</td>
      <td>OE3</td>
      <td>RF18</td>
      <td>3,33</td>
      <td>4,00</td>
      <td>6</td>
      <td style="background:#d4edda;">2,22</td>
      <td></td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.1 Cadastro e Acesso do Usuário</td>
      <td>US01</td>
      <td>Cadastrar usuário</td>
      <td>OE2</td>
      <td>RF01</td>
      <td>2,67</td>
      <td>3,00</td>
      <td>4</td>
      <td style="background:#d4edda;">2,00</td>
      <td></td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.1 Cadastro e Acesso do Usuário</td>
      <td>US02</td>
      <td>Logar usuário</td>
      <td>OE2</td>
      <td>RF02</td>
      <td>2,67</td>
      <td>3,00</td>
      <td>4</td>
      <td style="background:#d4edda;">2,00</td>
      <td></td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.4 Engajamento e Pós-Venda</td>
      <td>US15</td>
      <td>Adicionar avaliação produtos</td>
      <td>OE3</td>
      <td>RF15</td>
      <td>4,00</td>
      <td>3,67</td>
      <td>8</td>
      <td style="background:#d4edda;">1,83</td>
      <td></td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.4 Engajamento e Pós-Venda</td>
      <td>US16</td>
      <td>Remover Avaliação de produtos</td>
      <td>OE3</td>
      <td>RF16</td>
      <td>4,00</td>
      <td>3,67</td>
      <td>8</td>
      <td style="background:#d4edda;">1,83</td>
      <td></td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.1 Cadastro e Acesso do Usuário</td>
      <td>US03</td>
      <td>Deslogar usuário</td>
      <td>OE2</td>
      <td>RF03</td>
      <td>2,67</td>
      <td>2,67</td>
      <td>4</td>
      <td style="background:#d4edda;">1,78</td>
      <td></td>
    </tr>
    <tr>
      <td>1. Gestão de Clientes e Usuários</td>
      <td>1.2 Gerenciamento de perfil do usuário</td>
      <td>US06</td>
      <td>Deletar usuário</td>
      <td>OE3</td>
      <td>RF06</td>
      <td>1,33</td>
      <td>2,33</td>
      <td>2</td>
      <td style="background:#d4edda;">1,56</td>
      <td></td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.4 Engajamento e Pós-Venda</td>
      <td>US14</td>
      <td>Gerar códigos de desconto</td>
      <td>OE1</td>
      <td>RF14</td>
      <td>2,33</td>
      <td>2,67</td>
      <td>5</td>
      <td style="background:#d4edda;">1,24</td>
      <td></td>
    </tr>
    <tr>
      <td>2. Vendas e Experiência do Cliente</td>
      <td>2.1 Processo de compra</td>
      <td>US08</td>
      <td>Personalizar produto</td>
      <td>OE1</td>
      <td>RF08</td>
      <td>3,67</td>
      <td>2,67</td>
      <td>10</td>
      <td style="background:#d4edda;">0,98</td>
      <td></td>
    </tr>
  </tbody>
</table>
