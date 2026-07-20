# Validation Harness

<!--
Substitua este título pelo nome do projeto ou da funcionalidade.

Este documento descreve como comprovar que o comportamento definido em SPEC.md
foi implementado corretamente.

A SPEC define o que deve acontecer.
O harness define como verificar, de forma reproduzível, que isso aconteceu.

Não repita toda a especificação. Faça referências aos IDs já definidos:

- AC-XXX: acceptance criteria;
- SCN-XXX: behavior scenarios;
- BR-XXX: business rules;
- INV-XXX: invariants;
- ERR-XXX: error behaviors;
- EDGE-XXX: edge cases.
-->

## Metadata

* **Project:** `<project-name>`
* **Status:** `draft`
* **Related SPEC:** `SPEC.md`

<!--
Status permitidos:

- draft: estratégia de validação ainda incompleta;
- ready: harness definido e pronto para orientar implementação;
- superseded: harness substituído por uma versão posterior.

O Status ready significa que:

- os comportamentos relevantes estão mapeados;
- as fixtures necessárias estão definidas;
- as saídas esperadas estão definidas;
- os comandos de validação estão claros;
- as condições de sucesso e falha são verificáveis.

O resultado momentâneo dos testes não deve ser armazenado no Status.
Resultados de execuções podem ser registrados na seção Validation Record.
-->

## Purpose

<!--
Explique o objetivo deste harness.

Procure responder:

- Qual comportamento central será validado?
- Que tipo de confiança este harness deve fornecer?
- Para qual fase ou versão ele foi criado?
- Qual risco principal ele ajuda a reduzir?

Evite descrições genéricas como "testar o sistema".
-->

Este harness existe para validar que:

* [Comportamento principal.]
* [Regra ou contrato importante.]
* [Comportamento de erro relevante.]

## System Under Test

<!--
Defina o System Under Test, ou SUT.

O SUT é o componente ou limite específico que será exercitado pelo harness.

Evite declarar o projeto inteiro como SUT quando a tarefa atual valida apenas
uma função, parser, serviço ou fluxo local.

Registre:

- componente;
- entry point;
- limite da entrada;
- limite da saída;
- dependências relevantes.
-->

**Component:** `[component-name]`

**Entry point:** `[function, command or interface]`

**Input boundary:** [O que entra no SUT.]

**Output boundary:** [O que sai do SUT.]

**Relevant dependencies:**

* [Dependência interna ou externa relevante.]
* [Dependência interna ou externa relevante.]

## Validation Strategy

<!--
Liste somente as estratégias realmente usadas neste harness.

Opções comuns:

Unit test:
Valida uma função ou regra isolada.

Golden test:
Compara uma saída completa com um arquivo de referência aprovado.

Contract test:
Valida se uma interface, schema ou estrutura de dados respeita um contrato.

Integration test:
Valida a colaboração entre dois ou mais componentes reais.

End-to-end test:
Valida um fluxo completo pelos limites externos do sistema.

Property-based test:
Gera múltiplas entradas para verificar propriedades ou invariants.

Manual check:
Validação humana explícita para algo que ainda não é automatizado.

Para projetos iniciais, prefira a menor combinação que produza confiança
suficiente. Não adicione tipos de teste apenas para aumentar a quantidade de
camadas.
-->

| Strategy   | Purpose                         | Scope              |
| ---------- | ------------------------------- | ------------------ |
| `unit`     | [Regra ou função validada.]     | [Limite do teste.] |
| `golden`   | [Saída completa comparada.]     | [Limite do teste.] |
| `contract` | [Schema ou interface validada.] | [Limite do teste.] |

## Test Environment

<!--
Descreva o ambiente mínimo necessário para executar o harness.

Inclua apenas o que afeta a reprodução dos testes:

- runtime;
- versão mínima;
- sistema operacional, somente quando relevante;
- dependências;
- variáveis de ambiente;
- arquivos necessários;
- restrições de rede.

O harness local deve evitar rede e serviços externos sempre que possível.
-->

**Runtime:** [Exemplo: Python 3.13.]

**Required tools:**

* [Ferramenta necessária.]
* [Ferramenta necessária.]

