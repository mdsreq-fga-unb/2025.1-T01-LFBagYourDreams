# User Story Mapping

___________________________________________________________________________________

## Empresa EduConnect

<div style="text-align: justify">
O EduConnect é uma iniciativa que surgiu a partir da experiência de três educadores, que identificaram significativas dificuldades enfrentadas pelas instituições de ensino na organização e acompanhamento de projetos interdisciplinares e atividades extracurriculares. Diante desse cenário,o objetivo do negócio é oferecer uma plataforma única, acessível e eficiente, que ajude a planejar, gerenciar e avaliar esses projetos de forma integrada.
</div>

___________________________________________________________________________________

## Quadro do USM

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVIoOhEtk=/?embedMode=view_only_without_ui&moveToViewport=-8679,2678,16507,6996&embedId=749184690904" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

___________________________________________________________________________________

## Personas 

- **Professor Coordenador**  
  Planeja e gerencia os projetos. Precisa de controle geral e visão estratégica.

- **Professor Participante**  
  Contribui com sua área no projeto. Precisa de acesso às informações e boa comunicação.

- **Aluno**  
  Participa ativamente dos projetos. Busca uma plataforma intuitiva e interativa.

- **Pais/Responsáveis**  
  Acompanham o progresso dos filhos. Precisam de informações claras e atualizações regulares.

- **Especialista Externo**  
  Colabora com conhecimento prático. Precisa de orientações claras e integração com a equipe.

- **Coordenador Pedagógico**  
  Garante o alinhamento pedagógico. Precisa de visão global e dados para avaliar resultados.

## Técnica de Priorização: WSJF + MoSCoW

<div style="text-align: justify">
No projeto EduConnect, a priorização das funcionalidades foi feita combinando dois métodos: WSJF e MoSCoW. Essa abordagem permite tomar decisões mais estratégicas sobre o que desenvolver primeiro, levando em conta impacto, custo e urgência.
</div>

#### 1. WSJF – *Weighted Shortest Job First*

O WSJF (Trabalho Ponderado mais Curto Primeiro) é uma técnica usada para priorizar tarefas com base em três fatores:

- **CoD (Custo do Atraso):** representa o impacto financeiro ou de oportunidade que a não implementação de uma funcionalidade pode causar.
- **CoR (Custo do Trabalho em Andamento):** considera os custos contínuos enquanto a tarefa estiver em execução (como esforço da equipe e manutenção).
- **Tamanho do Trabalho:** mede o esforço necessário para realizar a funcionalidade, com base em pontos (geralmente usando a sequência de Fibonacci: 1, 2, 3, 5, 8, 13...).

**Fórmula:**

WSJF = (CoD + CoR) / Tamanho do Trabalho

Quanto maior o WSJF, mais vantajoso é realizar aquela funcionalidade primeiro.

#### 2. Critério MoSCoW

Após calcular o WSJF, as funcionalidades são classificadas com base no modelo **MoSCoW**, que divide as demandas em quatro categorias:

- 🔴 **Must Have (Essenciais):**  
  `WSJF > 2.0`  
  Funcionalidades indispensáveis para o funcionamento mínimo do produto (MVP). Sem elas, o sistema não opera.

- 🟢 **Should Have (Importantes):**  
  `1.0 ≤ WSJF ≤ 2.0`  
  Funcionalidades importantes que aumentam a eficiência, mas não são críticas. São priorizadas para uma próxima versão (Release 2.0).

- 🔵 **Could Have (Desejáveis):**  
  `WSJF < 1.0`  
  Funcionalidades que agregam valor ou diferencial competitivo, mas que só serão incluídas se houver tempo e recursos (Release 3.0).

- 🟡 **Won’t Have (Não essenciais neste momento):**  
  Funcionalidades que não serão desenvolvidas nesta fase. Podem ser consideradas no futuro ou descartadas