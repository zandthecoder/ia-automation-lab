# Agent Task

<!--
Este template transforma uma parte pequena e validável da SPEC e do HARNESS
em uma tarefa concreta para um agente de programação.

Cada prompt deve ter um único objetivo principal.

O prompt preenchido deve ser específico o suficiente para que seja possível
responder:

- o que deve ser alterado;
- por que a alteração existe;
- quais arquivos podem ser modificados;
- qual comportamento será validado;
- quais comandos devem ser executados;
- em quais situações o agente deve parar.

Antes de enviar o prompt ao agente:

1. remova comentários e exemplos desnecessários;
2. substitua todos os placeholders;
3. remova seções que não se aplicam;
4. confirme que SPEC.md e HARNESS.md estão prontos;
5. confirme que os comandos de validação são conhecidos;
6. mantenha apenas um objetivo principal.
-->

## Task Metadata

* **Task ID:** `TASK-XXX`
* **Project:** `<project-name>`
* **Task:** `<short-task-name>`
* **Task type:** `<task-type>`
* **Related SPEC:** `projects/<project-name>/SPEC.md`
* **Related HARNESS:** `projects/<project-name>/HARNESS.md`

<!--
Tipos de tarefa permitidos:

- spec-review:
  revisar ou melhorar uma especificação antes da implementação;

- harness-design:
  definir fixtures, testes, comandos e estratégia de validação;

- fixture:
  criar ou atualizar dados sintéticos usados por testes;

- test:
  implementar testes para comportamentos já especificados;

- implementation:
  implementar o menor comportamento necessário para um teste existente;

- refactor:
  melhorar a estrutura sem alterar o comportamento observável;

- investigation:
  analisar uma dúvida técnica, reproduzir um problema ou comparar alternativas;

- documentation:
  criar ou atualizar documentação sem alterar comportamento.

Evite combinar tipos independentes em uma única tarefa.

Exemplo inadequado:

Task type: spec-review + implementation + refactor

Prefira dividir isso em tarefas separadas.
-->

## Context

<!--
Explique por que esta tarefa existe e qual é o estado atual.

Mantenha o contexto curto.

Faça referência aos arquivos e identificadores existentes, em vez de copiar
toda a SPEC ou todo o HARNESS.

Exemplo:

O cenário SCN-001 está especificado e o harness define FX-001, EXP-001 e
TEST-001. O teste e a implementação ainda não existem.
-->

[Descreva o contexto necessário para compreender a tarefa.]

## Objective

<!--
Defina um único objetivo principal, pequeno e observável.

Exemplo adequado:

Implementar o parsing do merchant para o cenário SCN-001.

Exemplo inadequado:

Criar o parser completo, melhorar a arquitetura, adicionar integração com QR
Code e preparar o dashboard.

Quando existirem dois objetivos que possam ser implementados e validados
independentemente, crie duas tarefas.
-->

[Descreva o único objetivo principal desta tarefa.]

## Required Reading

Antes de alterar qualquer arquivo, leia:

1. `/AGENTS.md`;
2. `projects/<project-name>/README.md`;
3. `projects/<project-name>/SPEC.md`;
4. `projects/<project-name>/HARNESS.md`;
5. [Arquivos diretamente relacionados à tarefa.]

<!--
Inclua DECISIONS.md quando a tarefa envolver:

- arquitetura;
- escopo;
- contratos;
- dependências;
- convenções persistentes;
- privacidade;
- segurança;
- decisões que afetem mais de um projeto.

Inclua ROADMAP.md quando houver risco de expandir a fase atual.

Não peça ao agente para ler todo o repositório sem necessidade.
-->

Leia também:

* `/DECISIONS.md`: `[required | not-required]`
* `/ROADMAP.md`: `[required | not-required]`

## Instruction Priority

<!--
Esta seção normalmente pode permanecer curta porque a prioridade global já
está definida em AGENTS.md.

Ela existe para deixar claro que este prompt não autoriza ignorar documentos
vigentes.
-->

Siga a ordem de prioridade definida em `/AGENTS.md`.

Esta tarefa complementa as instruções do repositório, mas não autoriza:

* ignorar a SPEC;
* ignorar o HARNESS;
* alterar decisões vigentes silenciosamente;
* expandir o escopo da fase;
* modificar arquivos protegidos;
* inventar comportamento não especificado.

Em caso de conflito, pare e relate o conflito antes de implementar.

## Specification References

<!--
Preencha somente os identificadores envolvidos nesta tarefa.