**Environment variables:**

* Nenhuma.

<!--
Quando houver variáveis necessárias, liste apenas os nomes e a finalidade.
Nunca registre valores secretos.
-->

**Network access required:** `no`

**External services required:** `no`

## Recommended Fixture Structure

<!--
Estrutura padrão recomendada para projetos pequenos:

fixtures/
├── inputs/
└── expected/

Use nomes relacionados entre entrada e saída:

fixtures/inputs/single_item_receipt.txt
fixtures/expected/single_item_receipt.json

Quando uma fixture não possuir saída golden, ela ainda pode ser usada em testes
de erro, invariants ou validações unitárias.
-->

```text id="j9q1e4"
fixtures/
├── inputs/
│   ├── example_case_01.txt
│   └── example_case_02.txt
└── expected/
    ├── example_case_01.json
    └── example_case_02.json
```

## Traceability Matrix

<!--
Conecte cada critério de aceite e cenário da SPEC à sua evidência executável.

Todo acceptance criterion deve possuir ao menos uma forma de validação.

Use:

- FX-XXX para fixture de entrada;
- EXP-XXX para saída esperada;
- TEST-XXX para caso de teste.

Um mesmo teste pode cobrir mais de um critério, mas isso deve estar explícito.

Uma fixture pode ser reutilizada quando isso não tornar os testes confusos ou
excessivamente acoplados.
-->

| Acceptance criterion | Scenario  | Rules or errors | Fixture  | Expected output | Test       |
| -------------------- | --------- | --------------- | -------- | --------------- | ---------- |
| `AC-001`             | `SCN-001` | `BR-001`        | `FX-001` | `EXP-001`       | `TEST-001` |
| `AC-002`             | `SCN-002` | `INV-001`       | `FX-002` | `EXP-002`       | `TEST-002` |
| `AC-003`             | `SCN-003` | `ERR-001`       | `FX-003` | N/A             | `TEST-003` |

## Fixture Manifest

<!--
Documente a finalidade de cada fixture.

Uma boa fixture deve:

- representar um cenário específico;
- ser pequena;
- ser compreensível;
- conter apenas dados sintéticos;
- evitar campos irrelevantes;
- permanecer estável;
- ter um nome que revele sua intenção.

Não copie dados reais e apenas altere nomes. Crie exemplos sintéticos que
representem o formato necessário.
-->

| ID       | File                                  | Related scenario | Purpose                        | Sensitive data? |
| -------- | ------------------------------------- | ---------------- | ------------------------------ | --------------: |
| `FX-001` | `fixtures/inputs/example_case_01.txt` | `SCN-001`        | [Cenário válido principal.]    |              no |
| `FX-002` | `fixtures/inputs/example_case_02.txt` | `SCN-002`        | [Caso válido alternativo.]     |              no |
| `FX-003` | `fixtures/inputs/invalid_case_01.txt` | `SCN-003`        | [Entrada inválida específica.] |              no |

## Expected Output Manifest

<!--
Expected outputs são resultados aprovados usados como referência.

Eles são especialmente úteis em golden tests.

Arquivos expected devem:

- ser legíveis por humanos;
- conter somente dados determinísticos;
- evitar timestamps, IDs aleatórios ou caminhos locais instáveis;
- usar ordenação consistente;
- respeitar o contrato definido na SPEC;
- ser revisados antes de qualquer atualização.

Não atualize automaticamente um golden apenas porque o teste falhou.

Uma falha pode indicar:

- regressão;
- mudança legítima de contrato;
- fixture incorreta;
- golden incorreto;
- teste mal definido.

Investigue a causa antes de aceitar uma nova saída.
-->

| ID        | File                                     | Related fixture | Format | Purpose               |
| --------- | ---------------------------------------- | --------------- | ------ | --------------------- |
| `EXP-001` | `fixtures/expected/example_case_01.json` | `FX-001`        | `JSON` | [Resultado esperado.] |
| `EXP-002` | `fixtures/expected/example_case_02.json` | `FX-002`        | `JSON` | [Resultado esperado.] |

## Expected Output Rules

<!--
Preencha apenas as regras relevantes para o projeto.
-->

