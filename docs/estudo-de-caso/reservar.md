# HopeBridge – Especificação de Caso de Uso: Reservar Vaga em Abrigo

## 1. Reservar Vaga em Abrigo

### 1.1 Breve Descrição
Este caso de uso permite ao usuário refugiado reservar vagas disponíveis em abrigos cadastrados na plataforma. Para isso, é possível visualizar abrigos com base na localização atual ou filtrando por região, verificar detalhes dos abrigos e, então, efetuar a solicitação de reserva.

A reserva só será concluída se:
- houver vaga disponível,
- o perfil estiver completo,
- e não existir outra reserva ativa no mesmo período.

A visualização no mapa é uma funcionalidade opcional estendida.

### 1.2 Atores
Refugiado

---

## 2. Fluxo de Eventos

### 2.1 Fluxo Básico/Principal
Este caso de uso é iniciado quando o usuário escolhe a opção **Reservar Vaga em Abrigo**.

2.1.1 O sistema apresenta a listagem de abrigos disponíveis com informações básicas (localização, tipo, vagas).  
2.1.2 O usuário aplica filtros como localização, tipo de abrigo ou necessidades específicas.  
2.1.3 O sistema exibe os resultados da filtragem.  
2.1.4 O usuário seleciona um dos abrigos listados.  
2.1.5 O sistema exibe os detalhes do abrigo: endereço, regras, número de vagas, etc.  
2.1.6 O usuário solicita a reserva da vaga.  
2.1.7 O sistema valida a solicitação de reserva [RN01][FE01].  
2.1.8 O sistema confirma a reserva e atualiza a quantidade de vagas disponíveis.  
2.1.9 O sistema exibe mensagem de ação realizada com sucesso.  
2.1.10 O caso de uso é encerrado.

---

### 2.2 Fluxos Alternativos

#### 2.2.1 [FA01] Selecionar Outro Abrigo  
No passo 2.1.5 do fluxo básico o usuário decide não continuar com o abrigo selecionado.

2.2.1.1 O sistema retorna à lista de abrigos disponíveis.  
2.2.1.2 O fluxo segue a partir do passo 2.1.3.

#### 2.2.2 [FA02] Acessar Mapa Interativo  
No passo 2.1.1 do fluxo básico o usuário opta por visualizar abrigos através do mapa.

2.2.2.1 O sistema solicita o acesso à localização do usuário [RNF01][FA03].  
2.2.2.2 O usuário autoriza o acesso à sua localização atual.  
2.2.2.3 O sistema exibe o mapa interativo centralizado na localização do usuário, destacando os abrigos disponíveis.  
2.2.2.4 O usuário seleciona um dos abrigos exibidos.  
2.2.2.5 O fluxo segue a partir do passo 2.1.5 do fluxo básico.

#### 2.2.3 [FA03] Acessar Mapa Interativo sem Acesso à Localização em Tempo Real  
No passo 2.2.2.1 do FA02 o usuário não autoriza o sistema a acessar sua localização.

2.2.3.1 O sistema apresenta a opção de seleção manual por região/país.  
2.2.3.2 O sistema exibe o mapa interativo com base em um ponto genérico da região selecionada, destacando os abrigos disponíveis.  
2.2.3.3 O usuário seleciona um dos abrigos disponíveis.  
2.2.3.4 O fluxo segue a partir do passo 2.1.5 do fluxo básico.

---

### 2.3 Fluxos de Exceção

#### 2.3.1 [FE01] Falha na Validação da Solicitação  
No passo 2.1.7 do fluxo básico, o sistema identifica que:

- não há vagas disponíveis,  
- o perfil do usuário está incompleto, ou  
- já existe uma reserva ativa para o mesmo período.

2.3.1.1 O sistema exibe mensagem informando a falha na reserva.  
2.3.1.2 O sistema retorna ao passo 2.1.3 para nova seleção.

---

## 3. Pré-Condições

### 3.1 Login  
Para utilizar este caso de uso, é necessário que o usuário refugiado esteja autenticado na plataforma.

### 3.2 Perfil Completo  
O perfil do usuário deve estar completo com todos os dados obrigatórios preenchidos.

---

## 4. Pós-Condições

### 4.1 Registro de Operações  
A operação de reserva deve ser registrada, incluindo informações como: quem realizou a ação, em qual abrigo, e em que horário.

### 4.2 Atualização de Vagas  
O número de vagas disponíveis no abrigo é atualizado imediatamente após a reserva.

---

## 5. Requisitos Especiais

### 5.1 [RNF01] Dispositivo Móvel  
Este caso de uso deve ser acessível via dispositivos móveis com Android versão 7.0 ou superior.

### 5.2 [RNF02] Múltiplos Idiomas  
Este caso de uso deve incluir suporte para os idiomas árabe e inglês.

### 5.3 Tempo Real  
A atualização da quantidade de vagas disponíveis deve ocorrer em tempo real para evitar conflitos ou reservas inválidas.

---

## 6. Regras de Negócio

### 6.1 [RN01] Validação de Reserva  
A reserva somente será concluída se:

- houver vaga disponível no abrigo selecionado,  
- o usuário estiver com perfil completo e válido,  
- não houver outra reserva ativa para o mesmo período.

### 6.2 Expiração da Reserva  
Reservas têm validade de 24 horas e podem ser automaticamente canceladas caso não sejam confirmadas pelo abrigo.

---

[Retornar para Casos de Uso](casos_de_uso.md)