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

# 📋 Tabela de Backlog com Priorização

| **User Story** | **Descrição**                                 | **Prioridade**         |
|:--------------:|:---------------------------------------------:|:---------------------:|
| **US09**      | Visualizar Produtos                             | 🟥 Alta (Must have)   |
| **US12**      | Visualizar resumo da compra                            | 🟥 Alta (Must have)   |
| **US13**      | Selecionar Pagamento                               | 🟥 Alta (Must have)   |
| **US14**      |  Selecionar pagamento                            | 🟥 Alta (Must have)   |
| **US17**      |  Gerenciar catálogo                                | 🟥 Alta (Must have)   |
| **US18**      |   Atualização automática do estoque                  | 🟥 Alta (Must have)   |
| **US19**      | Editar estoque                    | 🟥 Alta (Must have)   |
| **US20**      | Gerenciar situação dos pedidos                             | 🟥 Alta (Must have)   |
| **US25**      | Solicitar devolução/troca                              | 🟥 Alta (Must have)   |
| **US01**      | Cadastrar usuário                 | 🟧 Média (Should have)   |
| **US02**      |  Autenticar usuário                               | 🟧 Média (Should have)|
| **US03**      | Deslogar usuário                                | 🟧 Média (Should have)|
| **US04**      |  Recuperar senha                           | 🟧 Média (Should have)|
| **US07**      | Adicionar produtos ao carrinho              | 🟧 Média (Should have)|
| **US08**      |  Remover produtos do carrinho                      | 🟧 Média (Should have)|
| **US10**      |  Buscar produtos                      | 🟧 Média (Should have)|
| **US15**      | Personalizar produto                             | 🟧 Média (Should have) |
| **US05**      | Editar dados da conta                          | 🟨 Baixa (Could have) |
| **US06**      | Deletar usuário                                | 🟨 Baixa (Could have) |
| **US11**      | Filtrar produtos                               | 🟨 Baixa (Could have) |
| **US16**      | Aplicar códigos de desconto                    | 🟨 Baixa (Could have) |
| **US21**      | Enviar notificações automáticas                | 🟨 Baixa (Could have) |
| **US22**      | Enviar notificações automáticas ao administrador (pedido realizado)                     | 🟨 Baixa (Could have) |
| **US23**      | Gerar códigos de desconto                           | 🟨 Baixa (Could have) |
| **US24**      | Sistema de avaliação                           | 🟨 Baixa (Could have) |
