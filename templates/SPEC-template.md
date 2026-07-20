# Project Specification

<!--
Substitua este título pelo nome do projeto ou da funcionalidade.

Esta SPEC descreve o comportamento esperado do sistema.
Ela deve explicar o que será construído, não como será implementado.

Remova exemplos que não forem relevantes, mas mantenha as seções obrigatórias.
-->

## Metadata

* **Project:** `<project-name>`
* **Status:** `draft`
* **Stage:** `now`

<!--
Status permitidos:

- draft: especificação ainda incompleta ou em discussão;
- ready: especificação validada e pronta para implementação;
- implemented: comportamento especificado já foi implementado;
- superseded: especificação substituída por uma versão ou decisão posterior.

Stage permitidos:

- now: projeto ou funcionalidade em foco;
- then: próximo trabalho planejado;
- later: trabalho futuro.

Código de produção não deve ser implementado enquanto o Status estiver como draft.
-->

## Problem

<!--
Descreva o problema real que motivou o projeto.

Procure responder:

- Qual dificuldade existe hoje?
- Quem enfrenta essa dificuldade?
- Como essa pessoa resolve o problema atualmente?
- Por que a solução atual é insuficiente?
- Com que frequência o problema acontece?

Evite começar descrevendo a solução técnica.
-->

[Descreva o problema.]

## Target User

<!--
Identifique quem usará o sistema.

O usuário pode ser o próprio autor do projeto, mas isso deve ser explícito.

Procure responder:

- Quem é o usuário principal?
- Em qual contexto ele usará o sistema?
- Qual conhecimento técnico pode ser esperado?
- O usuário é diferente de quem mantém o código?
-->

**Primary user:** [Descreva o usuário principal.]

**Usage context:** [Descreva quando e por que o sistema será usado.]

## Goal

<!--
Descreva o resultado principal que esta versão deve alcançar.

O objetivo deve ser pequeno, observável e verificável.

Evite objetivos vagos como:

- melhorar a experiência;
- usar IA para analisar dados;
- criar um aplicativo completo.

Prefira algo como:

- transformar uma entrada sintética em um JSON estruturado;
- gerar combinações válidas a partir de regras explícitas;
- identificar o próximo livro de uma série usando um catálogo local.
-->

[Descreva o objetivo desta versão.]

## Scope

<!--
Liste somente as capacidades incluídas nesta versão.

Cada item deve representar algo que poderá ser validado por critério de aceite,
cenário ou teste.

Evite incluir funcionalidades futuras.
-->

Esta versão inclui:

* [Capacidade incluída.]
* [Capacidade incluída.]
* [Capacidade incluída.]

## Non-goals

<!--
Registre explicitamente o que não será construído nesta versão.

Non-goals, ou escopo negativo, evitam que o projeto cresça silenciosamente.

Inclua funcionalidades tentadoras que tenham sido deliberadamente adiadas.
-->

Esta versão não inclui:

* [Funcionalidade fora do escopo.]
* [Integração fora do escopo.]
* [Automação fora do escopo.]

## Inputs

<!--
Descreva todas as entradas aceitas pelo sistema.

Para cada entrada, procure registrar:

- formato;
- origem;
- campos obrigatórios;
- campos opcionais;
- limites;
- encoding, unidade ou convenções relevantes;
- exemplo sintético.

Não use dados pessoais reais nos exemplos.
-->

### IN-001 — [Nome da entrada]

**Description:** [O que esta entrada representa.]

**Format:** [JSON, CSV, texto, argumento de CLI etc.]

**Required fields:**

| Field        | Type     | Required | Description  |
| ------------ | -------- | -------: | ------------ |
| `field_name` | `string` |      yes | [Descrição.] |

**Constraints:**

* [Restrição da entrada.]
* [Restrição da entrada.]

**Synthetic example:**

```text
[Exemplo sintético de entrada.]
```

## Outputs

<!--
Descreva as saídas observáveis do sistema.

Para cada saída, registre:

- formato;
- campos;
- tipos;
- ordenação, quando relevante;
- precisão numérica;
- comportamento em caso de erro;
- exemplo esperado.

Não descreva estruturas internas que não sejam observáveis pelo consumidor.
-->

### OUT-001 — [Nome da saída]

**Description:** [O que a saída representa.]

**Format:** [JSON, CSV, texto, código de saída etc.]

**Schema:**

| Field        | Type     | Required | Description  |
| ------------ | -------- | -------: | ------------ |
| `field_name` | `string` |      yes | [Descrição.] |

**Synthetic example:**

```json
{
  "field_name": "synthetic value"
}
```

## Domain Concepts and Glossary

<!--
Defina os conceitos importantes do domínio usando linguagem consistente.

Use DDD de forma leve:

- identifique os conceitos que aparecem nas regras;
- explique o significado de cada termo;
- diferencie conceitos parecidos;
- não crie classes ou abstrações apenas porque estão neste glossário.

Os nomes técnicos usados no código e nos schemas devem ficar em inglês.
As explicações podem permanecer em português.
-->

