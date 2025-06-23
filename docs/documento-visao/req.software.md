### 7.1 Lista de Requisitos Funcionais

Requisitos funcionais descrevem as funcionalidades e as ações que um sistema ou produto deve ser capaz de executar. Eles detalham as tarefas específicas que este produto deve realizar para atender às necessidades do usuário.

**Gerenciamento de Conta do Usuário**

- **RF01** - Cadastrar usuário no sistema 

- **RF02** - Logar usuário no sistema

- **RF03** - Deslogar usuário do sistema

- **RF04** - Recuperar senha

- **RF05** - Editar dados da conta do usuário

- **RF06** - Deletar usuário do sistema

**Processo de Compra**

- **RF07** - Buscar por produtos no sistema por nome e categoria

- **RF08** - Personalizar o produto

**Carrinho de Compras**

- **RF09** - Adicionar produtos ao carrinho

- **RF10** - Editar produtos do carrinho

- **RF11** - Remover produtos do carrinho

**Finalização da Compra e Pagamento**

- **RF12** - Gerar resumo da compra

- **RF13** - Finalizar compra
    * **Regra de negócio**: Enviar notificação automática para informar compra realizada.

**Engajamento e Pós-Venda**

- **RF14** -  Gerar códigos ou links de desconto por recomendação

- **RF15** - Adicionar avaliação de produtos (estrelas e comentários)

- **RF16** - Remover avaliação de produtos (estrelas e comentários)

- **RF17** - Solicitar devolução/troca de produto

**Gerenciamento de Produtos pelo Administrador**

- **RF18** - Adicionar produtos ao catálogo

- **RF19** - Editar produtos do catálogo

- **RF20** - Remover produtos do catálogo


**Gestão de Estoque e Pedidos**

- **RF21** - Editar a quantidade do produto em estoque

- **RF22** - Alterar status de um pedido
    * **Regra de negócio**: Notificar por e-mail mudanças no status do pedido


### 7.2 Lista de Requisitos Não Funcionais

Requisitos não funcionais descrevem características e qualidades do sistema ou produto. Neste projeto, os requisitos não funcionais foram definidos a partir do modelo **URPS+**, que considera aspectos como usabilidade, confiabilidade, desempenho e suportabilidade.

**Usability** (Usabilidade)

- **RNF01:** O sistema deverá possuir uma interface responsiva, adaptando-se corretamente a dispositivos móveis (largura mínima de 320px), tablets, e desktops (até 1920px), mantendo a usabilidade e legibilidade em todas as resoluções.

- **RNF02:** O sistema deverá ser compatível com os principais navegadores modernos, garantindo funcionamento correto da interface e funcionalidades nas seguintes versões mínimas: Google Chrome 110+, Mozilla Firefox 110+, Microsoft Edge 110+, Apple Safari 15+ e Opera 90+.

- **RNF03:** O sistema deverá apresentar recursos de personalização da página, permitindo ao usuário ajustar o tamanho da fonte e o espaçamento entre caracteres e linhas.

- **RNF04:** O sistema deverá exibir o catálogo de produtos durante o primeiro contato do usuário com a plataforma.


**Reliability** (Confiabilidade)

- **RNF05:** O sistema deverá atender aos artigos 8 e 18 da LGPD. O artigo 8 exige que o consentimento do usuário para a coleta de dados pessoais seja livre, informado e explícito, devendo ser obtido por meio de uma manifestação clara. Já o artigo 18 garante ao titular dos dados o direito de acessar, corrigir, excluir e revogar o consentimento sobre seus dados pessoais.

- **RNF06:** O sistema deverá ser entregue com um usuário administrador previamente cadastrado no banco de dados, sem necessidade de registro manual via interface gráfica.


**Performance** (Desempenho)

- **RNF07:** O tempo de carregamento da interface (frontend) deverá ser inferior a 2 segundos.

**Supportability** (Suportabilidade)

- **RNF08:** O sistema deverá ser integrado a API do Mercado Pago, para a realização do pagamento pelos usuários.

