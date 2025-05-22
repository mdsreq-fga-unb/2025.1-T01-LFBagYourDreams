
| **Ciclo** | **Início** | **Fim** | **Objetivo Principal** | **Entregas Esperadas** | **Validação do Cliente** |
|:---:| :---: | :---: | :---: | :---: | :---: |
| **1** | 22/04/2025 | 04/05/2025 | Planejamento e Definição de Backlog | \- Definição do backlog inicial.<br><br>\- Configuração da arquitetura (React, Python, MongoDB, Docker).<br><br>\- Ambiente de desenvolvimento pronto. | Revisão do backlog e confirmação de prioridades. |
| **2** | 05/05/2025 | 18/05/2025 | Interface inicial do sistema | \- Catálogo de produtos;<br><br>\- Sistema de personalização de cada produto;<br><br>\- Sistema de autenticação. | Validação do catálogo, sistema de personalização de produtos, e sistema de autenticação. |
| **3** | 19/05/2025 | 28/05/2025 | Perfil do usuário, pagamento através da plataforma| \- Edição de dados da conta do usuário;<br><br>\- Integração com sistema de pagamento externo. | Validação da área de perfil do usuário e do fluxo de pedidos.
| **4** | 29/05/2025 | 08/06/2025 | Notificações automáticas e mecanismo de desconto, área de administração | \- Notificações automáticas (e-mail) para confirmação de pedidos.<br><br> \- Descontos por recomendação (código de desconto ou links).<br><br> \- Gerenciamento de estoque;<br><br> \- Gerenciamento de situação dos pedidos. | Validação do sistema de notificações por e-mail; validação do sistema de descontos por divulgação do software.<br>Validação das funcionalidades do administrador.
| **5** | 09/06/2025 | 18/06/2025 | Avaliação dos produtos, carrinho de compras  | \- Implementação do sistema de avaliação de produtos (estrelas, comentários, imagens, vídeos).<br><br> \- Implementação do carrinho de compras. | Feedback das avaliações e validação do fluxo do carrinho de compras.
| **6** | 19/06/2025 | 28/06/2025 | Lançamento Final e Monitoramento | \- Lançamento final do sistema para todos os usuários;<br><br>\- Monitoramento pós-lançamento e ajustes com base nos primeiros feedbacks. | Homologação pela cliente e aprovação final.<br>Feedback dos primeiros usuários reais e ajustes pós-lançamento. |


**Considerações importantes:**

1. **Datas de início e fim:** Cada ciclo tem a duração de 9 dias, começando em 22/04/2025 e finalizando em 24/08/2025, distribuindo as entregas parciais ao longo do tempo, com exceção do ciclo 4, que, devido a uma quantidade maior de funcionalidades a serem desenvolvidas, possui 20 dias de duração (1 semana a mais). 

2. **Etapas da metodologia RAD a cada ciclo:** No primeiro ciclo do cronograma, haverá a etapa de planejamento de requisitos, em conjunto com a cliente. Em cada ciclo intermediário, serão realizados o design do usuário (prototipação), a construção rápida e incremental, testes e coleta de feedbacks da cliente. No último ciclo (cutover), será realizada a implantação do sistema.

3. **Ciclos:** O RAD é centrado na iteratividade, prototipação rápida, feedback constante dos usuários e ajustes contínuos, e o nosso ciclo ilustrado na figura 2 segue a seguinte lógica: 

    >a. **User Design**– o foco é entender as necessidades do usuário e fazer ajustes com base em feedbacks constantes.
    >
    >
    >b. **Construção** – Corresponde à fase de desenvolvimento e codificação rápida dos componentes definidos anteriormente.
    >
    >
    >c. **Testes** – Encaixa-se na fase de validação, onde o produto é testado frequentemente para detectar falhas cedo.


A sequência circular a sugere um **processo iterativo**:

![Ciclos do processo RAD](../assets/Ciclos.png)
 <center><strong>Figura 2:</strong> Ciclos do processo RAD</center>