### `[DomainConcept]`

[Explique o conceito e sua função dentro do problema.]

### `[AnotherDomainConcept]`

[Explique o conceito e como ele se diferencia dos demais.]

### Glossary

| Term               | Meaning                   |
| ------------------ | ------------------------- |
| `[technical_term]` | [Definição em português.] |

## Business Rules

<!--
Business rules são regras que determinam o comportamento do sistema.

Cada regra deve:

- receber um identificador;
- ser observável ou verificável;
- evitar detalhes de implementação;
- apontar ambiguidades quando existirem.

Exemplos:

- BR-001: O total de uma linha corresponde à quantidade multiplicada pelo preço unitário.
- BR-002: Itens sem preço não devem ser aceitos.
-->

### BR-001 — [Nome curto da regra]

[Descreva a regra.]

### BR-002 — [Nome curto da regra]

[Descreva a regra.]

## Invariants

<!--
Invariants são condições que nunca podem ser violadas em um estado válido do sistema.

Exemplos:

- valores monetários nunca podem ser negativos;
- uma saída válida sempre deve conter um identificador;
- uma série concluída não pode ter próximo livro pendente.

Uma invariant não descreve uma sequência de ações. Ela descreve uma condição
que deve continuar verdadeira.
-->

### INV-001 — [Nome curto da invariant]

[Descreva a condição que deve permanecer verdadeira.]

### INV-002 — [Nome curto da invariant]

[Descreva a condição que deve permanecer verdadeira.]

## Acceptance Criteria

<!--
Critérios de aceite definem as condições verificáveis para considerar esta
versão correta.

Cada critério deve:

- possuir um identificador AC-XXX;
- descrever comportamento observável;
- poder ser comprovado por um cenário ou teste;
- evitar termos subjetivos como rápido, intuitivo ou adequado sem uma métrica.

Não descreva como o código deve ser organizado.
-->

* **AC-001:** [Critério verificável.]
* **AC-002:** [Critério verificável.]
* **AC-003:** [Critério verificável.]

## Behavior Scenarios

<!--
Use cenários Given–When–Then para representar comportamentos importantes.

Given:
contexto e estado inicial.

When:
ação executada pelo usuário ou consumidor.

Then:
resultado observável.

Um cenário pode validar mais de um critério de aceite, mas deve ter um único
objetivo comportamental claro.

Os cenários ainda não são os testes executáveis. O HARNESS.md explicará como
cada cenário será comprovado com fixtures e testes.
-->

### SCN-001 — [Nome do cenário]

**Covers:** `AC-001`

**Given**

[Contexto inicial.]

**When**

[Ação executada.]

**Then**

[Resultado esperado.]

### SCN-002 — [Nome do cenário]

**Covers:** `AC-002`, `AC-003`

**Given**

[Contexto inicial.]

**When**

[Ação executada.]

**Then**

[Resultado esperado.]

## Invalid Inputs and Error Behavior

<!--
Descreva entradas inválidas e o comportamento esperado do sistema.

Não basta dizer que o sistema deve "gerar um erro".

Quando relevante, defina:

- condição que torna a entrada inválida;
- se o processamento deve parar;
- tipo ou código do erro;
- mensagem ou informação mínima;
- código de saída;
- possibilidade de processamento parcial;
- dados que não devem aparecer no erro.

Erros devem ser previsíveis e testáveis.
-->

### ERR-001 — [Nome do erro]

**Invalid condition:** [O que torna a entrada inválida.]

**Expected behavior:** [Como o sistema deve reagir.]

**Expected error:** `[error_identifier]`

**Related acceptance criteria:** `AC-XXX`

## Edge Cases

<!--
Edge cases são casos válidos ou plausíveis, mas incomuns.

Eles são diferentes de entradas inválidas.

Exemplos:

- quantidade decimal;
- arquivo vazio permitido;
- série com um único livro;
- aniversário em 29 de fevereiro;
- lista sem combinações possíveis.

Registre apenas casos relevantes para o escopo atual.
-->

### EDGE-001 — [Nome do caso extremo]

**Condition:** [Descreva a situação.]

**Expected behavior:** [Descreva o comportamento.]

### EDGE-002 — [Nome do caso extremo]

**Condition:** [Descreva a situação.]

**Expected behavior:** [Descreva o comportamento.]

## Privacy and Security

<!--
Avalie se o projeto envolve:

- documentos fiscais;
- informações financeiras;
- contatos;
- e-mails;
- aniversários;
- dados de saúde;
- identificadores pessoais;
- credenciais;
- tokens ou secrets;
- automações com efeito real.

O padrão do laboratório é usar dados sintéticos.

Descreva:

- quais dados são sensíveis;
- quais dados podem ser armazenados;
- quais dados não podem ser versionados;
- como exemplos reais devem ser anonimizados;
- quais ações exigem validação humana.

Se não houver risco relevante, registre isso explicitamente.
-->

**Sensitive data involved:** [yes | no]

**Risks:**

* [Risco identificado.]

