### 7.1 Lista de Requisitos Funcionais

Requisitos funcionais descrevem as funcionalidades e as ações que um sistema ou produto deve ser capaz de executar. Eles detalham as tarefas específicas que este produto deve realizar para atender às necessidades do usuário.

**Autenticação**

- **RF01 - Cadastrar usuário no sistema:** O usuário deverá ser capaz de cadastrar uma conta no sistema, fornecendo os dados solicitados.
- **RF02 - Autenticar usuário no sistema:** O usuário deverá ser capaz de realizar login no sistema com as suas credenciais previamente cadastradas.
- **RF03 - Deslogar usuário do sistema:** O usuário deverá ser capaz de realizar logout no sistema.
- **RF04 - Recuperar senha:** O usuário deverá ser capaz de recuperar o acesso à sua conta por meio de um processo de redefinição de senha via e-mail.
- **RF05 - Deletar usuário do sistema:** O usuário deverá ser capaz de deletar a sua conta permanentemente no sistema.
- **RF06 - Edição de dados da conta do usuário:** O usuário deverá ser capaz de editar seus dados registrados no sistema.

**Carrinho de Compras**

- **RF07 - Adicionar produtos ao carrinho:** O usuário deverá ser capaz de adicionar um ou mais produtos ao carrinho de compras a partir do catálogo do sistema.
- **RF08 - Remover produtos do carrinho:** O usuário deverá ser capaz de remover um ou mais produtos do carrinho. 

**Catálogo de Produtos**

- **RF09 - Visualizar produtos no sistema:** O usuário deverá ser capaz de visualizar um catálogo que apresente os produtos cadastrados no sistema pelo administrador.
- **RF10 - Buscar produtos no sistema:** O usuário deverá ser capaz de buscar por produtos específicos no sistema.
- **RF11 - Filtrar produtos por categoria:** O usuário deverá ser capaz de filtrar os produtos que visualiza no catálogo por categoria (bolsas casuais, bolsas térmicas, mochilas universitárias, carteiras, necessaire).

**Checkout**

- **RF12 - Visualizar o resumo da compra:** O usuário deverá ser capaz de visualizar os produtos escolhidos para a compra.
- **RF13 - Escolher a forma de pagamento:** O usuário deverá ser capaz de escolher como realizar o pagamento (pix, boleto, cartão).
- **RF14 - Personalizar o produto:** O usuário deverá ser capaz de personalizar cada componente de um produto para realizar a compra.
- **RF15 - Aplicar códigos de desconto:** O usuário deverá ser capaz de inserir códigos válidos para aplicar descontos na finalização da compra.

**Área do Administrador**

- **RF16 - Gerenciar catálogo:** O administrador deverá ser capaz de visualizar, adicionar, editar e remover produtos a serem exibidos no catálogo para todos os usuários.
- **RF17 - Atualização automática do estoque:** O sistema deverá atualizar automaticamente a quantidade disponível de cada produto no sistema conforme compras realizadas pelos usuários.
- **RF18 - Gerenciar estoque:** O administrador deverá ser capaz de editar a quantidade disponível para cada produto no sistema.
- **RF19 - Gerenciar situação dos pedidos:** O administrador deverá ser capaz de visualizar todos os pedidos e atualizar seu status (ex: em processamento, enviado, entregue, cancelado).

**Notificações**

- **RF20 - Enviar notificações automáticas (e-mail) para confirmação de pedidos:** O sistema deverá enviar automaticamente um e-mail de confirmação ao usuário após a finalização de um pedido.

**Descontos por Recomendação**

- **RF21 - Gerar códigos ou links de desconto por recomendação:** O sistema deverá fornecer códigos ou links de desconto após o usuário compartilhar o site com outras pessoas.

**Avaliação de Produtos**

- **RF22 - Sistema de avaliação de produtos (estrelas, comentários, imagens, vídeos):** O usuário deverá ser capaz de avaliar produtos adquiridos utilizando um sistema de estrelas (de 1 a 5), deixar comentários textuais sobre os produtos e anexar imagens e vídeos às suas avaliações.
- **RF23 - Solicitar devolução/troca de produto:** O usuário dev

### 7.2 Lista de Requisitos Não Funcionais

Requisitos não funcionais descrevem características e qualidades do sistema ou produto. Neste projeto, os requisitos não funcionais foram definidos a partir do modelo **URPS+**, que considera aspectos como usabilidade, confiabilidade, desempenho e suportabilidade.

**Usability**

- **RFN01:** O sistema deverá possuir uma interface responsiva.
- **RFN02:** O sistema deverá ser compatível com os principais navegadores modernos, incluindo Firefox, Safari, Chrome, Opera e Edge.
- **RFN03:** O sistema deverá apresentar recursos de acessibilidade visual, tais como ampliação da fonte de texto e espaçamento de caracteres.

**Reliability**

- **RFN04:** O sistema deverá estar em conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD).

**Performance**

- **RFN05:** O tempo de carregamento da interface (frontend) deverá ser inferior a 2 segundos.

**Supportability**

- **RFN06:** O sistema deverá ser integrado a uma API de comércio eletrônico/vendas externa, para a realização do pagamento pelos usuários.
