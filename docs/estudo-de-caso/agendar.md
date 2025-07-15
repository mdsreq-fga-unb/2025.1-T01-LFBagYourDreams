# HopeBridge - Especificação de Caso de Uso: Agendar Consulta Médica

## 1. Agendar Consulta Médica

### 1.1 Breve Descrição
Este caso de uso permite ao usuário agendar consulta médica em uma unidade de atendimento próxima à sua região. Para tanto, é possível que seja realizada a listagem das unidades de atendimento disponíveis, a visualização das unidades de atendimento disponíveis através de mapa interativo, a especificação dos horários de atendimento disponíveis, e o agendamento de consulta em determinada unidade e horário. Uma consulta agendada não poderá ser desmarcada.

### 1.2 Atores
Refugiado

## 2. Fluxo de Eventos

### 2.1 Fluxo Básico/Principal
Este caso de uso é iniciado quando o usuário escolher a opção Agendar Consulta Médica.

2.1.1 O sistema apresenta as seguintes opções:  
Ver unidades de atendimento disponíveis  
Acessar mapa interativo [FA01].

2.1.2 O usuário refugiado seleciona a opção para a visualização das unidades de atendimento disponíveis.

2.1.3 O sistema solicita o acesso à localização do usuário [RNF02][FA02].

2.1.4 O usuário refugiado autoriza o acesso à sua localização atual.

2.1.5 O sistema exibe as unidades de atendimento disponíveis próximas à localização do usuário.

2.1.6 O usuário refugiado seleciona uma das unidades de atendimento disponíveis.

2.1.7 O sistema apresenta os serviços de atendimento disponíveis para a unidade selecionada.

2.1.8 O usuário refugiado seleciona um dos serviços de atendimento disponíveis para a unidade selecionada [RN01].

2.1.9 O sistema apresenta os horários de atendimento disponíveis para a unidade selecionada.

2.1.10 O usuário refugiado seleciona um dos horários disponíveis.

2.1.11 O sistema pergunta ao usuário se o mesmo, realmente, deseja agendar uma consulta médica; e indica que a ação não poderá ser desfeita.

2.1.12 O usuário refugiado confirma o agendamento [FE01].

2.1.13 O sistema exibe mensagem de ação realizada com sucesso.

2.1.14 O caso de uso é encerrado.

### 2.2 Fluxos Alternativos

#### 2.2.1 [FA01] Acessar Mapa Interativo  
No passo 2.2.1 do fluxo básico o usuário refugiado seleciona a opção para acessar o mapa interativo.

2.2.1.1 O sistema solicita o acesso à localização do usuário [RNF02][FA03].

2.2.1.2 O usuário refugiado autoriza o acesso à sua localização atual.

2.2.1.3 O sistema exibe o mapa interativo centralizado na atual localização do usuário refugiado, destacando as unidades de atendimento próximas disponíveis.

2.2.1.4 O usuário refugiado seleciona uma das unidades de atendimento disponíveis.

2.2.1.5 O fluxo segue a partir do passo 2.1.7 do fluxo básico.

#### 2.2.2 [FA02] Agendamento de Consulta sem Acesso à Localização em Tempo Real  
No passo 2.1.3 do fluxo básico o usuário não autoriza ao sistema o acesso à sua localização em tempo real.

2.2.2.1 O sistema exibe uma listagem de todas as unidades de atendimento disponíveis e filtros por região/país.

2.2.2.2 O usuário seleciona o filtro correspondente a sua região.

2.2.2.3 O sistema exibe os resultados da filtragem de região.

2.2.2.4 O usuário refugiado seleciona uma das unidades de atendimento disponíveis.

2.2.2.5 O fluxo segue a partir do passo 2.1.7 do fluxo básico.

#### 2.2.3 [FA03] Acessar Mapa Interativo sem Acesso à Localização em Tempo Real  
No passo 2.2.1.1 do FA01 o usuário não autoriza ao sistema o acesso à sua localização em tempo real.

2.2.3.1 O sistema apresenta ao usuário a opção de selecionar por determinada região/país.

2.2.3.2 O sistema exibe o mapa interativo a partir de um ponto genérico dentro dos limites territoriais estabelecidos para a região selecionada pelo usuário, destacando as unidades de atendimento próximas disponíveis.

2.2.3.3 O usuário refugiado seleciona uma das unidades de atendimento disponíveis.

2.2.3.4 O fluxo segue a partir do passo 2.1.7 do fluxo básico.

### 2.3 Fluxos de Exceção

#### 2.3.1 [FE01] Ações não Confirmadas  
No passo 2.1.10 o usuário não confirma o agendamento de atendimento médico.  
O sistema retorna ao passo 2.1.8.

---

## 3. Pré-Condições

### 3.1 Login  
Para utilizar este caso de uso, é necessário que o usuário refugiado esteja “logado” na aplicação.

---

## 4. Pós-Condições

### 4.1 Registro de Operações  
Ao final deste caso de uso, as operações realizadas devem ser registradas, com o objetivo de tornar possível a recuperação de informações sobre quem realizou quais operações e quando.

---

## 5. Requisitos Especiais

### 5.1 [RNF01] Dispositivo Móvel  
Este caso de uso deve ser acessível via dispositivo móvel, o qual utiliza o Android a partir da versão 7.0.

### 5.2 [RNF02] Acesso à localização em tempo real 
Este caso de uso deve ser capaz de obter a localização em tempo real do usuário a partir de seu dispositivo móvel.

### 5.3 [RNF03] Múltiplos Idiomas  
Este caso de uso deve incluir suporte para os idiomas árabe e inglês.

---

## 6. Regras de Negócio

### 6.1 [RN01] Serviços de atendimento disponíveis
A seguinte validação de serviços de atendimento disponíveis nas unidades de atendimento deve ser realizada:

| Nome         | Código            | Obrigatoriedade           |
|------------------|----------------------|--------------------|
| Clínica médica  | 1      | -    |
| Pediatria  | 2      | -    |
| Ginecologia  | 3      | -    |
| Obstetrícia  | 4      | -    |
| Ortopedia  | 5      | -    |
| Oftalmologia  | 6      | -    |
| Cirurgia geral  | 7      | -    |

[Retornar para Casos de Uso](casos_de_uso.md)