# HopeBridge - Especificação de Caso de Uso: Cadastrar Perfil

## 1. Cadastrar Perfil

### 1.1 Breve Descrição
Este caso de uso permite ao refugiado realizar seu registro inicial na plataforma HopeBridge,  
informando dados pessoais (nome completo, data de nascimento, número de telefone), composição  
familiar (número de membros) e idioma de preferência. A criação do usuário é necessária para  
utilização dos outros serviços da plataforma.

### 1.2 Atores
● Refugiado

---

## 2. Fluxo de Eventos

### 2.1 Fluxo Básico/Principal
O caso de uso inicia quando o refugiado seleciona “Criar Perfil” na tela de boas-vindas.

2.1.1 O sistema apresenta o formulário de cadastro solicitando os dados pessoais (nome completo,  
data de nascimento, número de telefone, composição familiar e idioma de preferência). [RNF02]  
2.1.2 O usuário preenche todos os campos do formulário e clica em “Confirmar”. [FE01]  
2.1.3 O sistema envia um pedido de confirmação ao telefone do usuário.  
2.1.5 O usuário clica em “Confirmar cadastro” no telefone. [FE02]  
2.1.6 O sistema exibe a mensagem “Cadastro realizado com sucesso” e redireciona o usuário à tela  
de login.  
2.1.7 O caso de uso é encerrado.

---

### 2.3 Fluxos de Exceção

#### 2.3.1 [FE01] Dados não confirmados  
No passo 2.1.2, se o usuário não confirmar as informações de cadastro, o sistema retorna ao passo  
2.1.1.

#### 2.3.2 [FE02] Código não confirmado  
No passo 2.1.5, se o código de confirmação não for confirmado dentro de 5 minutos, o sistema  
retorna ao passo 2.1.1.

---

## 3. Pré-Condições
Não há nenhuma pré-condição para a execução deste caso de uso.

---

## 4. Pós-Condições
Ao final deste caso de uso, o cadastro do usuário deve ser registrado, com o objetivo de tornar  
possível que ele realize o login na plataforma.

---

## 5. Requisitos Especiais

### 5.1 [RNF01] Dispositivo Móvel  
Este caso de uso deve ser acessível via dispositivo móvel, o qual utiliza o Android a partir da versão  
7.0.

### 5.2 [RNF02] Múltiplos Idiomas  
Este caso de uso deve incluir suporte para os idiomas árabe e inglês.

---

[Retornar para Casos de Uso](casos_de_uso.md)