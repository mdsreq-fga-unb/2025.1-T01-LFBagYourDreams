### 8.1 Definition of Ready (DoR)

O DoR é um acordo entre o time e o Product Owner (PO) indicando quando um requisito estará preparado para ser puxado para uma Sprint. Alguns itens que podem ser verificados para determinar se um requisito está 'Ready'
são:

- **O Requisito possui informação necessária para ser trabalhado?**  
   É fundamental que o requisito apresente informações claras e detalhadas, garantindo que a equipe de desenvolvimento possa iniciar o trabalho sem interpretações erradas.

- **O Requisito cabe em uma iteração?**  
   O requisito deve ter um tamanho que permita sua conclusão dentro de uma única iteração.

- **O Requisito está representado por uma história de usuário?**  
   O requisito deve ser expresso como uma user story, garantindo melhor compreensão pelo time.

- **O Requisito está coberto por Critérios de Aceite?**  
   O requisito deve conter critérios de aceite claros e específicos, no formato Behavior Driven Development, antes de entrar em desenvolvimento.

- **O Requisito está mapeado para uma interface (quando necessário)?**  
   Caso o requisito demande uma interface, ele precisa ter sua representação visual definida (protótipo) para melhor clareza no desenvolvimento.

- **As dependências do Requisito estão identificadas (se houver)?**  
   Se o requisito tiver dependências (ex: APIs, times externos, componentes de UI), elas devem estar mapeadas e com plano de ação definido.

### 8.2 Definition of Done (DoD)

O DoD é um acordo que demonstra a qualidade do requisito produzido indicando que “Done” comprova a satisfação de todos com o trabalho realizado. Se um requisito não atende ao “Done”, ele não deve ser liberado ou apresentado nas entregas dos ciclos. Alguns itens que devem ser verificados para determinar se um requisito está 'Done' são:

- **A interface está de acordo com o protótipo passado pelo stakeholder?**  
  A interface deve estar de acordo com o que foi validado pela stakeholder.

- **Os critérios de aceitação definidos com o stakeholder foram atendidos?**  
  O requisito deve conter todas as ações e comportamentos esperados pelo stakeholder, assim como foi definido anteriormente.

- **O backend foi integrado ao frontend?**  
  Backend e frontend devem ser integrados corretamente.

- **O código segue os padrões e convenções definidos pelo time?**  
  O código deve estar de acordo com os padrões de estilo e formatação definidos pela equipe: PEP-8 para Python, e Airbnb React/JSX Style Guide para React Native.

- **A funcionalidade está responsiva?**  
  A funcionalidade deve estar responsiva, adaptando-se corretamente a dispositivos móveis (largura mínima de 320px), tablets, e desktops (até 1920px), mantendo a usabilidade e legibilidade em todas as resoluções.

- **Entrega um incremento do produto?**
 A funcionalidade implementada deve agregar valor ao produto, gerando um incremento funcional, utilizável e validado pelo usuário final, conforme o protótipo aprovado pela stakeholder.

– **Contempla os critérios de aceite estabelecidos?**
 Os critérios de aceitação, definidos em conjunto com a stakeholder, devem estar totalmente atendidos, incluindo todas as ações e comportamentos esperados, conforme validado no protótipo.

– **Está documentado para uso?**
 A documentação técnica e de usuário deve ser revisada e atualizada, garantindo que o incremento possa ser utilizado e mantido com facilidade pela equipe e pelo cliente.

– **A funcionalidade foi integrada e testada no ambiente adequado?**
 A integração entre backend e frontend deve estar completa e validada. Testes unitários e de integração devem ser realizados e aprovados, com produção em pares onde um desenvolve e testa o front-end e o outro o back-end, assegurando que a funcionalidade funciona corretamente e não impacta outras partes do sistema.



