# Product Backlog Building

## Empresa HealthNet

<div style="text-align: justify"> A HealthNet é uma ampla rede de clínicas e hospitais distribuídos por diversos estados que enfrenta desafios significativos na gestão de dados de pacientes e na integração de processos clínicos e administrativos. Diante de sistemas legados isolados e ineficiências em agendamentos, prontuários e controle de medicamentos, o negócio busca oferecer uma plataforma unificada e segura que conecte as diferentes unidades, facilite o acesso imediato a informações completas do paciente, automatize verificações de prescrições e interações medicamentosas, e otimize fluxos de trabalho para recepcionistas, médicos, farmacêuticos e coordenadores. Além de melhorar a experiência do paciente com portais de autoatendimento e notificações, a solução visa garantir conformidade com regulamentações de privacidade e permitir relatórios consolidados para a tomada de decisões estratégicas pela diretoria de tecnologia, promovendo maior eficiência operacional, redução de erros e melhor qualidade no atendimento à saúde.</div>

## Canvas do PBB

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVIlN5Oxg=/?embedMode=view_only_without_ui&moveToViewport=-13358,-12556,33280,16059&embedId=530780821800" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

---

## Personas

- **Maria - A Recepcionista**<br>
  Registra e atualiza as informações dos pacientes. Precisa de acesso rápido a informações de pacientes de outras unidades e capacidade de registro e atualização de pacientes sem atrasos.

- **Dr. João - O Médico Clínico Geral**<br>
  Atende os pacientes. Precisa de acesso rápido ao histórico médico, prescrições e exames.

- **Lívia - A Farmacêutica**<br>
  Dispensa medicamentos. Precisa um sistema à prova de erros e que ofereça informações detalhadas sobre medicamentos.

- **Rafael - O Coordenador de Agendamento**<br>
  Gerencia o agendamento de consultas para os médicos da clínica. Precisa de um sistema que evite conflitos e otimize a agenda dos médicos.

- **Sra. Clara - A Paciente**<br>
  Visita a HealthNet para check-ups e tratamento. Precisa de um portal para ver seu histórico médico, agendar consultas e acessar resultados de exames.

- **Sr. Roberto - Diretor de Tecnologia**<br>
  Supervisiona a infraestrutura tecnológica da HealthNet. Precisa de uma solução com ferramentas de monitoramento e relatórios.

## Técnica de Priorização: COORG

<div style="text-align: justify">
No projeto HealthNet, a priorização foi feita a partir da utilização do método COORG, que avalia os Product Backlog Items - PBI - pela suas pontuações em <b>Frequência de Uso</b> e seu <b>Valor de Negócio</b>, que são posteriormente somadas.
</div>

### 1. Frequência de Uso

A frequência de uso é determinada com uma <b>nota de 1 à 5</b>, que varia conforme a descrição abaixo:

- **(5) Hora a Hora:** utilizado mais de uma vez ao dia.
- **(4) Diário:** utilizado uma vez no dia, pelo menos.
- **(3) Semanal:** utilizado uma, duas ou três vezes na semana.
- **(2) Mensal:** utilizado uma vez no mês, ou pouco mais de uma vez.
- **(1) Trimestral:** utilizado, pelo menos, uma vez a cada 3 meses.

### 2. Valor de Negócio

Já o valor de negócio é determinado com uma <b>nota de 1 à 3</b>, que varia conforme descrição abaixo:

- **(3) Alto:** muito importante, principal, algo com um valor de negócio alto.
- **(2) Médio:** algo que tem relevância, um valor de negócio médio.
- **(1) Baixo:** algo que faz sentido, mas que não agrega muito valor no
  momento atual, um valor de negócio baixo.

## Behavior Driven Development (BDD)

Após a priorização dos <b>Product Backlog Items</b> e <b>User Stories</b>, utilizamos do BDD para descrever o comportamento esperado das funcionalidades-chave em cenários claros, trazendo mais à tona a realidade de uso da funcionalidade. Divido em:

- **"Dado que ...":** se refere ao contexto inicial.
- **"Quando ...":** se refere a algum evento ou ação.
- **"Então ...":** se refere ao resultado esperado.

<pre>
<code>
<span style="color: yellow;">Funcionalidade</span>: Registrar novos pacientes

<span style="color: green;">Cenário</span>: A recepcionista registra um novo paciente na recepção
    <span style="color: orange;">Dado</span> que a recepcionista está registrando o paciente utilizando o sistema,
    <span style="color: orange;">Quando</span> ela preenche os dados do novo paciente,
    <span style="color: orange;">Então</span> o paciente deve ser adicionado ao sistema e o tempo de espera na recepção deve ser reduzido.
</code>
</pre>

Assim, além de auxiliar no desenvolvimento orientado a testes, o BDD contribui com documentação viva do produto, mantendo os requisitos sempre atualizados e compreensíveis.
