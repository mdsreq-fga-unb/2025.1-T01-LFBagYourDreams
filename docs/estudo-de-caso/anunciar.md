# Caso de Uso: Anunciar Vaga de Trabalho

## 1. Breve Descrição

1.1 Este caso de uso permite que empregadores parceiros anunciem vagas de trabalho na plataforma HopeBridge, tornando-as visíveis para refugiados cadastrados.  
O processo envolve o preenchimento de informações detalhadas sobre a vaga, como título, descrição, local, requisitos, carga horária e remuneração (quando aplicável).  
O sistema também permite salvar rascunhos e acompanhar o status das vagas anunciadas.

## 1.2 Atores

- Empregador

---

## 2. Fluxo de Eventos

### 2.1 Fluxo Básico/Principal

2.1.1 O empregador acessa a opção “Anunciar Vaga de Trabalho”.  
2.1.2 O sistema apresenta formulário com os seguintes campos obrigatórios:
- Título da vaga  
- Área de atuação  
- Descrição da vaga  
- Requisitos  
- Local de trabalho (presencial, remoto ou híbrido)  
- Horário e carga horária  
- Remuneração (opcional)

2.1.3 O empregador preenche as informações da vaga.  
2.1.4 O sistema valida os dados preenchidos e alerta sobre eventuais campos obrigatórios não preenchidos [FE01].  
2.1.5 O sistema solicita confirmação para publicação da vaga, oferecendo a opção de Salvar como Rascunho [FA01].  
2.1.6 O empregador confirma a publicação.  
2.1.7 O sistema registra a vaga e exibe mensagem de confirmação de sucesso.  
2.1.8 A vaga é publicada e passa a estar visível para os refugiados na plataforma.  
2.1.9 O caso de uso é encerrado.

---

### 2.2 Fluxos Alternativos

#### 2.2.1 [FA01] Salvar Vaga como Rascunho

2.2.1.1 O empregador opta por salvar a vaga como rascunho.  
2.2.1.2 O sistema salva os dados preenchidos em estado de rascunho.  
2.2.1.3 O sistema exibe mensagem de confirmação de que a vaga foi salva como rascunho.  
2.2.1.4 O caso de uso é encerrado.

#### 2.2.2 [FA02] Publicar Vaga Salva como Rascunho

2.2.2.1 O empregador escolhe publicar uma vaga salva como rascunho.  
2.2.2.2 O sistema carrega os dados da vaga selecionada.  
2.2.2.3 O empregador pode revisar e modificar os campos.  
2.2.2.4 O sistema valida os dados preenchidos [RN01][FE01].  
2.2.2.5 O sistema solicita confirmação para a publicação.  
2.2.2.6 O empregador confirma a publicação [FE02].  
2.2.2.7 O sistema registra a vaga e exibe mensagem de sucesso.  
2.2.2.8 A vaga passa a estar visível para os refugiados.  
2.2.2.9 O caso de uso é encerrado.

#### 2.2.3 [FA03] Edição de Vaga Publicada

2.2.3.1 O empregador escolhe editar uma vaga publicada.  
2.2.3.2 O sistema exibe os dados para edição.  
2.2.3.3 O empregador modifica os campos desejados.  
2.2.3.4 O sistema valida os dados preenchidos [RN01][FE01].  
2.2.3.5 O sistema solicita confirmação para atualizar a vaga.  
2.2.3.6 O empregador confirma a atualização [FE02].  
2.2.3.7 O sistema salva as alterações e exibe mensagem de sucesso.  
2.2.3.8 O caso de uso é encerrado.

---

### 2.3 Fluxos de Exceção

#### 2.3.1 [FE01] Dados Incompletos ou Inválidos

2.3.1.1 O sistema detecta ausência ou erro em campos obrigatórios.  
2.3.1.2 Destaca os campos com erro e exibe mensagens explicativas.  
2.3.1.3 O fluxo retorna ao passo de correção (2.1.2 ou 2.2.3.2) para novo envio.

#### 2.3.2 [FE02] Ações Não Confirmadas

2.3.2.1 O empregador não confirma publicação/atualização.  
2.3.2.2 O sistema retorna ao passo anterior de confirmação (2.1.4, 2.2.2.4 ou 2.2.3.4).

---

## 3. Pré-Condições

3.1 O empregador deve estar autenticado com perfil autorizado para anunciar vagas.

---

## 4. Pós-Condições

4.1 Publicação da Vaga  
Ao final deste caso de uso, a vaga será publicada no sistema e poderá ser consultada por refugiados que atendam aos critérios de busca.

4.2 Vaga Salva como Rascunho  
Se o empregador optar por salvar como rascunho, a vaga ficará armazenada em estado de rascunho, não visível para os refugiados, e poderá ser acessada e editada posteriormente pelo empregador.

---

## 5. Requisitos Especiais

5.1 **[RNF01] Acessibilidade Móvel**  
Este caso de uso deve ser acessível via dispositivo móvel com sistema Android a partir da versão 7.0.

5.2 **[RNF02] Múltiplos Idiomas**  
O sistema deve apresentar suporte para os idiomas árabe e inglês.

5.3 **Armazenamento Offline**  
Empregadores com acesso intermitente à internet poderão salvar vagas como rascunho offline, sincronizando os dados quando houver conectividade.

---

## 6. Regras de Negócio

### 6.1 [RN01] Validação de Informações

| Nome                    | Formato                 | Obrigatoriedade | Valores                            |
|-------------------------|-------------------------|------------------|-------------------------------------|
| Título da Vaga          | Texto até 100 caracteres | Sim              |                                     |
| Área de Atuação         | Texto até 50 caracteres  | Sim              | Ex: TI, Saúde, Construção           |
| Descrição da Vaga       | Texto livre              | Sim              |                                     |
| Requisitos              | Texto livre              | Sim              |                                     |
| Local de Trabalho       | Seleção Múltipla         | Sim              | Presencial; Remoto; Híbrido         |
| Horário e Carga Horária | Texto até 100 caracteres | Sim              | Ex: 8h às 17h, 40h semanais         |
| Remuneração             | Numérico (decimal)       | Não              | Ex: 1500.00                         |


---

[Retornar para Casos de Uso](casos_de_uso.md)