A rastreabilidade deve permitir seguir o caminho:

Acceptance criterion
→ scenario
→ rule or invariant
→ fixture
→ expected output
→ test
→ implementation

Use N/A somente quando a referência realmente não for aplicável.
-->

* **Acceptance criteria:** `AC-XXX`
* **Scenarios:** `SCN-XXX`
* **Business rules:** `BR-XXX`
* **Invariants:** `INV-XXX | N/A`
* **Errors:** `ERR-XXX | N/A`
* **Edge cases:** `EDGE-XXX | N/A`
* **Fixtures:** `FX-XXX | N/A`
* **Expected outputs:** `EXP-XXX | N/A`
* **Tests:** `TEST-XXX | N/A`

## Specification Gate

<!--
Antes de implementar, o agente deve confirmar que a documentação é suficiente.

A verificação deve acontecer antes de qualquer código de produção.
-->

Antes de implementar, confirme que:

* `SPEC.md` está com status `ready`;
* `HARNESS.md` está com status `ready`;
* as referências desta tarefa existem;
* o comportamento esperado está explícito;
* entradas e saídas relevantes estão definidas;
* os critérios de aceite são verificáveis;
* não há pergunta aberta bloqueante;
* o teste pode ser derivado da SPEC sem inventar requisitos.

Se qualquer condição não for atendida:

1. não implemente;
2. identifique a lacuna ou contradição;
3. explique qual comportamento está indefinido;
4. proponha a menor correção documental;
5. pare antes de alterar código de produção.

Para tarefas `spec-review` ou `harness-design`, esta seção deve ser adaptada ao
objetivo da revisão.

## Scope

### Included

<!--
Liste exatamente o que esta tarefa deve realizar.

Cada item deve poder ser relacionado a um critério de aceite ou entregável.
-->

Esta tarefa inclui:

* [Alteração incluída.]
* [Teste ou evidência incluída.]
* [Documentação diretamente afetada, quando aplicável.]

### Excluded

<!--
Registre funcionalidades próximas ou tentadoras que não fazem parte desta
execução.
-->

Esta tarefa não inclui:

* [Comportamento fora do escopo.]
* [Cenário futuro.]
* [Refatoração não relacionada.]
* [Integração não autorizada.]

## Allowed Files

<!--
Liste os arquivos que o agente pode modificar.

Use caminhos exatos sempre que forem conhecidos.
-->

O agente pode modificar:

* `projects/<project-name>/tests/<test-file>`
* `projects/<project-name>/src/<source-file>`

O agente pode criar:

* [Arquivo permitido.]
* Nenhum outro arquivo.

## Protected Files

<!--
Arquivos protegidos não podem ser alterados nesta tarefa.

Inclua documentos que já foram aprovados e arquivos fora do escopo.
-->

Não modifique:

* `/AGENTS.md`;
* `/ROADMAP.md`;
* `/PROJECT_IDEAS.md`;
* `/DECISIONS.md`;
* `projects/<project-name>/SPEC.md`;
* `projects/<project-name>/HARNESS.md`;
* [Outros arquivos protegidos.]

## Additional File Rule

Não altere arquivos fora de `Allowed Files`.

Caso seja indispensável alterar ou criar outro arquivo:

1. pare antes de fazer a alteração;
2. identifique o arquivo;
3. explique por que ele é necessário;
4. descreva o impacto esperado;
5. informe se isso representa mudança de escopo, contrato ou arquitetura;
6. aguarde nova autorização.

Não use necessidade de teste como justificativa automática para expandir o
conjunto de arquivos.

## Constraints

<!--
Liste restrições específicas desta tarefa.

Não repita todas as regras globais do AGENTS.md. Inclua apenas restrições que
ajudem a delimitar esta execução.
-->

* Implemente apenas o comportamento referenciado nesta tarefa.
* Use somente dados sintéticos.
* Não altere contratos sem atualização prévia da SPEC.
* Não atualize golden files automaticamente.
* Não refatore componentes não relacionados.
* Não faça chamadas de rede.
* Não use serviços externos.
* Não crie efeitos reais.
* Não crie commits, branches, tags ou pull requests.
* Não reverta mudanças preexistentes do usuário.
* Preserve compatibilidade com [contrato relevante].
* [Restrição específica.]

## Dependencies

**New dependencies allowed:** `no`

<!--
O padrão é não permitir novas dependências.

Quando uma dependência for explicitamente autorizada, substitua por:

