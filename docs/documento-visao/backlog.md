### 9.1 Backlog Geral

# Autenticação

**US01** - Como usuário, eu quero me cadastrar fornecendo os meus dados para que eu possa ter acesso às funcionalidades do sistema.

**US02** - Como usuário, eu quero fazer login no sistema com as minhas credenciais para que eu possa acessar minha conta e todas as suas funcionalidades.

**US03** - Como usuário, eu quero poder realizar o logoff para que ninguém utilize minha conta.

**US04** - Como usuário, eu quero poder recuperar minha senha para acessar minha conta caso eu a perca.

**US05** - Como usuário, eu quero poder editar meus dados como “e-mail” e “senha”, para manter minhas informações atualizadas.

**US06** - Como usuário, eu quero poder deletar a minha conta, para quando eu não possuir mais interesse em continuar na plataforma.

# Carrinho de Compras

**US07** - Como usuário, eu quero poder adicionar itens a um carrinho de compras a partir de um catálogo de produtos para que eu possa realizar uma compra.

**US08** - Como usuário, eu quero poder remover itens de um carrinho de compras para que esses itens não sejam incluídos em uma compra.

# Catálogo de Produtos

**US09** - Como usuário, eu gostaria de visualizar os produtos no catálogo, para melhor escolher o produto desejado.

**US10** - Como usuário, eu gostaria de buscar pelos produtos do catálogo por barra de pesquisa, para localizar meus interesses mais facilmente.

**US11** - Como usuário, eu gostaria de filtrar os produtos do catálogo por categoria, para facilitar a minha busca.

**US12** - Como usuário, eu gostaria de visualizar detalhes de cada produto, para confirmar que ele se tornará o item de uma compra.

# Checkout

**US13** - Como usuário, eu quero poder visualizar um resumo de uma compra a ser finalizada, definido por um conjunto de itens que adicionei ao carrinho.

**US14** - Como usuário, eu gostaria de realizar o pagamento por diversos meios (cartão, pix, boleto), para ter flexibilidade na hora do pagamento.

**US15** - Como usuário, eu gostaria de personalizar e escolher cada um dos componentes das bolsas, para garantir que a bolsa seja do jeito que eu quero.

**US16** - Como usuário, eu quero poder aplicar um código de desconto a uma compra para que o valor final da compra receba o desconto correspondente.

# Área do Administrador

**US17** - Como administrador, eu quero gerenciar o catálogo de produtos (visualizar, adicionar, editar, remover) para que eu possa manter minha loja atualizada com os produtos corretos.

**US18** - Como administrador, eu quero que o sistema atualize automaticamente o estoque após cada compra, para facilitar e tornar mais seguro o controle de estoque.

**US19** - Como administrador, eu quero editar as quantidades em estoque de cada produto, para que eu possa corrigir erros ou atualizar após reabastecimento.

**US20** - Como administrador, eu quero gerenciar o status de cada compra - compra em processamento, enviado, entregue ou cancelado -, para que eu possa estar atento a quaisquer eventualidades que possam ocorrer na compra.

# Notificações

**US21** - Como usuário, eu quero receber notificações automáticas no e-mail para confirmar o meu pedido, para que eu possa ter confirmação e acompanhamento da compra.

**US22** - Como administrador, eu quero receber notificação automática no e-mail/WhatsApp para informar pedido realizado por um usuário, para facilitar o gerenciamento de pedidos.

# Descontos por Recomendação

**US23** - Como usuário, eu quero receber desconto ao compartilhar o site com outras pessoas, para que eu possa obter benefícios em compras por indicar o site para meus contatos.

# Avaliação de Produtos

**US24** - Como usuário, eu quero avaliar produtos que adquiri (usando estrelas, comentários, imagens e vídeos), para que eu possa compartilhar minha experiência e dar meu feedback com outros clientes e com a loja.

**US25** - Como usuário, eu quero ser capaz de iniciar um processo de devolução ou troca de um item comprado, para que eu possa resolver problemas com produtos recebidos de forma prática e eficiente.


### 9.2 Priorização do Backlog Geral

# Priorização do Backlog - Técnica MoSCoW

Nesta seção, realizamos a priorização dos itens do backlog utilizando a técnica **MoSCoW**, que organiza as funcionalidades em três categorias principais:

- **Must have**: Funcionalidades essenciais para o funcionamento do produto, que devem ser entregues sem exceção.
- **Should have**: Funcionalidades importantes, porém que podem ser implementadas após as funcionalidades essenciais.
- **Could have**: Funcionalidades desejáveis, que agregam valor, mas não são prioritárias no escopo inicial.

A priorização teve como objetivo garantir que o desenvolvimento fosse focado nas funcionalidades mais críticas, alinhando o produto às necessidades do negócio e aos recursos disponíveis. Cada integrante do grupo deu notas de 1 a 3, cada uma tendo sua recṕroca nas categorias do MoSCoW, para cada um dos requisitos. A partir da média dessas notas, foi realizada a priorização.

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


### 9.3 MVP

A priorização das funcionalidades teve como objetivo assegurar que o desenvolvimento do produto esteja focado nos itens mais críticos, alinhando-se tanto às necessidades do negócio quanto aos recursos disponíveis. Para isso, elaboramos uma tabela que detalha a classificação de cada item do backlog, promovendo maior clareza e organização para as próximas etapas do projeto.

Com base nesse processo, foi definido o MVP (Produto Mínimo Viável), composto por todos os itens classificados como “Must have”. Vale ressaltar que toda a priorização e definição do MVP foi realizada em conjunto com a LF Bag Your Dreams, garantindo o alinhamento com as expectativas e demandas da empresa.

| **ID**  | **Descrição**                                      | **Prioridade**        |
|---------|---------------------------------------------------|----------------------|
| **US09** | Visualizar Produtos                               | 🟥 Alta (Must have)  |
| **US12** | Visualizar resumo da compra                       | 🟥 Alta (Must have)  |
| **US13** | Selecionar Pagamento                              | 🟥 Alta (Must have)  |
| **US14** | Selecionar pagamento                              | 🟥 Alta (Must have)  |
| **US17** | Gerenciar catálogo                                | 🟥 Alta (Must have)  |
| **US18** | Atualização automática do estoque                 | 🟥 Alta (Must have)  |
| **US19** | Editar estoque                                    | 🟥 Alta (Must have)  |
| **US20** | Gerenciar situação dos pedidos                    | 🟥 Alta (Must have)  |
| **US25** | Solicitar devolução/troca                         | 🟥 Alta (Must have)  |