* Campos obrigatórios devem sempre estar presentes.
* Valores monetários devem usar [formato definido na SPEC].
* A ordenação de [campo ou coleção] faz parte do contrato.
* Campos instáveis devem ser normalizados antes da comparação.
* O arquivo esperado não deve ser atualizado sem revisão humana.
* Diferenças entre saída atual e esperada devem ser exibidas claramente.

## Test Cases

<!--
A matriz de rastreabilidade oferece a visão geral.

Detalhe abaixo apenas testes:

- centrais para o comportamento;
- complexos;
- com preparação especial;
- com condições de falha importantes;
- que exigem explicação além do nome do teste.

Cada teste deve validar um comportamento claro.
-->

### TEST-001 — [Nome do teste]

**Covers:** `AC-001`, `SCN-001`, `BR-001`

**Test level:** `golden`

**Fixture:** `FX-001`

**Expected output:** `EXP-001`

**Setup:**

1. [Preparação necessária.]
2. [Preparação necessária.]

**Execution:**

[Descreva a ação executada sobre o SUT.]

**Pass condition:**

* [Condição verificável.]
* [Condição verificável.]

**Failure evidence:**

* código de saída diferente de zero;
* diff entre a saída atual e `EXP-001`;
* identificação do campo ou valor divergente.

### TEST-002 — [Nome do teste]

**Covers:** `AC-002`, `SCN-002`, `INV-001`

**Test level:** `unit | golden | contract | integration`

**Fixture:** `FX-002`

**Expected output:** `EXP-002 | N/A`

**Pass condition:**

* [Condição verificável.]

**Failure evidence:**

* [Como a falha deve ser apresentada.]

## Invalid Input Validation

<!--
Mapeie os erros definidos na SPEC.

O teste deve verificar não apenas que houve uma falha, mas que o sistema falhou
da maneira esperada.

Quando aplicável, valide:

- tipo de erro;
- error identifier;
- mensagem;
- código de saída;
- ausência de saída parcial;
- ausência de dados sensíveis;
- preservação de invariants.
-->

| Error     | Fixture  | Test       | Expected behavior                     |
| --------- | -------- | ---------- | ------------------------------------- |
| `ERR-001` | `FX-003` | `TEST-003` | [Erro esperado e condição de parada.] |

### TEST-003 — [Nome do teste de erro]

**Covers:** `ERR-001`, `AC-003`

**Fixture:** `FX-003`

**Expected error:** `[error_identifier]`

**Pass condition:**

* o processamento falha de forma controlada;
* o identificador esperado é retornado;
* nenhuma saída válida é produzida;
* a mensagem não contém dados sensíveis.

## Edge-Case Validation

<!--
Mapeie os edge cases da SPEC.

Edge cases podem ser válidos, mesmo que incomuns.

Não trate todo caso incomum como erro.
-->

| Edge case  | Fixture  | Test       | Expected behavior         |
| ---------- | -------- | ---------- | ------------------------- |
| `EDGE-001` | `FX-004` | `TEST-004` | [Comportamento esperado.] |

## Invariant Validation

<!--
Explique como cada invariant relevante será comprovada.

Uma invariant importante pode ter:

- teste direto;
- teste parametrizado;
- property-based test;
- validação de schema;
- múltiplos cenários que demonstrem sua preservação.
-->

| Invariant | Validation method | Tests                  |
| --------- | ----------------- | ---------------------- |
| `INV-001` | [Método.]         | `TEST-002`, `TEST-004` |

## Contract Validation

<!--
Use esta seção quando a saída, schema, função ou integração tiver um contrato
explícito.

Um contract test verifica se o sistema mantém uma interface previamente
definida.

Exemplos:

- campos obrigatórios de um JSON;
- tipos de dados;
- assinatura pública de uma função;
- formato de um arquivo;
- respostas esperadas de uma integração mockada.

Não confunda contract test com teste de implementação interna.
-->

**Contract under validation:** [Nome ou descrição.]

**Contract source:** [SPEC, schema file ou decisão.]

**Validation method:** [Como o contrato será verificado.]

**Breaking changes include:**