New dependencies allowed: yes, limited to `<dependency-name>`

E explique:

- qual problema ela resolve;
- por que a biblioteca padrão não é suficiente;
- impacto no ambiente;
- impacto no harness;
- risco de segurança e manutenção;
- como poderá ser removida futuramente.

Uma dependência que altere arquitetura ou processo pode exigir registro em
DECISIONS.md.
-->

Se a tarefa parecer exigir uma nova dependência não autorizada:

1. não instale;
2. não altere arquivos de dependências;
3. explique a necessidade;
4. apresente uma alternativa sem dependência, quando existir;
5. pare antes da alteração.

## Pre-change Plan

<!--
O agente deve apresentar um plano curto e depois continuar automaticamente,
desde que o plano permaneça dentro do escopo autorizado.

Não é necessário aguardar confirmação depois do plano.
-->

Antes de editar, apresente um plano curto contendo:

1. comportamento que será alterado;
2. arquivos que serão modificados;
3. teste que será criado ou atualizado;
4. menor implementação prevista;
5. comandos de validação;
6. riscos ou ambiguidades observados.

Depois do plano, execute a tarefa sem aguardar confirmação adicional, desde que:

* nenhum arquivo extra seja necessário;
* nenhuma dependência nova seja necessária;
* nenhuma contradição seja encontrada;
* o escopo permaneça inalterado;
* nenhuma condição de parada seja acionada.

## Expected Workflow

<!--
Escolha o fluxo correspondente ao tipo de tarefa.
Remova os fluxos que não forem aplicáveis do prompt final.
-->

### For implementation tasks

1. ler os arquivos obrigatórios;
2. validar o Specification Gate;
3. revisar o teste, fixture e expected output relacionados;
4. escrever ou atualizar o menor teste que representa o comportamento;
5. executar o teste;
6. confirmar que ele falha pelo motivo esperado;
7. implementar a menor mudança necessária;
8. executar novamente o teste;
9. executar o harness relacionado;
10. refatorar somente se necessário;
11. executar novamente as validações;
12. revisar o diff;
13. produzir o Completion Report.

### For test tasks

1. confirmar que o comportamento já está especificado;
2. confirmar que fixture e expected output estão definidos;
3. implementar o teste sem adicionar código de produção;
4. executar o teste;
5. confirmar que a falha corresponde à ausência ou incorreção esperada;
6. não enfraquecer asserts para obter resultado verde;
7. revisar o diff;
8. produzir o Completion Report.

### For fixture tasks

1. identificar o cenário e o propósito da fixture;
2. usar somente dados sintéticos;
3. incluir apenas os campos necessários;
4. manter a fixture pequena e legível;
5. criar ou atualizar o expected output autorizado;
6. validar o formato;
7. não implementar código de produção;
8. produzir o Completion Report.

### For specification or harness review tasks

1. identificar ambiguidades, contradições e lacunas;
2. verificar rastreabilidade;
3. verificar se critérios são observáveis;
4. verificar se entradas, saídas e erros estão definidos;
5. propor alterações mínimas;
6. modificar somente arquivos Markdown autorizados;
7. não implementar código de produção;
8. produzir o Completion Report.

### For refactor tasks

1. confirmar que os testes relevantes passam antes da alteração;
2. registrar o estado inicial;
3. alterar somente a estrutura interna autorizada;
4. não modificar comportamento observável;
5. executar os mesmos testes depois da alteração;
6. comparar resultados;
7. interromper se a refatoração exigir mudança de contrato;
8. produzir o Completion Report.

### For investigation tasks

1. formular a pergunta investigada;
2. reproduzir o problema com o menor exemplo possível;
3. separar fatos de hipóteses;
4. não implementar uma solução definitiva sem autorização;
5. registrar evidências e alternativas;
6. indicar qual decisão ou tarefa deveria vir depois;
7. produzir o Completion Report.

## TDD Requirements

<!--
Use esta seção para tarefas de test ou implementation.

Para tarefas de documentação ou investigação, remova esta seção ou marque-a
explicitamente como não aplicável.
-->

Para esta tarefa, siga o ciclo:

### Red

* criar ou atualizar o teste relacionado;
* executar o teste antes da implementação;
* confirmar que ele falha;
* confirmar que a falha acontece pelo motivo esperado.

### Green

* implementar somente o mínimo necessário;
* executar novamente o teste;
* não implementar cenários adicionais.

### Refactor

* refatorar apenas quando houver benefício claro;
* preservar o comportamento;
* manter todos os testes relacionados passando;
* evitar abstrações para necessidades futuras.

