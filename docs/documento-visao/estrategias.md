#### 3.1 Estratégia Priorizada

- **Abordagem:** Híbrida
- **Ciclo de vida:** Incremental e Iterativo
- **Processo:** RAD (Rapid Application Development)

#### 3.2 Quadro Comparativo

O Quadro, a seguir, apresenta algumas características que podem ser relacionadas ao OpenUP e ao RAD (Rapid Application Development), visando auxiliar no entendimento e justificativa da escolha do processo mais adequado ao caso da LF Bag Your Dreams.

| **Características** | **OpenUP** | **RAD** |
| --- | --- | --- |
| Abordagem Geral | Iterativo, incremental e direcionado pela arquitetura. | Ágil, centrada no usuário e no design do produto. |
| Foco em Arquitetura | Forte ênfase na definição de uma arquitetura sólida e flexível desde o início do projeto. | Inicialmente, há pouca preocupação com a arquitetura. À medida que os protótipos são refinados, a estrutura vai evoluindo. |
| Estrutura de Processos | Estrutura mais formal com fases bem definidas (Iniciação, Elaboração, Construção, Transição). Oferece um roteiro claro para o desenvolvimento. | Estrutura menos formal, com definição de requisitos e modelagem mais rápidas. E a prototipagem, revisão e implementação ocorrem em ciclos mais curtos. |
| Flexibilidade de Requisitos | Flexibilidade para adaptações iterativas, mas dependente de uma arquitetura bem definida. Mudanças drásticas podem exigir revisões significativas na arquitetura. | Alta flexibilidade, em que mudanças podem ser incorporadas entre iterações de protótipo sem grandes retrabalhos. |
| Colaboração com Cliente | Envolvimento contínuo, com foco nas fases de entrega e validação. Colaboração intensa nas fases iniciais e finais do projeto. | Feedback constante por meio de workshops e demonstrações dos protótipos. |
| Complexidade do Processo | Mais formal e estruturado, com documentação detalhada. Exige mais disciplina e papeis bem definidos. | Processo leve e informal, com menor burocracia e papeis flexíveis. |
| Qualidade Técnica | Qualidade assegurada pela definição clara da arquitetura e validação incremental. Permite um controle rigoroso da qualidade em cada fase. | Depende da maturidade das ferramentas e das revisões nos protótipos; risco de comprometer qualidade técnica se os ciclos forem muito curtos ou mal gerenciados. |
| Práticas de Desenvolvimento | Estrutura formal com foco em arquitetura e controle de progresso. Menos práticas técnicas específicas. | Fortemente orientado a prototipagem rápida, desenvolvimento de componentes reutilizáveis e integração contínua. |
| Adaptação ao Projeto da LF Bag Your Dreams | Adequado para projetos que exigem uma arquitetura bem definida desde o início, como a integração com sistemas de estoque e pagamento. Permite entregas incrementais com flexibilidade limitada. | Ideal para validar rapidamente interfaces de usuário e fluxos de venda/pagamento junto ao cliente. |
| Documentação | Requer documentação formal para cada fase, com ênfase em requisitos e arquitetura. Pode ser mais pesado em termos de tempo e recursos. | Documentação mínima, reservada apenas para o essencial. |
| Controle de Qualidade | Validações incrementais e revisões da arquitetura em cada fase. Garante que os requisitos sejam atendidos em cada etapa. | Testes incorporados a cada protótipo; validação prática, porém menos formalizada (foco no uso real em vez de documentos). |
| Escalabilidade | Pode ser aplicado em projetos maiores e mais complexos, com equipes médias a grandes. Permite um controle mais centralizado e coordenado. | Melhor para projetos de pequena a média escala; projetos muito grandes podem sofrer com a falta de governança e padronização. |
| Suporte a Equipes de Desenvolvimento | Suporta equipes maiores com papeis definidos, exigindo controle sobre o progresso e as fases do projeto. Facilita a gestão de projetos complexos com muitas partes interessadas. | Voltado a equipes pequenas e multifuncionais, com papeis fluidos e alta comunicação direta. |

#### 3.3 Justificativa

Com base nas características do projeto e nos desafios enfrentados pela LF Bag Your Dreams, o **RAD (Rapid Application Development)** é o processo mais adequado pelo seguintes motivos:

**3.3.1. Flexibilidade e entregas rápidas**

- Ao contrário do OpenUP, que possui foco na arquitetura e é orientado a papéis bem definidos, o RAD é focado em prototipação eficiente e colaboração contínua com o cliente, permitindo que a equipe receba feedbacks a cada ciclo, e viabilizando maior flexibilidade na construção da solução. Esse fator é importantíssimo para este projeto, cujo diferencial está justamente na experiência personalizada do usuário. O desenvolvimento iterativo e incremental facilita ajustes ao longo do processo, mantendo o sistema sempre direcionado às necessidades básicas dos usuários finais.

**3.3.2. Práticas de qualidade técnica eficientes**

- A partir da entrega rápida de protótipo funcional, o RAD antecipa a identificação de possíveis problemas na interface e facilita a confirmação de escolhas de design.
- O RAD favorece práticas de testes a cada ciclo de desenvolvimento, de modo a adequar-se ao cronograma curto, e permitindo a entrega de valor rápida a cada ciclo. 
- O RAD incentiva a reutilização de código, com fácil integração.

**3.3.3. Satisfação do cliente**

- Tendo o foco no constante envolvimento do cliente para realizar validações ao longo de todo o projeto, não somente nas fases iniciais e finais, o RAD permite a rápida adaptação de cada funcionalidade às necessidades e desejos do cliente, de modo a contribuir para a sua satisfação durante a entrega do sistema.