* remoção de campo obrigatório;
* mudança incompatível de tipo;
* alteração de significado;
* modificação da estrutura sem atualização da SPEC.

## External Dependency Substitutes

<!--
Dependências externas não devem ser o único caminho para validar o sistema.

Termos úteis:

Fixture:
dado estático usado como entrada ou referência.

Stub:
substituto que retorna respostas predeterminadas.

Fake:
implementação simplificada, mas funcional.

Mock:
substituto controlado que também permite verificar como foi chamado.

Escolha a alternativa mais simples que permita validar o comportamento.
Não é necessário usar frameworks específicos de mocking.
-->

| Dependency      | Substitute              | Type     | Purpose |      |       |                           |
| --------------- | ----------------------- | -------- | ------- | ---- | ----- | ------------------------- |
| [External API.] | [Local file or object.] | `fixture | stub    | fake | mock` | [Comportamento simulado.] |

### Substitute behavior

<!--
Descreva apenas o contrato necessário para o teste.
-->

* [Entrada recebida pelo substituto.]
* [Resposta predeterminada.]
* [Erro que pode ser simulado.]
* [Interação que precisa ser verificada.]

## Manual Checks

<!--
Testes manuais são permitidos quando uma validação ainda não puder ser
automatizada de forma proporcional.

O comportamento central não deve depender exclusivamente de testes manuais.

Todo check manual deve ter:

- objetivo;
- procedimento;
- condição de aprovação;
- justificativa para não estar automatizado.
-->

| Check        | Procedure | Pass condition | Reason not automated |
| ------------ | --------- | -------------- | -------------------- |
| [Validação.] | [Passos.] | [Condição.]    | [Justificativa.]     |

## Validation Commands

<!--
Liste comandos reproduzíveis.

Categorias possíveis:

Fast check:
teste isolado e rápido para o comportamento em desenvolvimento.

Project harness:
execução principal do harness do projeto.

Full test suite:
todos os testes disponíveis.

Static validation:
lint, type checking ou schema validation.

Manual smoke test:
execução mínima feita por uma pessoa.

Não inclua comandos que dependam de contexto não documentado.
-->

| Purpose           | Command     | Expected result       |
| ----------------- | ----------- | --------------------- |
| Fast check        | `[command]` | [Resultado esperado.] |
| Project harness   | `[command]` | [Resultado esperado.] |
| Full test suite   | `[command]` | [Resultado esperado.] |
| Static validation | `[command]` | [Resultado esperado.] |

### Command prerequisites

* [Diretório a partir do qual o comando deve ser executado.]
* [Dependência necessária.]
* [Arquivo necessário.]
* [Variável de ambiente, se houver.]

## Failure Reporting

<!--
Falhas devem ser visíveis e úteis.

O harness deve, sempre que possível:

- retornar código de saída diferente de zero;
- identificar o teste que falhou;
- mostrar esperado versus atual;
- mostrar diff de golden files;
- indicar fixture envolvida;
- preservar traceback ou contexto relevante;
- evitar mensagens genéricas;
- não ignorar erros silenciosamente.

Não transforme falhas em warnings apenas para manter a execução verde.
-->

Em caso de falha, o harness deve informar:

* teste;
* critério de aceite ou cenário relacionado;
* fixture utilizada;
* resultado esperado;
* resultado atual;
* diferença relevante;
* comando executado;
* código de saída.

### Golden-file failures

Quando uma saída divergir de um golden:

1. não atualizar o arquivo automaticamente;
2. revisar a SPEC;
3. revisar a fixture;
4. revisar a implementação;
5. determinar se houve regressão ou mudança legítima;
6. atualizar o golden somente após aprovação humana.

## TDD Workflow

<!--
TDD, ou Test-Driven Development, é o processo usado para implementar cada
comportamento em pequenos ciclos.

Red:
escrever um teste relevante que falha pelo motivo esperado.

Green:
implementar a menor alteração que faz o teste passar.

Refactor:
melhorar a estrutura sem alterar o comportamento, mantendo os testes passando.

O teste deve derivar de um comportamento já especificado.
TDD não substitui uma SPEC válida.
-->

Para cada incremento:

