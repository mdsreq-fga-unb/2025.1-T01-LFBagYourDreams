# Especificação de Casos de Uso

## Especificação de Caso de Uso: Gerenciar Recursos

### 1. Breve Descrição
Este caso de uso permite à Agência Humanitária gerenciar, monitorar e distribuir recursos  
de forma eficiente dentro da plataforma HopeBridge. Inclui funcionalidades para cadastrar  
novos recursos, atualizar informações de recursos existentes, visualizar o status dos  
recursos disponíveis e gerar relatórios de impacto sobre a distribuição.

### 2. Ator Principal
● Agência Humanitária

### 3. Fluxo de Eventos

#### 3.1 Fluxo Básico/Principal  
Este caso de uso é iniciado quando a Agência Humanitária acessa a funcionalidade de  
Gerenciar Recursos no sistema.

3.1.1. A Agência Humanitária acessa o módulo "Gerenciar Recursos".  
3.1.2. O sistema exibe um painel com a visão geral dos recursos cadastrados e seu status  
atual.  
3.1.3. A Agência Humanitária seleciona a opção para adicionar um novo recurso.  
3.1.4. O sistema apresenta um formulário para preenchimento das informações do recurso  
(ex: tipo de recurso, quantidade, localização, data de validade).  
3.1.5. A Agência Humanitária preenche os detalhes do recurso e confirma o cadastro.  
3.1.6. [RN01] O sistema valida as informações inseridas e registra o novo recurso.  
3.1.7. O sistema exibe uma mensagem de sucesso confirmando o cadastro do recurso.  
3.1.8. O caso de uso é encerrado.

#### 3.2 Fluxos Alternativos

● 3.2.1 [FA01] Atualizar Informações de Recurso  
No passo 3.1.3 do Fluxo Básico, a Agência Humanitária seleciona um recurso  
existente para atualização.

3.2.1.1. A Agência Humanitária busca o recurso desejado (ex: por nome, ID ou tipo).  
3.2.1.2. O sistema exibe os detalhes do recurso selecionado.  
3.2.1.3. A Agência Humanitária modifica as informações necessárias (ex:  
quantidade, localização, status).  
3.2.1.4. A Agência Humanitária confirma as alterações.  
3.2.1.5. [RN01] O sistema valida as alterações e atualiza o registro do recurso.  
3.2.1.6. O sistema exibe uma mensagem de sucesso.  
3.2.1.7. O fluxo segue a partir do passo 3.1.2 do fluxo básico ou é encerrado.

● 3.2.2 [FA02] Visualizar Relatórios de Recursos  
No passo 3.1.2 do Fluxo Básico, a Agência Humanitária seleciona a opção para gerar  
relatórios.

3.2.2.1. O sistema apresenta opções de filtros para geração de relatórios (ex:  
período, tipo de recurso, localização, pessoas atendidas).  
3.2.2.2. A Agência Humanitária seleciona os filtros desejados e solicita a geração do  
relatório.  
3.2.2.3. O sistema processa os dados e exibe o relatório com as métricas e  
informações solicitadas sobre a distribuição e impacto dos recursos.  
3.2.2.4. A Agência Humanitária pode exportar ou imprimir o relatório.  
3.2.2.5. O caso de uso é encerrado.

● 3.2.3 [FA03] Inativar Recurso  
No passo 3.1.3 do Fluxo Básico, a Agência Humanitária seleciona um recurso para  
inativação.

3.2.3.1. A Agência Humanitária busca e seleciona o recurso a ser inativado.  
3.2.3.2. O sistema solicita confirmação para inativar o recurso.  
3.2.3.3. [RN02] A Agência Humanitária confirma a inativação.  
3.2.3.4. O sistema altera o status do recurso para "inativo" e o remove da lista de  
recursos disponíveis para alocação.  
3.2.3.5. O sistema exibe uma mensagem de sucesso.  
3.2.3.6. O caso de uso é encerrado.

#### 3.3 Fluxos de Exceção

● 3.3.1 [FE01] Informações de Recurso Inválidas  
No passo 3.1.6 do Fluxo Básico (ou passo 3.2.1.5 do FA01), caso a Agência  
Humanitária insira informações incompletas ou inválidas no formulário de  
cadastro/atualização.

3.3.1.1. O sistema exibe uma mensagem de erro indicando os campos que precisam  
ser corrigidos.  
3.3.1.2. O caso de uso retorna ao passo anterior (passo 3.1.4 do FB ou passo  
3.2.1.3 do FA01) para que a Agência Humanitária possa corrigir as informações.

● 3.3.2 [FE02] Recurso Não Encontrado  
No passo 3.2.1.1 do FA01 ou 3.2.3.1 do FA03, caso a Agência Humanitária tente  
buscar um recurso que não está cadastrado ou não existe no sistema.

3.3.2.1. O sistema exibe uma mensagem informando que o recurso não foi  
encontrado.  
3.3.2.2. O caso de uso retorna ao passo inicial do fluxo alternativo (passo 3.2.1.1 do  
FA01 ou 3.2.3.1 do FA03).

---

### 4. Pré-Condições

4.1. A Agência Humanitária deve estar "logada" na aplicação.

---

### 5. Pós-Condições

5.1. Ao final deste caso de uso, as operações realizadas (cadastro, atualização, inativação  
de recursos) devem ser registradas no sistema, com o objetivo de tornar possível a  
recuperação de informações sobre quem realizou quais operações e quando.  
5.2. O sistema deve refletir as informações atualizadas dos recursos.

---

### 6. Regras de Negócio (RN)

6.1. [RN01] Validação de Recursos: As informações inseridas ou atualizadas no formulário  
de recursos (tipo de recurso, quantidade, localização, data de validade) devem ser válidas e  
completas para que o sistema possa registrá-las.  
6.2. [RN02] Inativação de Recurso: A inativação de um recurso deve ser confirmada pela  
Agência Humanitária antes de ser efetivada, e o recurso inativado não deve mais aparecer  
nas listas de recursos disponíveis.

---

[Retornar para Casos de Uso](casos_de_uso.md)