**Required protections:**

* [Proteção necessária.]
* [Proteção necessária.]

**Human validation required for:**

* [Ação que exige revisão humana.]

## External Dependencies

<!--
Liste APIs, serviços, sites, bancos de dados, bibliotecas ou plataformas externas.

Na primeira versão, prefira que Required now? seja no.

Test substitute descreve como a dependência será substituída no harness:
fixture, mock, fake, stub ou catálogo local.

Não adicione uma dependência apenas porque ela pode ser útil no futuro.
-->

| ID        | Dependency     | Purpose       | Required now? | Test substitute                       |
| --------- | -------------- | ------------- | ------------: | ------------------------------------- |
| `DEP-001` | [Dependência.] | [Finalidade.] |            no | [Fixture, mock ou alternativa local.] |

## Assumptions

<!--
Assumptions são hipóteses aceitas temporariamente para permitir o avanço da SPEC.

Elas devem ser explícitas porque podem se provar incorretas quando o sistema
entrar em contato com dados reais.

Uma assumption não deve esconder uma decisão que já pode ser tomada.
-->

### ASM-001 — [Nome da hipótese]

[Descreva a hipótese e seu impacto.]

**Validation plan:** [Como essa hipótese poderá ser verificada futuramente.]

## Open Questions

<!--
Registre perguntas ainda sem resposta.

Uma pergunta aberta bloqueia a implementação quando sua resposta pode alterar:

- entradas;
- saídas;
- regras;
- invariants;
- critérios de aceite;
- contratos;
- riscos de privacidade;
- escopo da tarefa atual.

Uma SPEC pode permanecer como draft enquanto existirem perguntas bloqueantes.

Uma SPEC não deve mudar para ready enquanto houver pergunta bloqueante sem
resposta.
-->

### Q-001 — [Pergunta]

**Blocking:** `yes | no`

**Impact:** [O que pode mudar dependendo da resposta.]

**Resolution:** [Resposta ou decisão, quando existir.]

## Traceability

<!--
Relacione critérios de aceite, regras e cenários.

O HARNESS.md completará a rastreabilidade com fixtures, testes e comandos.

Não é necessário que toda regra tenha um cenário exclusivo, mas todo critério
de aceite deve ter uma forma explícita de validação.
-->

| Acceptance criterion | Related rules       | Scenarios |
| -------------------- | ------------------- | --------- |
| `AC-001`             | `BR-001`, `INV-001` | `SCN-001` |
| `AC-002`             | `BR-002`            | `SCN-002` |

## Specification Readiness Checklist

<!--
Todos os itens obrigatórios devem estar marcados antes de alterar o Status
de draft para ready.

Itens não aplicáveis podem ser marcados como N/A com uma justificativa curta.
-->

### Problem and scope

* [ ] O problema está descrito sem presumir uma solução técnica.
* [ ] O usuário principal está identificado.
* [ ] O objetivo desta versão é pequeno e observável.
* [ ] O escopo incluído está explícito.
* [ ] Os non-goals estão explícitos.
* [ ] O projeto continua dentro da fase definida no `ROADMAP.md`.

### Behavior

* [ ] As entradas estão definidas.
* [ ] As saídas estão definidas.
* [ ] Os conceitos principais do domínio estão descritos.
* [ ] As regras de negócio estão identificadas.
* [ ] As invariants relevantes estão identificadas.
* [ ] Os critérios de aceite são verificáveis.
* [ ] Todo critério de aceite possui ao menos um cenário relacionado.
* [ ] Existem cenários Given–When–Then para os comportamentos principais.
* [ ] Entradas inválidas possuem comportamento de erro definido.
* [ ] Casos extremos relevantes foram considerados.

### Safety and dependencies

* [ ] Os riscos de privacidade e segurança foram avaliados.
* [ ] Os exemplos usam somente dados sintéticos.
* [ ] Dependências externas foram identificadas.
* [ ] Dependências não essenciais foram adiadas ou substituídas.
* [ ] A necessidade de validação humana está explícita.

### Readiness

* [ ] As assumptions relevantes estão registradas.
* [ ] Não existem contradições conhecidas.
* [ ] Não existem perguntas abertas que bloqueiem a implementação.
* [ ] A rastreabilidade entre critérios, regras e cenários foi preenchida.
* [ ] O comportamento pode ser transformado em fixtures e testes.
* [ ] O `HARNESS.md` pode ser elaborado a partir desta SPEC.

## Specification Approval

<!--
Preencha esta seção somente depois de revisar o checklist.

A aprovação não precisa ser formal ou burocrática. Ela registra que a SPEC foi
deliberadamente considerada suficiente para iniciar a implementação.

Depois da aprovação:

1. altere Status de draft para ready;
2. crie ou revise o HARNESS.md;
3. implemente um cenário por vez;
4. registre mudanças de escopo antes de continuar.
-->

* **Reviewed by:** [Nome ou papel.]
* **Decision:** `approved | changes-required`
* **Notes:** [Observações da revisão.]