Se o teste passar antes da implementação:

1. não continue automaticamente;
2. investigue se o comportamento já existe;
3. verifique se o teste é fraco ou incorreto;
4. verifique se a fixture representa o cenário;
5. relate a descoberta;
6. pare quando isso alterar a natureza da tarefa.

## Task Acceptance Criteria

<!--
Copie apenas os critérios específicos desta execução.

Além dos ACs da SPEC, inclua critérios operacionais da tarefa.

Cada item deve poder ser verificado.
-->

A tarefa estará concluída quando:

* [ ] `AC-XXX` estiver atendido.
* [ ] `SCN-XXX` estiver representado por teste.
* [ ] `TEST-XXX` tiver sido criado ou atualizado.
* [ ] O teste tiver sido observado falhando pelo motivo esperado.
* [ ] A menor implementação necessária tiver sido adicionada.
* [ ] `EXP-XXX` for produzido sem divergências.
* [ ] Nenhum cenário adicional tiver sido implementado.
* [ ] Nenhuma dependência nova tiver sido adicionada.
* [ ] Somente arquivos permitidos tiverem sido alterados.
* [ ] Os comandos de validação tiverem sido executados.
* [ ] Limitações ou bloqueios tiverem sido relatados.

## Validation Commands

<!--
Forneça comandos exatos.

Não use apenas instruções como "rode os testes".

Os comandos devem funcionar a partir do diretório explicitado em
Command Context.

Se ainda não for possível definir como validar a tarefa, ela provavelmente não
está pronta para implementação.
-->

### Command Context

Execute os comandos a partir de:

```text
[repository root or project directory]
```

### Fast Check

```bash
[exact command for the focused test]
```

**Expected result:** [Resultado esperado.]

### Project Harness

```bash
[exact command for the project harness]
```

**Expected result:** [Resultado esperado.]

### Full Test Suite

```bash
[exact command for the relevant full suite]
```

**Expected result:** [Resultado esperado.]

### Static Validation

```bash
[lint, type-check or schema validation command]
```

**Expected result:** [Resultado esperado.]

<!--
Remova comandos que não se aplicam.

Não invente um comando apenas para preencher o template.
-->

## Validation Rules

Antes de concluir:

* execute o teste diretamente relacionado;
* execute o harness do projeto;
* execute a suíte mais ampla quando for proporcional;
* preserve warnings e erros relevantes;
* não afirme que algo funciona sem executar a validação;
* não atualize expected outputs apenas para obter testes verdes;
* não ignore testes quebrados;
* não substitua validação automatizada por inspeção visual sem justificativa.

Se um comando não puder ser executado:

1. informe que não foi executado;
2. explique o motivo;
3. apresente o comando que deveria ser usado;
4. não declare o comportamento como validado;
5. diferencie `implemented` de `validated`.

## Stop Conditions

<!--
Quando uma condição abaixo ocorrer, o agente deve parar antes de tomar uma
decisão não autorizada.

Parar não significa abandonar silenciosamente a tarefa. Significa produzir um
relatório claro sobre o bloqueio.
-->

Pare e relate quando:

* `SPEC.md` não estiver `ready`;
* `HARNESS.md` não estiver `ready`;
* uma referência obrigatória não existir;
* houver contradição entre SPEC, HARNESS e teste;
* uma pergunta aberta puder alterar o comportamento;
* uma regra tiver mais de uma interpretação plausível;
* o teste não falhar pelo motivo esperado;
* for necessário modificar um arquivo protegido;
* for necessário alterar um arquivo fora de `Allowed Files`;
* for necessária uma dependência não autorizada;
* for necessário mudar um contrato ou schema;
* a tarefa exigir outro cenário não autorizado;
* dados pessoais, credenciais ou secrets forem encontrados;
* a tarefa exigir rede, serviço externo ou efeito real não autorizado;
* alterações preexistentes do usuário impedirem uma mudança segura;
* a implementação mínima não puder ser feita sem ampliar o escopo.

Ao parar, informe:

1. a condição encontrada;
2. a evidência;
3. o impacto;
4. a menor decisão necessária para desbloquear;
5. os arquivos que seriam afetados;
6. nenhuma alteração especulativa adicional.

## Git Rules

Não:

* crie commits;
* crie branches;
* crie tags;
* abra pull requests;
* descarte alterações preexistentes;
* use comandos destrutivos;
* altere o histórico;
* execute `git push`.