1. selecionar um critério e cenário da SPEC;
2. confirmar que o comportamento está suficientemente especificado;
3. criar ou revisar a fixture;
4. criar ou revisar a saída esperada;
5. escrever o menor teste que representa o comportamento;
6. executar o teste e confirmar que ele falha pelo motivo esperado;
7. implementar a menor mudança necessária;
8. executar novamente o teste;
9. executar o harness relacionado;
10. refatorar somente se os testes permanecerem passando;
11. revisar o diff antes de avançar.

## Test Independence

<!--
Os testes devem poder ser executados:

- em qualquer ordem;
- mais de uma vez;
- sem depender de dados produzidos por outro teste;
- sem depender de horário, rede ou estado externo não controlado.

Quando isso não for possível, documente claramente a dependência.
-->

Os testes não devem depender de:

* ordem de execução;
* arquivos temporários deixados por outro teste;
* horário atual não controlado;
* rede;
* banco de dados compartilhado;
* estado de uma conta externa;
* dados pessoais reais.

## Determinism

<!--
Um teste determinístico produz o mesmo resultado quando executado repetidamente
sob as mesmas condições.

Fontes comuns de instabilidade:

- datas e horários atuais;
- randomização sem seed;
- ordem não garantida;
- IDs aleatórios;
- rede;
- concorrência;
- locale;
- timezone;
- diferenças de sistema operacional.

Registre como cada fonte relevante será controlada.
-->

| Source of instability | Control                               |
| --------------------- | ------------------------------------- |
| Current time          | [Clock injection, fixed date or N/A.] |
| Random values         | [Fixed seed or N/A.]                  |
| Ordering              | [Explicit sorting or N/A.]            |
| Timezone              | [Fixed timezone or N/A.]              |
| Locale                | [Fixed locale or N/A.]                |

## Data Safety

<!--
Todo dado usado pelo harness deve seguir as regras de privacidade do
repositório.

Não presuma que dados em tests/ ou fixtures/ são inofensivos.

Fixtures devem representar formato e comportamento, não preservar pessoas ou
documentos reais.
-->

* Todas as fixtures são sintéticas.
* Nenhuma fixture contém identificadores pessoais reais.
* Nenhum golden contém tokens, secrets ou dados reais.
* Logs de teste não reproduzem entradas sensíveis.
* Dados reais anonimizados, quando necessários, permanecem fora do Git.
* Arquivos temporários são removidos ou ignorados adequadamente.

## Coverage Boundaries

<!--
Explique claramente o que este harness valida e o que ele não valida.

Isto evita uma falsa sensação de segurança.

Exemplos:

Valida:
- parsing local;
- schema da saída;
- erros suportados.

Não valida:
- acesso ao QR Code;
- disponibilidade de site externo;
- qualidade de dados reais;
- performance em grande escala.
-->

### Validated

Este harness valida:

* [Comportamento validado.]
* [Contrato validado.]
* [Erro validado.]

### Not validated

Este harness não valida:

* [Integração fora do escopo.]
* [Cenário futuro.]
* [Característica ainda não medida.]

### Residual risks

<!--
Riscos que continuam existindo mesmo com o harness passando.
-->

* [Risco residual.]
* [Risco residual.]

## Harness Maintenance Rules

<!--
Defina como o harness deve evoluir junto com a SPEC e a implementação.
-->

* Toda mudança de comportamento exige revisão da SPEC.
* Todo novo acceptance criterion exige uma evidência de validação.
* Mudanças em cenários devem atualizar a matriz de rastreabilidade.
* Fixtures sem cenário ou teste associado devem ser removidas ou justificadas.
* Testes obsoletos não devem permanecer apenas para preservar cobertura.
* Goldens devem ser revisados, não regenerados cegamente.
* Alterações em contratos devem ser tratadas como potencialmente incompatíveis.
* O harness não deve ser acoplado a detalhes internos sem necessidade.

## Optional Validation Record

<!--
Esta seção é opcional.

Ela pode ser útil durante o aprendizado para registrar execuções relevantes,
como:

- primeira execução completa;
- validação antes de concluir uma fase;
- reprodução de uma regressão;
- execução usada em uma retrospectiva.

