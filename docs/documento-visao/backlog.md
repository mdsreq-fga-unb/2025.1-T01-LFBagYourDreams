### 9.1 Backlog Geral

## Autenticação

**US01** - Como usuário, eu quero me cadastrar fornecendo os meus dados para que eu possa ter acesso às funcionalidades do sistema.

**US02** - Como usuário, eu quero fazer login no sistema com as minhas credenciais para que eu possa acessar minha conta e todas as suas funcionalidades.

**US03** - Como usuário, eu quero poder realizar o logoff para que ninguém utilize minha conta.

**US04** - Como usuário, eu quero poder recuperar minha senha para acessar minha conta caso eu a perca.

**US05** - Como usuário, eu quero poder editar meus dados como “e-mail” e “senha”, para manter minhas informações atualizadas.

**US06** - Como usuário, eu quero poder deletar a minha conta, para quando eu não possuir mais interesse em continuar na plataforma.

## Carrinho de Compras

**US07** - Como usuário, eu quero poder adicionar itens a um carrinho de compras a partir de um catálogo de produtos para que eu possa realizar uma compra.

**US08** - Como usuário, eu quero poder remover itens de um carrinho de compras para que esses itens não sejam incluídos em uma compra.

## Catálogo de Produtos

**US09** - Como usuário, eu gostaria de visualizar os produtos no catálogo, para melhor escolher o produto desejado.

**US10** - Como usuário, eu gostaria de buscar pelos produtos do catálogo por barra de pesquisa, para localizar meus interesses mais facilmente.

**US11** - Como usuário, eu gostaria de filtrar os produtos do catálogo por categoria, para facilitar a minha busca.

## Checkout

**US12** - Como usuário, eu quero poder visualizar um resumo de uma compra a ser finalizada, definido por um conjunto de itens que adicionei ao carrinho.

**US13** - Como usuário, eu gostaria de realizar o pagamento por diversos meios (cartão, pix, boleto), para ter flexibilidade na hora do pagamento.

**US14** - Como usuário, eu gostaria de personalizar e escolher cada um dos componentes das bolsas, para garantir que a bolsa seja do jeito que eu quero.

**US15** - Como usuário, eu quero poder aplicar um código de desconto a uma compra para que o valor final da compra receba o desconto correspondente.

## Área do Administrador

**US16** - Como administrador, eu quero gerenciar o catálogo de produtos (visualizar, adicionar, editar, remover) para que eu possa manter minha loja atualizada com os produtos corretos.

**US17** - Como administrador, eu quero que o sistema atualize automaticamente o estoque após cada compra, para facilitar e tornar mais seguro o controle de estoque.

- **US18** - Como administrador, eu quero editar as quantidades em estoque de cada produto, para que eu possa corrigir erros ou atualizar após reabastecimento.
- **US19** - Como administrador, eu quero gerenciar o status de cada compra - compra em processamento, enviado, entregue ou cancelado -, para que eu possa estar atento a quaisquer eventualidades que possam ocorrer na compra.

## Notificações

**US20** - Como usuário, eu quero receber notificações automáticas no e-mail para confirmar o meu pedido, para que eu possa ter confirmação e acompanhamento da compra.

## Descontos por Recomendação

**US21** - Como usuário, eu quero receber desconto ao compartilhar o site com outras pessoas, para que eu possa obter benefícios em compras por indicar o site para meus contatos.

## Avaliação de Produtos

**US22** - Como usuário, eu quero avaliar produtos que adquiri (usando estrelas, comentários, imagens e vídeos), para que eu possa compartilhar minha experiência e dar meu feedback com outros clientes e com a loja.

**US23** - Como usuário, eu quero ser capaz de iniciar um processo de devolução ou troca de um item comprado, para que eu possa resolver problemas com produtos recebidos de forma prática e eficiente.


### 9.2 Priorização do Backlog Geral

## Priorização do Backlog - Técnica MoSCoW

Nesta seção, realizamos a priorização dos itens do backlog utilizando a técnica **MoSCoW**, que organiza as funcionalidades em três categorias principais:

- **Must have**: Funcionalidades essenciais para o funcionamento do produto, que devem ser entregues sem exceção.
- **Should have**: Funcionalidades importantes, porém que podem ser implementadas após as funcionalidades essenciais.
- **Could have**: Funcionalidades desejáveis, que agregam valor, mas não são prioritárias no escopo inicial.

A priorização teve como objetivo garantir que o desenvolvimento fosse focado nas funcionalidades mais críticas, alinhando o produto às necessidades do negócio e aos recursos disponíveis. Cada integrante do grupo deu notas de 1 a 3, cada uma tendo sua recṕroca nas categorias do MoSCoW, para cada um dos requisitos. A partir da média dessas notas, foi realizada a priorização.

## 📋 Tabela de Backlog com Priorização

| **User Story** | **Descrição**                                 | **Prioridade**         |
|:--------------:|:---------------------------------------------:|:---------------------:|
| **US02**      | Autenticar usuário                             | 🟥 Alta (Must have)   |
| **US07**      | Adicionar produtos                             | 🟥 Alta (Must have)   |
| **US08**      | Remover produtos                               | 🟥 Alta (Must have)   |
| **US09**      | Visualizar produtos                            | 🟥 Alta (Must have)   |
| **US10**      | Buscar produtos                                | 🟥 Alta (Must have)   |
| **US12**      | Visualizar resumo da compra                    | 🟥 Alta (Must have)   |
| **US13**      | Escolher forma de pagamento                    | 🟥 Alta (Must have)   |
| **US16**      | Gerenciar catálogo                             | 🟥 Alta (Must have)   |
| **US18**      | Gerenciar estoque                              | 🟥 Alta (Must have)   |
| **US19**      | Gerenciar situação dos pedidos                 | 🟥 Alta (Must have)   |
| **US03**      | Deslogar usuário                               | 🟧 Média (Should have)|
| **US04**      | Recuperar senha                                | 🟧 Média (Should have)|
| **US14**      | Personalizar produto                           | 🟧 Média (Should have)|
| **US17**      | Atualização automática do estoque              | 🟧 Média (Should have)|
| **US23**      | Solicitar devolução/troca                      | 🟧 Média (Should have)|
| **US01**      | Cadastrar usuário                              | 🟨 Baixa (Could have) |
| **US05**      | Editar dados da conta                          | 🟨 Baixa (Could have) |
| **US06**      | Deletar usuário                                | 🟨 Baixa (Could have) |
| **US11**      | Filtrar produtos                               | 🟨 Baixa (Could have) |
| **US15**      | Aplicar códigos de desconto                    | 🟨 Baixa (Could have) |
| **US20**      | Enviar notificações automáticas                | 🟨 Baixa (Could have) |
| **US21**      | Gerar códigos de desconto                      | 🟨 Baixa (Could have) |
| **US22**      | Sistema de avaliação                           | 🟨 Baixa (Could have) |