Antes de concluir:

* revise o diff;
* identifique mudanças acidentais;
* confirme que somente arquivos permitidos foram alterados;
* confirme que nenhum dado sensível foi adicionado;
* sugira uma mensagem de commit.

## Deliverables

<!--
Liste os resultados concretos esperados.

Entregáveis são diferentes de critérios de aceite:
eles identificam os arquivos ou artefatos que devem existir ao final.
-->

Ao final, devem existir:

* [Arquivo criado ou atualizado.]
* [Teste criado ou atualizado.]
* [Fixture ou expected output, quando aplicável.]
* [Relatório final no chat.]

Nenhum outro entregável está autorizado.

## Completion Report

Ao terminar, responda usando exatamente esta estrutura:

### Summary

Descreva brevemente o que foi feito.

### Files changed

Liste cada arquivo alterado e sua finalidade.

Exemplo:

```text
projects/example/src/parser.py
- Added parsing for the merchant field required by SCN-001.

projects/example/tests/test_parser.py
- Added TEST-001 covering AC-001.
```

### Tests added or updated

Liste:

* testes criados;
* testes alterados;
* critérios e cenários cobertos;
* comportamento observado na etapa Red.

### Validation performed

Para cada comando, informe:

```text
Command: [command]
Result: [pass | fail | blocked | not-run]
Details: [resultado relevante]
```

Não resuma `not-run` como sucesso.

### Scope verification

Informe explicitamente:

* **Spec changed:** `yes | no`
* **Harness changed:** `yes | no`
* **Protected files changed:** `yes | no`
* **Files outside Allowed Files changed:** `yes | no`
* **New dependencies:** `yes | no`
* **Network used:** `yes | no`
* **Sensitive data added:** `yes | no`
* **Commits created:** `yes | no`

Qualquer resposta `yes` que não tenha sido autorizada deve ser explicada como
bloqueio ou desvio.

### Decisions and trade-offs

Informe:

* decisões tomadas;
* alternativas relevantes;
* trade-offs aceitos;
* se um registro em `DECISIONS.md` é recomendado.

Use uma destas opções quando não houver decisão persistente:

```text
No persistent decision was required.
```

### Limitations

Liste comportamentos ainda não suportados, validações não executadas ou riscos
restantes.

### Suggested commit message

Sugira uma única mensagem de commit pequena e coerente.

Exemplo:

```text
feat: parse merchant for synthetic receipt
```

### Suggested next step

Sugira no máximo um próximo incremento pequeno e verificável.

Não execute esse próximo passo na tarefa atual.

## Prompt Readiness Checklist

<!--
Revise este checklist antes de enviar o prompt ao agente.
-->

### Task definition

* [ ] O Task ID foi definido.
* [ ] O projeto e o tipo de tarefa foram definidos.
* [ ] Existe apenas um objetivo principal.
* [ ] O contexto é suficiente e não repete toda a documentação.
* [ ] O escopo incluído está explícito.
* [ ] O escopo excluído está explícito.

### Specification and harness

* [ ] A SPEC aplicável está identificada.
* [ ] O HARNESS aplicável está identificado.
* [ ] Os IDs relevantes estão preenchidos.
* [ ] A SPEC está `ready`, quando necessário.
* [ ] O HARNESS está `ready`, quando necessário.
* [ ] Não existem questões bloqueantes conhecidas.

### Change boundaries

* [ ] Os arquivos permitidos estão listados.
* [ ] Os arquivos protegidos estão listados.
* [ ] A regra para arquivos adicionais está explícita.
* [ ] Novas dependências estão proibidas ou especificamente autorizadas.
* [ ] As restrições negativas estão explícitas.
* [ ] O agente não está autorizado a criar commits.

### Validation

* [ ] Os critérios de aceite da tarefa são verificáveis.
* [ ] O teste relacionado está identificado.
* [ ] A fixture está identificada, quando aplicável.
* [ ] O expected output está identificado, quando aplicável.
* [ ] Os comandos exatos de validação estão presentes.
* [ ] O diretório de execução está claro.
* [ ] As condições de parada estão explícitas.

### Final cleanup

* [ ] Todos os placeholders foram substituídos.
* [ ] Comentários desnecessários foram removidos.
* [ ] Seções não aplicáveis foram removidas.
* [ ] O prompt não pede implementação de mais de um incremento.
* [ ] O prompt não duplica desnecessariamente o `AGENTS.md`.
* [ ] O Completion Report exigido está preservado.