Não registre toda execução local.
Git e ferramentas de CI podem assumir esse papel no futuro.

O campo Commit pode permanecer como uncommitted quando a execução ocorrer antes
do commit.
-->

| Date         | Commit        | Command     | Result | Notes |          |               |
| ------------ | ------------- | ----------- | ------ | ----- | -------- | ------------- |
| `YYYY-MM-DD` | `uncommitted` | `[command]` | `pass  | fail  | blocked` | [Observação.] |

## Harness Readiness Checklist

<!--
Todos os itens obrigatórios devem estar preenchidos antes de alterar o Status
de draft para ready.

Itens não aplicáveis podem ser marcados como N/A com justificativa.
-->

### Scope and strategy

* [ ] O System Under Test está claramente definido.
* [ ] Os limites de entrada e saída estão explícitos.
* [ ] As estratégias de teste adotadas são proporcionais ao projeto.
* [ ] O harness não tenta validar funcionalidades fora da fase atual.
* [ ] As dependências relevantes estão identificadas.

### Traceability

* [ ] Todo acceptance criterion possui uma forma de validação.
* [ ] Todos os cenários principais estão associados a testes.
* [ ] Regras e invariants importantes possuem cobertura identificável.
* [ ] Erros relevantes possuem testes.
* [ ] Edge cases relevantes possuem testes.
* [ ] A matriz de rastreabilidade está preenchida.

### Fixtures and expected outputs

* [ ] Todas as fixtures possuem finalidade clara.
* [ ] Todas as fixtures usam dados sintéticos.
* [ ] Fixtures válidas e inválidas estão separadas de forma compreensível.
* [ ] Expected outputs existem quando necessários.
* [ ] Expected outputs são determinísticos.
* [ ] Golden files podem ser revisados por humanos.
* [ ] Não há atualização automática de goldens sem revisão.

### Execution

* [ ] Os comandos de validação estão documentados.
* [ ] Os comandos podem ser executados a partir de um diretório conhecido.
* [ ] Dependências e pré-requisitos estão explícitos.
* [ ] Falhas retornam código de saída diferente de zero.
* [ ] Mensagens de falha ajudam a localizar o problema.
* [ ] Diferenças entre esperado e atual são visíveis.

### Test quality

* [ ] Os testes são independentes.
* [ ] Os testes são reproduzíveis.
* [ ] Fontes de instabilidade foram controladas.
* [ ] O comportamento central não depende apenas de testes manuais.
* [ ] Os testes verificam comportamento, não apenas implementação interna.
* [ ] Pelo menos um teste foi confirmado falhando pelo motivo esperado antes da implementação.

### Safety and boundaries

* [ ] Nenhum dado sensível está presente.
* [ ] Dependências externas foram substituídas ou isoladas.
* [ ] Os limites do harness estão documentados.
* [ ] Riscos residuais estão explícitos.
* [ ] O harness não cria efeitos reais.

## Harness Approval

<!--
Preencha esta seção depois da revisão do checklist.

A aprovação indica que o harness é suficiente para orientar o primeiro ciclo
de implementação.

Ela não significa que os testes já estão passando. Significa que a estratégia,
os dados e as condições de validação estão definidos.
-->

* **Reviewed by:** [Nome ou papel.]
* **Decision:** `approved | changes-required`
* **Notes:** [Observações.]

## Implementation Entry Gate

<!--
A implementação pode começar quando:

1. SPEC.md estiver com Status ready;
2. não existirem perguntas bloqueantes relevantes;
3. este harness estiver aprovado;
4. o primeiro cenário estiver ligado a fixture, expected output e teste;
5. o comando de validação estiver definido.

O primeiro ciclo deve começar com apenas um comportamento.
-->

Antes do primeiro código de produção, confirmar:

* [ ] `SPEC.md` está `ready`.
* [ ] Este harness está `ready`.
* [ ] O cenário inicial foi escolhido.
* [ ] A fixture inicial existe ou está claramente definida.
* [ ] A saída esperada existe ou está claramente definida.
* [ ] O primeiro teste pode ser escrito.
* [ ] O comando para executar esse teste está documentado.
