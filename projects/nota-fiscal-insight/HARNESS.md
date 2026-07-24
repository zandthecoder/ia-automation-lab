# Nota Fiscal Insight — Validation Harness

## Metadata

* **Project:** `nota-fiscal-insight`
* **Status:** `ready`
* **Related SPEC:** `SPEC.md`

Este harness está `ready` para o primeiro ciclo de implementação porque:

* `FX-001` foi criada;
* `EXP-001` foi revisado;
* os comandos necessários ao primeiro ciclo `SCN-001` foram testados no ambiente local;
* a estratégia foi aprovada pelo usuário.

## Purpose

Este harness existe para comprovar que o parser local:

* transforma uma nota fiscal sintética válida em uma estrutura previsível;
* preserva os valores e a ordem definidos na SPEC;
* valida os cálculos de itens e do total da nota;
* rejeita entradas inválidas com erros estruturados;
* não retorna resultados parciais em caso de falha;
* funciona sem rede, banco de dados ou serviços externos.

O principal risco reduzido por este harness é implementar um parser que aparentemente funciona para um exemplo, mas aceita dados inconsistentes ou produz saídas incompatíveis com o contrato.

## System Under Test

**Component:** synthetic receipt parser

**Entry point:**

```python
parse_receipt(raw_text: str) -> dict
```

**Source module:**

```text
src/receipt_parser.py
```

**Input boundary:** string contendo uma única nota fiscal sintética no formato definido em `SPEC.md`.

**Output boundary:** dicionário Python serializável como JSON.

**Error boundary:** exceção estruturada:

```python
ReceiptValidationError
```

A exceção deve disponibilizar:

```text
code
message
line_number
```

**Relevant dependencies:**

* `decimal.Decimal`;
* parsing de datas da biblioteca padrão;
* `pytest`;
* fixtures locais.

## Minimal Stack

A primeira versão utilizará:

```text
Language: Python 3.13
Test runner: pytest
Development operating system: Windows 11
Development shell: PowerShell
Environment: venv
Python invocation: .\.venv\Scripts\python.exe
Package installation: pip
Production dependencies: standard library only
```

O código de produção não deve depender de bibliotecas externas nesta fase.

O `pytest` é uma dependência apenas de desenvolvimento e teste.

Os comandos automatizados não devem depender da ativação da `.venv`. O interpretador virtual deve ser chamado diretamente por:

```text
.\.venv\Scripts\python.exe
```

Essa convenção evita dependência do estado da sessão do PowerShell e da política de execução de scripts do Windows.

## Proposed Project Structure

```text
nota-fiscal-insight/
├── HARNESS.md
├── README.md
├── SPEC.md
├── fixtures/
│   ├── inputs/
│   │   ├── valid_single_item.txt
│   │   ├── valid_multiple_items.txt
│   │   ├── valid_decimal_quantity.txt
│   │   ├── invalid_line_total.txt
│   │   ├── invalid_receipt_total.txt
│   │   ├── invalid_missing_item.txt
│   │   ├── invalid_record_order.txt
│   │   └── invalid_numeric_format.txt
│   └── expected/
│       ├── valid_single_item.json
│       ├── valid_multiple_items.json
│       └── valid_decimal_quantity.json
├── src/
│   └── receipt_parser.py
└── tests/
    └── test_receipt_parser.py
```

Não devem ser criados módulos ou diretórios adicionais antes que exista uma necessidade demonstrada.

## Validation Strategy

| Strategy       | Purpose                                              | Scope                                         |
| -------------- | ---------------------------------------------------- | --------------------------------------------- |
| `unit`         | Validar regras isoladas de parsing, formato e erro.  | Função `parse_receipt` e exceção pública.     |
| `golden`       | Comparar a saída completa com JSON aprovado.         | Cenários válidos principais.                  |
| `contract`     | Validar schema, tipos e contrato dos erros.          | Saída estruturada e `ReceiptValidationError`. |
| `parametrized` | Validar vários formatos inválidos com a mesma regra. | Números, campos obrigatórios e ordem.         |

Não serão utilizados nesta fase:

* integration tests com serviços externos;
* end-to-end tests de aplicação web;
* property-based testing;
* testes de banco de dados;
* testes de rede;
* testes de performance em grande escala.

## Test Environment

**Development environment:** Windows 11

**Development shell:** PowerShell

**Runtime:** Python 3.13

**Required base interpreter:**

* `python`, resolvendo para Python 3.13.

**Required host tools:**

* Python 3.13;
* módulo `venv`;
* `pip`.

**Production dependencies:**

* nenhuma além da biblioteca padrão.

**Development dependencies:**

* `pytest`, instalado dentro da `.venv`.

**Environment variables:**

* nenhuma.

**Network access required for test execution:** `no`

**Network access potentially required for initial dependency installation:** `yes`

**External services required:** `no`

**Database required:** `no`

**Operating-system-specific behavior:**

* o código de produção não deve possuir comportamento específico de sistema operacional;
* os comandos documentados neste harness são específicos para PowerShell no Windows;
* os testes devem usar APIs portáveis, como `pathlib`, e não devem depender de separadores de caminho escritos manualmente.

## Environment Setup

Os comandos devem ser executados a partir da pasta:

```text
D:\dev\ia-automation-lab\projects\nota-fiscal-insight
```

Confirmar primeiro o interpretador base:

```powershell
python --version
```

Resultado esperado:

```text
Python 3.13.x
```

Criar o ambiente virtual:

```powershell
python -m venv .venv
```

Confirmar o interpretador da `.venv` sem ativá-la:

```powershell
.\.venv\Scripts\python.exe --version
```

Resultado esperado:

```text
Python 3.13.x
```

Instalar o test runner dentro da `.venv`:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
```

Confirmar a instalação:

```powershell
.\.venv\Scripts\python.exe -m pytest --version
```

O ambiente virtual `.venv\` não deve ser versionado.

A ativação por `Activate.ps1` não faz parte do procedimento exigido por este harness.

A execução direta de:

```text
.\.venv\Scripts\python.exe
```

é a convenção oficial deste projeto para comandos Python e `pytest`.

Essa estratégia evita depender da política de execução de scripts do PowerShell e garante que o interpretador usado pertence à `.venv` do projeto.

## Fixture Structure

```text
fixtures/
├── inputs/
└── expected/
```

As fixtures de entrada devem permanecer separadas dos expected outputs.

Os pares devem usar nomes relacionados:

```text
fixtures/inputs/valid_single_item.txt
fixtures/expected/valid_single_item.json
```

Fixtures inválidas normalmente não possuem expected output JSON, pois o resultado esperado é uma exceção estruturada.

## Fixture Manifest

| ID       | File                                            | Related scenario | Purpose                                        | Sensitive data? |
| -------- | ----------------------------------------------- | ---------------- | ---------------------------------------------- | --------------: |
| `FX-001` | `fixtures/inputs/valid_single_item.txt`         | `SCN-001`        | Nota válida com um item e quantidade inteira.  |              no |
| `FX-002` | `fixtures/inputs/valid_multiple_items.txt`      | `SCN-002`        | Nota válida com vários itens.                  |              no |
| `FX-003` | `fixtures/inputs/valid_decimal_quantity.txt`    | `SCN-003`        | Nota válida com quantidade decimal.            |              no |
| `FX-004` | `fixtures/inputs/invalid_line_total.txt`        | `SCN-004`        | Total de item matematicamente inconsistente.   |              no |
| `FX-005` | `fixtures/inputs/invalid_receipt_total.txt`     | `SCN-005`        | Total da nota diferente da soma dos itens.     |              no |
| `FX-006` | `fixtures/inputs/invalid_missing_item.txt`      | `SCN-006`        | Entrada sem registro `ITEM`.                   |              no |
| `FX-007` | `fixtures/inputs/invalid_record_order.txt`      | `SCN-007`        | Registros válidos em ordem incorreta.          |              no |
| `FX-008` | `fixtures/inputs/valid_external_whitespace.txt` | `SCN-008`        | Entrada válida com espaços e linhas em branco. |              no |
| `FX-009` | `fixtures/inputs/invalid_numeric_format.txt`    | `SCN-009`        | Quantidade ou valor com formato não suportado. |              no |
| `FX-010` | `fixtures/inputs/invalid_empty_input.txt`       | `SCN-010`        | Entrada completamente vazia.                   |              no |

## Fixture Contents

### FX-001 — Valid single-item receipt

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-01
ITEM: Arroz | 2 | 8.50 | 17.00
TOTAL: 17.00
```

### FX-002 — Valid multiple-item receipt

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-02
ITEM: Arroz | 2 | 8.50 | 17.00
ITEM: Café | 1 | 12.00 | 12.00
TOTAL: 29.00
```

### FX-003 — Valid decimal quantity

```text
MERCHANT: Feira Exemplo
DATE: 2026-07-03
ITEM: Tomate | 0.750 | 10.00 | 7.50
TOTAL: 7.50
```

### FX-004 — Invalid line total

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-04
ITEM: Arroz | 2 | 8.50 | 16.00
TOTAL: 16.00
```

### FX-005 — Invalid receipt total

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-05
ITEM: Arroz | 2 | 8.50 | 17.00
ITEM: Café | 1 | 12.00 | 12.00
TOTAL: 30.00
```

### FX-006 — Missing item

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-06
TOTAL: 10.00
```

### FX-007 — Invalid record order

```text
DATE: 2026-07-07
MERCHANT: Mercado Exemplo
ITEM: Arroz | 1 | 8.50 | 8.50
TOTAL: 8.50
```

### FX-008 — External whitespace

```text


  MERCHANT:   Mercado Exemplo

 DATE: 2026-07-08

 ITEM:   Arroz   |  2  |  8.50  |  17.00

 TOTAL: 17.00


```

### FX-009 — Unsupported numeric format

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-09
ITEM: Tomate | 0,750 | 10.00 | 7.50
TOTAL: 7.50
```

### FX-010 — Empty input

**Status:** planned

O arquivo `fixtures/inputs/invalid_empty_input.txt` deverá possuir exatamente `0 bytes`, sem quebra de linha ou qualquer outro conteúdo.

`FX-010` representa somente uma string completamente vazia. Uma entrada contendo apenas whitespace não faz parte de `SCN-010` e poderá ser avaliada separadamente no futuro.

## Expected Output Manifest

| ID        | File                                               | Related fixture | Format | Purpose                                             |
| --------- | -------------------------------------------------- | --------------- | ------ | --------------------------------------------------- |
| `EXP-001` | `fixtures/expected/valid_single_item.json`         | `FX-001`        | JSON   | Saída de uma nota válida com um item.               |
| `EXP-002` | `fixtures/expected/valid_multiple_items.json`      | `FX-002`        | JSON   | Saída de uma nota válida com vários itens.          |
| `EXP-003` | `fixtures/expected/valid_decimal_quantity.json`    | `FX-003`        | JSON   | Saída preservando quantidade decimal.               |
| `EXP-004` | `fixtures/expected/valid_external_whitespace.json` | `FX-008`        | JSON   | Saída normalizada após remoção de espaços externos. |

## Expected Outputs

### EXP-001 — Valid single item

```json
{
  "merchant": {
    "name": "Mercado Exemplo"
  },
  "purchase_date": "2026-07-01",
  "items": [
    {
      "description": "Arroz",
      "quantity": "2",
      "unit_price": "8.50",
      "line_total": "17.00"
    }
  ],
  "receipt_total": "17.00"
}
```

### EXP-002 — Valid multiple items

```json
{
  "merchant": {
    "name": "Mercado Exemplo"
  },
  "purchase_date": "2026-07-02",
  "items": [
    {
      "description": "Arroz",
      "quantity": "2",
      "unit_price": "8.50",
      "line_total": "17.00"
    },
    {
      "description": "Café",
      "quantity": "1",
      "unit_price": "12.00",
      "line_total": "12.00"
    }
  ],
  "receipt_total": "29.00"
}
```

### EXP-003 — Valid decimal quantity

```json
{
  "merchant": {
    "name": "Feira Exemplo"
  },
  "purchase_date": "2026-07-03",
  "items": [
    {
      "description": "Tomate",
      "quantity": "0.750",
      "unit_price": "10.00",
      "line_total": "7.50"
    }
  ],
  "receipt_total": "7.50"
}
```

### EXP-004 — Valid external whitespace

```json
{
  "merchant": {
    "name": "Mercado Exemplo"
  },
  "purchase_date": "2026-07-08",
  "items": [
    {
      "description": "Arroz",
      "quantity": "2",
      "unit_price": "8.50",
      "line_total": "17.00"
    }
  ],
  "receipt_total": "17.00"
}
```

## Expected Output Rules

* Expected outputs devem ser revisados por uma pessoa.
* Expected outputs não podem ser atualizados automaticamente.
* Valores monetários devem permanecer como strings com duas casas decimais.
* Quantidades devem preservar a representação textual validada.
* A ordem dos itens faz parte do contrato.
* Nenhum campo adicional deve aparecer.
* JSON deve utilizar encoding UTF-8.
* Chaves devem seguir exatamente os nomes definidos na SPEC.
* Timestamps, IDs aleatórios e caminhos locais não devem aparecer.
* Diferenças entre resultado atual e esperado devem ser exibidas pelo `pytest`.

## Traceability Matrix

| Acceptance criterion | Scenario             | Rules or errors       | Fixture            | Expected output      | Test                   |
| -------------------- | -------------------- | --------------------- | ------------------ | -------------------- | ---------------------- |
| `AC-001`             | `SCN-001`            | `BR-001`, `INV-005`   | `FX-001`           | `EXP-001`            | `TEST-001`             |
| `AC-002`             | `SCN-002`            | `BR-008`              | `FX-002`           | `EXP-002`            | `TEST-002`             |
| `AC-003`             | `SCN-001`            | `BR-004`              | `FX-001`           | `EXP-001`            | `TEST-001`             |
| `AC-004`             | `SCN-003`            | `BR-004`              | `FX-003`           | `EXP-003`            | `TEST-003`             |
| `AC-005`             | `SCN-001`, `SCN-003` | `BR-005`              | `FX-001`, `FX-003` | `EXP-001`, `EXP-003` | `TEST-001`, `TEST-003` |
| `AC-006`             | `SCN-004`            | `BR-006`, `ERR-014`   | `FX-004`           | N/A                  | `TEST-004`             |
| `AC-007`             | `SCN-005`            | `BR-007`, `ERR-018`   | `FX-005`           | N/A                  | `TEST-005`             |
| `AC-008`             | `SCN-006`            | `BR-001`, `ERR-002`, `ERR-005`, `ERR-008`, `ERR-015` | `FX-006` e fixtures planejadas | N/A | `TEST-006` e testes planejados de registros ausentes |
| `AC-009`             | `SCN-007`            | `BR-002`, `ERR-020`   | `FX-007`           | N/A                  | `TEST-007`             |
| `AC-010`             | `SCN-009`            | `ERR-011`             | `FX-009`           | N/A                  | `TEST-009`             |
| `AC-011`             | `SCN-004`–`SCN-009`  | Error Contract        | `FX-004`–`FX-009`  | N/A                  | `TEST-004`–`TEST-009`  |
| `AC-012`             | `SCN-004`, `SCN-005` | `BR-009`, `INV-006`   | `FX-004`, `FX-005` | N/A                  | `TEST-004`, `TEST-005` |
| `AC-013`             | `SCN-008`            | General parsing rules | `FX-008`           | `EXP-004`            | `TEST-008`             |
| `AC-014`             | Todos                | `DEC-004`             | Todas              | Todas aplicáveis     | Suíte completa         |
| N/A                  | `SCN-010`            | `ERR-001`, `empty_input` | `FX-010`        | N/A                  | `TEST-010`             |

## Planned Scenario Expansion

### SCN-010 — Empty input

**Status:** planned

**Given**

* a entrada é uma string vazia;
* após a normalização, nenhuma linha lógica existe.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "empty_input"`;
* `error.message` é uma string não vazia e legível;
* nenhum resultado parcial é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-010`. O atributo `line_number` permanece na interface pública de `ReceiptValidationError`, mas o teste futuro não deverá verificar `error.line_number is None` nem qualquer número específico.

## Test Cases

### TEST-001 — Parse valid single-item receipt

**Covers:** `AC-001`, `AC-003`, `AC-005`, `SCN-001`

**Test level:** `golden`

**Fixture:** `FX-001`

**Expected output:** `EXP-001`

**Execution:**

1. Ler a fixture como texto UTF-8.
2. Chamar `parse_receipt(raw_text)`.
3. Ler o expected JSON.
4. Comparar o dicionário retornado com o conteúdo esperado.

**Pass condition:**

* a função retorna um dicionário;
* o resultado é exatamente igual a `EXP-001`;
* nenhum campo adicional é produzido;
* os valores monetários permanecem strings.

### TEST-002 — Preserve multiple-item order

**Covers:** `AC-002`, `SCN-002`, `BR-008`

**Test level:** `golden`

**Fixture:** `FX-002`

**Expected output:** `EXP-002`

**Pass condition:**

* os dois itens aparecem;
* `Arroz` permanece antes de `Café`;
* o resultado completo é igual a `EXP-002`.

### TEST-003 — Preserve decimal quantity

**Covers:** `AC-004`, `AC-005`, `SCN-003`

**Test level:** `golden`

**Fixture:** `FX-003`

**Expected output:** `EXP-003`

**Pass condition:**

* a quantidade é retornada como `"0.750"`;
* o total do item é `"7.50"`;
* o resultado completo é igual a `EXP-003`.

### TEST-004 — Reject inconsistent line total

**Covers:** `AC-006`, `AC-011`, `AC-012`, `SCN-004`

**Test level:** `unit`

**Fixture:** `FX-004`

**Expected error:** `line_total_mismatch`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "line_total_mismatch"`;
* `error.line_number == 3`;
* `error.message` é uma string não vazia;
* nenhum resultado parcial é retornado.

### TEST-005 — Reject inconsistent receipt total

**Covers:** `AC-007`, `AC-011`, `AC-012`, `SCN-005`

**Test level:** `unit`

**Fixture:** `FX-005`

**Expected error:** `receipt_total_mismatch`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "receipt_total_mismatch"`;
* `error.line_number == 5`;
* `error.message` é uma string não vazia;
* o total declarado é comparado com a soma dos totais dos itens;
* nenhum resultado parcial é retornado.

### TEST-006 — Reject missing item

**Covers:** `AC-008`, `AC-011`, `SCN-006`

**Test level:** `unit`

**Fixture:** `FX-006`

**Expected error:** `missing_item`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_item"`;
* `error.message` é uma string não vazia;
* a entrada não contém nenhum registro `ITEM`;
* `missing_item` é emitido antes de `receipt_total_mismatch` para `FX-006`;
* nenhum valor específico de `line_number` é exigido.

### TEST-007 — Reject invalid record order

**Covers:** `AC-009`, `AC-011`, `SCN-007`

**Test level:** `unit`

**Fixture:** `FX-007`

**Expected error:** `invalid_record_order`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_record_order"`;
* `error.line_number == 1`;
* `error.message` é uma string não vazia;
* a entrada começa com `DATE` em vez de `MERCHANT`;
* a ordem é validada antes da interpretação dos valores da linha.

### TEST-008 — Ignore blank lines and external whitespace

**Covers:** `AC-013`, `SCN-008`

**Test level:** `golden`

**Fixture:** `FX-008`

**Expected output:** `EXP-004`

**Pass condition:**

* linhas em branco são ignoradas;
* espaços antes dos prefixos e espaços adicionais depois deles são removidos;
* espaços em torno dos campos de `ITEM` são removidos;
* o resultado é exatamente igual a `EXP-004`;
* `merchant.name == "Mercado Exemplo"`;
* a descrição do item é `"Arroz"`;
* os valores numéricos permanecem strings.

### TEST-009 — Reject unsupported numeric format

**Covers:** `AC-010`, `AC-011`, `SCN-009`

**Test level:** `unit`

**Fixture:** `FX-009`

**Expected error:** `invalid_quantity`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_quantity"`;
* a quantidade `0,750` não é aceita;
* `error.message` é uma string não vazia;
* não existe exigência específica para `line_number`;
* o texto exato da mensagem não é comparado.

### TEST-010 — Reject empty input

**Status:** planned

**Covers:** `SCN-010`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-010`

**Expected error:** `empty_input`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "empty_input"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* nenhum requisito específico é imposto a `line_number`;
* nenhuma exceção técnica como `IndexError` escapa;
* nenhum resultado parcial é retornado.

`TEST-010` ainda não foi criado nem executado.

## Additional Error Validation

Os demais códigos de erro definidos na SPEC podem ser validados por testes parametrizados depois dos primeiros cenários.

Para `AC-008`, deve existir cobertura planejada para a ausência de cada registro obrigatório: `MERCHANT`, `DATE`, `ITEM` e `TOTAL`. `TEST-006` cobre inicialmente apenas `missing_item`; portanto, sua implementação isolada não torna `AC-008` completamente coberto. Testes adicionais para `missing_merchant`, `missing_date` e `missing_total` deverão completar essa cobertura em incrementos posteriores.

`empty_input` foi promovido da lista genérica futura para o planejamento formal `SCN-010` / `FX-010` / `TEST-010`. Esses artefatos permanecem planejados e ainda não foram implementados.

Exemplo de tabela futura:

| Error code                 | Synthetic input condition |
| -------------------------- | ------------------------- |
| `missing_merchant`         | entrada começa em `DATE`  |
| `duplicate_merchant`       | duas linhas `MERCHANT`    |
| `invalid_merchant`         | nome vazio                |
| `missing_date`             | ausência de `DATE`        |
| `duplicate_date`           | duas linhas `DATE`        |
| `invalid_date`             | `2026-02-30`              |
| `invalid_item_format`      | item com três campos      |
| `invalid_item_description` | descrição vazia           |
| `invalid_unit_price`       | preço `8.5`               |
| `invalid_line_total`       | total `-1.00`             |
| `missing_total`            | ausência de `TOTAL`       |
| `duplicate_total`          | duas linhas `TOTAL`       |
| `invalid_receipt_total`    | total `10,00`             |
| `unexpected_record`        | prefixo desconhecido      |

Esses testes não precisam ser todos implementados no primeiro incremento.

Eles devem ser adicionados em tarefas pequenas, mantendo rastreabilidade com a SPEC.

## Pendências de planejamento não bloqueantes

Antes da implementação completa dos cenários inválidos, uma decisão humana deverá definir a precedência quando uma mesma entrada puder corresponder a mais de um código de erro.

### Decisão localizada para SCN-010

Quando nenhuma linha lógica permanece após a normalização, `empty_input` deve ser emitido antes da validação de registros obrigatórios individuais.

Essa decisão se limita a entradas sem nenhuma linha lógica. Nesse caso, a entrada não deve ser classificada primeiro como `missing_merchant`, `missing_date`, `missing_item`, `missing_total` ou `invalid_record_order`. Nenhuma política geral é estabelecida para outras combinações de erros.

Exemplos que ainda exigem essa definição:

* `duplicate_total` versus `invalid_record_order`;
* `duplicate_merchant` versus `invalid_record_order`;
* registro obrigatório ausente versus registro equivalente presente fora de ordem.

Esta pendência não altera os códigos de erro existentes, não escolhe uma precedência e não bloqueia `SCN-001`. O comportamento aprovado para o primeiro cenário permanece inalterado.

## Invariant Validation

| Invariant | Validation method                                        | Tests                              |
| --------- | -------------------------------------------------------- | ---------------------------------- |
| `INV-001` | Teste de ausência de item.                               | `TEST-006`                         |
| `INV-002` | Testes parametrizados de quantidade e valores positivos. | futuros testes de erro             |
| `INV-003` | Comparação decimal exata do total do item.               | `TEST-004`                         |
| `INV-004` | Comparação decimal exata do total da nota.               | `TEST-005`                         |
| `INV-005` | Golden tests de saída completa.                          | `TEST-001`, `TEST-002`, `TEST-003` |
| `INV-006` | Testes que esperam exceção em vez de retorno.            | `TEST-004`, `TEST-005`             |

## Contract Validation

### Structured output contract

**Contract source:** `SPEC.md`, seção `Outputs`.

O teste deve validar:

* presença de `merchant`;
* presença de `merchant.name`;
* presença de `purchase_date`;
* presença de `items`;
* presença de pelo menos um item;
* presença de `receipt_total`;
* tipos definidos;
* ausência de campos adicionais;
* valores monetários como strings;
* quantidade como string;
* ordem dos itens preservada.

### Error contract

**Contract source:** `SPEC.md`, seção `Error Contract`.

O teste deve validar que `ReceiptValidationError` disponibiliza:

```text
code
message
line_number
```

O `code` é o identificador estável usado pelos testes.

A mensagem deve ser legível em inglês, mas o texto completo não precisa ser comparado quando o código já representar o contrato.

Implemented error contract:

* `line_total_mismatch`
* `receipt_total_mismatch`
* `missing_item`
* `invalid_record_order`
* `invalid_quantity`

`SCN-008` é um cenário válido e não adiciona código de erro. O contrato `invalid_quantity` está comprovado somente para a quantidade com vírgula coberta por `SCN-009`; essa evidência não estabelece suporte geral para outros formatos numéricos inválidos.

Fluxo atualmente comprovado pelos testes:

1. enumerar as linhas brutas preservando seus números originais;
2. remover whitespace externo de cada linha;
3. ignorar linhas vazias;
4. validar a sequência estrutural dos registros normalizados;
5. extrair e limpar os valores;
6. converter a quantidade para `Decimal`, traduzindo falhas para `invalid_quantity`;
7. converter os demais números necessários;
8. validar o total matemático de cada item;
9. acumular somente itens válidos;
10. verificar se existe pelo menos um item;
11. validar o total agregado;
12. produzir a saída estruturada.

A normalização mantém uma associação equivalente a `(original_line_number, normalized_text)`. Linhas vazias são removidas da sequência lógica, registros não vazios mantêm o número original, a validação estrutural usa o texto normalizado e os erros continuam reportando a posição original no arquivo.

Esse fluxo descreve o comportamento coberto pelos testes atuais, não uma arquitetura definitiva.

Em `FX-008`, os registros correspondem a:

* linha original 3 → `MERCHANT`;
* linha original 5 → `DATE`;
* linha original 7 → `ITEM`;
* linha original 9 → `TOTAL`.

`TEST-008` é um cenário válido e não valida diretamente exceções nessas linhas. A regressão dos cenários inválidos confirma `line_total_mismatch` na linha 3, `receipt_total_mismatch` na linha 5 e `invalid_record_order` na linha 1. A ausência completa do bloco de itens continua produzindo `missing_item`, não `invalid_record_order`.

Esse fluxo representa o comportamento comprovado pelos testes atuais, não uma arquitetura definitiva nem uma política geral para entradas ainda não cobertas.

## External Dependency Substitutes

| Dependency     | Substitute                           | Type              | Purpose                                          |
| -------------- | ------------------------------------ | ----------------- | ------------------------------------------------ |
| Portal fiscal  | Arquivos em `fixtures/inputs/`       | `fixture`         | Representar entradas sem rede.                   |
| QR Code        | Texto entregue diretamente ao parser | `stub conceptual` | Eliminar leitura externa nesta fase.             |
| Banco de dados | Dicionários Python em memória        | `fake conceptual` | Representar dados estruturados sem persistência. |

Nenhum framework formal de mocks é necessário nesta fase.

## Validation Commands

Todos os comandos abaixo devem ser executados a partir de:

```text
projects/nota-fiscal-insight
```

### Fast check — first scenario

```PowerShell
.\.venv\Scripts\python.exe -m pytest tests/test_receipt_parser.py::test_parse_valid_single_item_receipt -q
```

**Expected result after implementation:**

```text
1 passed
```

### Valid golden tests

```PowerShell
.\.venv\Scripts\python.exe -m pytest tests/test_receipt_parser.py -k "valid or whitespace" -q
```

**Expected result:** todos os cenários válidos implementados passam.

### Error tests

```PowerShell
.\.venv\Scripts\python.exe -m pytest tests/test_receipt_parser.py -k "reject" -q
```

**Expected result:** todas as entradas inválidas implementadas geram os códigos esperados.

### Project harness

```PowerShell
.\.venv\Scripts\python.exe -m pytest -q
```

**Expected result:** toda a suíte passa.

### Verbose failure investigation

```PowerShell
.\.venv\Scripts\python.exe -m pytest -vv
```

**Expected result:** em caso de falha, o cenário, a fixture e o assert divergente ficam visíveis.

## Initial TDD Sequence

O primeiro ciclo deve implementar somente `SCN-001`.

### Task 1 — Create FX-001 and EXP-001

Criar:

```text
fixtures/inputs/valid_single_item.txt
fixtures/expected/valid_single_item.json
```

Nenhum código de produção deve ser criado nesta tarefa.

### Task 2 — Create TEST-001

Criar o teste:

```text
test_parse_valid_single_item_receipt
```

O teste deve importar:

```python
parse_receipt
```

e comparar o resultado com `EXP-001`.

Neste momento, o teste deve falhar porque a implementação ainda não existe.

### Task 3 — Implement minimum parser

Criar apenas o código necessário para processar `FX-001`.

A implementação não deve antecipar todos os erros ou cenários futuros.

### Task 4 — Execute TEST-001

Executar:

```PowerShell
python -m pytest tests/test_receipt_parser.py::test_parse_valid_single_item_receipt -q
```

### Task 5 — Add next scenario

Somente depois que `TEST-001` passar e o diff for revisado, selecionar `SCN-002` ou outro incremento pequeno.

## Planned TDD Sequence for SCN-010

1. Formalizar `SCN-010` no harness.
2. Criar `FX-010` como arquivo de zero bytes.
3. Criar `TEST-010`.
4. Executar `TEST-010` e observar o Red.
5. Implementar uma guarda mínima após a normalização.
6. Executar a suíte completa.
7. Registrar as evidências.

Somente o primeiro passo está sendo realizado nesta tarefa. A fixture, o teste e a implementação permanecem pendentes.

## TDD Workflow

Para cada comportamento:

1. selecionar um cenário da SPEC;
2. confirmar a rastreabilidade;
3. criar ou revisar a fixture;
4. criar ou revisar o expected output;
5. escrever o teste;
6. executar e observar a falha esperada;
7. implementar o mínimo;
8. executar novamente;
9. executar a suíte relacionada;
10. refatorar somente com testes verdes;
11. revisar o diff;
12. realizar commit humano.

Se o teste passar antes da implementação esperada:

* investigar se o comportamento já existe;
* verificar se o teste é fraco;
* verificar se a fixture é adequada;
* não continuar automaticamente.

## Failure Reporting

O harness deve:

* retornar código de saída diferente de zero quando qualquer teste falhar;
* identificar o nome do teste;
* exibir esperado e atual;
* exibir o diff de estruturas ou JSON;
* preservar o traceback relevante;
* informar o código de erro atual quando ele divergir do esperado;
* não converter falhas em warnings;
* não ignorar testes automaticamente.

### Golden-file failure procedure

Quando o resultado divergir do expected output:

1. não atualizar o JSON automaticamente;
2. revisar a SPEC;
3. revisar a fixture;
4. revisar o expected output;
5. revisar a implementação;
6. determinar se existe regressão ou mudança legítima;
7. atualizar o expected somente depois de aprovação humana.

## Test Independence

Cada teste deve:

* carregar sua própria fixture;
* não depender de arquivos gerados por outro teste;
* não depender da ordem de execução;
* não modificar fixtures;
* não depender de horário atual;
* não depender de rede;
* não depender de banco;
* não manter estado global mutável;
* poder ser executado isoladamente.

## Determinism

| Source of instability | Control                                     |
| --------------------- | ------------------------------------------- |
| Current time          | Nenhum uso permitido.                       |
| Random values         | Nenhum uso permitido.                       |
| Ordering              | Ordem explicitamente preservada e validada. |
| Timezone              | Datas sem horário; timezone não aplicável.  |
| Locale                | Formato decimal fixo com ponto.             |
| Floating point        | Uso obrigatório de `Decimal`.               |
| Network               | Proibida.                                   |
| External state        | Substituído por fixtures.                   |

## Data Safety

* Todas as fixtures devem ser sintéticas.
* Nomes de estabelecimentos devem ser fictícios.
* Produtos e preços devem ser exemplos criados para teste.
* Nenhuma chave fiscal deve ser usada.
* Nenhum CPF deve ser usado.
* Nenhum endereço real deve ser usado.
* Nenhum QR Code real deve ser usado.
* Mensagens de erro não devem reproduzir a entrada inteira.
* `.venv/` e arquivos temporários não devem ser versionados.
* Dados reais anonimizados, caso sejam usados futuramente, devem permanecer fora do Git.

## Manual Checks

| Check                                      | Procedure                                                     | Pass condition                                                   | Reason not automated                            |
| ------------------------------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------- |
| Legibilidade inicial das mensagens de erro | Executar um teste inválido com `pytest -vv` e ler a mensagem. | A mensagem explica o problema sem reproduzir a entrada completa. | Qualidade textual exige revisão humana inicial. |
| Revisão dos expected outputs               | Abrir os JSONs e comparar com a SPEC.                         | Campos, tipos e valores correspondem ao contrato.                | Aprovação de golden exige julgamento humano.    |
| Revisão de privacidade                     | Inspecionar fixtures e diff antes do commit.                  | Nenhum dado real ou sensível está presente.                      | A classificação do dado exige revisão humana.   |

O comportamento central deve continuar coberto por testes automatizados.

## Coverage Boundaries

### Validated

Este harness valida:

* parsing do formato sintético controlado;
* schema da saída;
* preservação da ordem;
* strings monetárias;
* quantidades inteiras e decimais;
* cálculo de `line_total`;
* cálculo de `receipt_total`;
* erros estruturados;
* registros obrigatórios;
* ordem dos registros;
* espaços externos e linhas em branco;
* ausência de rede e serviços externos.

### Not validated

Este harness não valida:

* notas fiscais reais;
* HTML de NFC-e;
* leitura de QR Code;
* portais governamentais;
* vírgula como separador decimal;
* descontos;
* impostos;
* arredondamentos fiscais;
* grande volume de documentos;
* performance;
* banco de dados;
* API;
* frontend;
* autenticação;
* segurança de aplicação web.

### Residual risks

Mesmo com todos os testes passando:

* o formato sintético pode não representar irregularidades de notas reais;
* novas regras fiscais podem exigir outro modelo;
* o catálogo de erros pode precisar crescer;
* decisões de parsing podem precisar ser revisadas ao introduzir HTML real;
* a estrutura inicial pode exigir refatoração quando novos formatos forem adicionados.

## Harness Maintenance Rules

* Toda mudança de comportamento exige revisão da SPEC.
* Todo novo acceptance criterion deve possuir teste relacionado.
* Novas fixtures devem ser registradas no manifest.
* Fixtures sem teste devem ser removidas ou justificadas.
* Expected outputs não devem ser regenerados cegamente.
* Mudanças de schema devem ser tratadas como quebra de contrato.
* Testes não devem depender de detalhes internos sem necessidade.
* O harness deve continuar executável sem rede.
* O harness deve continuar usando apenas dados sintéticos.
* Refatorações devem preservar os mesmos testes.
* Códigos de erro devem permanecer estáveis enquanto a SPEC não mudar.

## Optional Validation Record

| Date         | Commit        | Command                                                                                                                                                                                               | Result            | Notes                                                           |
| ------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------- |
| `2026-07-21` | `uncommitted` | `.\projects\nota-fiscal-insight\.venv\Scripts\python.exe -m pytest .\projects\nota-fiscal-insight\tests\test_receipt_parser.py::test_parse_valid_single_item_receipt -q` | `fail (expected)` | `ModuleNotFoundError: No module named 'src.receipt_parser'`      |
| `2026-07-22` | `f7e19fc`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 and TEST-002 passed; SCN-001 and SCN-002 validated; multiple-item order preserved.` |
| `2026-07-22` | `491dd9c`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-003 passed; SCN-003 was already supported; quantity "0.750" preserved.` |
| `2026-07-22` | `68df7b2`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-004 passed; ReceiptValidationError and line_total_mismatch validated at line 3.` |
| `2026-07-22` | `ac51e95`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-005 passed; receipt_total_mismatch validated at line 5 using Decimal item totals.` |
| `2026-07-22` | `9124b85`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-006 passed; missing_item validated before receipt_total_mismatch for receipts without ITEM records.` |
| `2026-07-22` | `17c489c`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-007 passed; invalid_record_order validated at line 1 before record-specific parsing.` |
| `2026-07-22` | `52ef59a`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-008 passed; blank lines and external whitespace normalized while original line numbers remain preserved.` |
| `2026-07-23` | `2e3a921`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-009 passed; invalid quantity format translated from InvalidOperation to ReceiptValidationError with code invalid_quantity.` |

Esta tabela é opcional e não deve registrar todas as execuções locais.

## Current Implementation Evidence

* `FX-002` e `EXP-002` foram materializados e revisados.
* `TEST-002` foi criado.
* O Red foi observado enquanto a implementação estava limitada a um item.
* O Green foi obtido após o parser passar a aceitar uma sequência de registros `ITEM`.
* `TEST-001` e `TEST-002` passam juntos.
* A ordem original dos itens é preservada.
* `FX-003` e `EXP-003` foram materializados e revisados.
* `TEST-003` foi criado e passou na primeira execução contra o parser existente, caracterizando um Green preexisting.
* Nenhuma mudança no código de produção foi necessária para `SCN-003`.
* A quantidade `"0.750"` foi preservada lexicalmente como string.
* Os cálculos continuaram usando `Decimal`.
* `TEST-001`, `TEST-002` e `TEST-003` passam juntos.
* `FX-004` foi materializado e revisado.
* `TEST-004` foi inicialmente observado vermelho pela ausência de `ReceiptValidationError`.
* A classe pública `ReceiptValidationError` foi implementada com `code`, `message` e `line_number`.
* O erro `line_total_mismatch` passou a ser emitido para a inconsistência matemática do item.
* `line_number == 3` e uma mensagem não vazia foram validados.
* O item inválido não é retornado como resultado parcial.
* `TEST-001` a `TEST-004` passam juntos.
* `FX-005` foi materializado e revisado.
* `TEST-005` foi inicialmente observado vermelho porque o parser ainda não atendia ao contrato `receipt_total_mismatch`.
* O comportamento foi implementado reutilizando a classe pública `ReceiptValidationError`.
* O código `receipt_total_mismatch`, `line_number == 5` e uma mensagem não vazia foram validados.
* O total declarado `30.00` foi rejeitado porque a soma correta dos itens é `29.00`.
* A soma dos itens e a comparação do total usam `Decimal`.
* `TEST-001` a `TEST-005` passam juntos.
* `FX-006` foi materializado e revisado com `MERCHANT`, `DATE` e `TOTAL`, mas sem registros `ITEM`.
* `TEST-006` foi inicialmente observado vermelho porque o parser emitia `receipt_total_mismatch` em vez de `missing_item`.
* O Red demonstrou uma questão localizada de precedência para notas sem itens.
* O código `missing_item` e uma mensagem não vazia foram validados.
* `TEST-006` não define expectativa específica para `line_number`.
* A ausência de itens é verificada antes da comparação do total agregado.
* `TEST-001` a `TEST-006` passam juntos.
* `FX-007` foi materializado e revisado com a ordem inválida `DATE → MERCHANT → ITEM → TOTAL`.
* `TEST-007` foi inicialmente observado vermelho pela ausência do contrato `invalid_record_order`.
* O parser passou a validar o tipo esperado antes do parsing específico da linha.
* O código `invalid_record_order`, `line_number == 1` e uma mensagem não vazia foram validados.
* `TEST-001` a `TEST-007` passam juntos.
* `FX-008` e `EXP-004` foram materializados e revisados com linhas em branco e whitespace externo.
* `TEST-008` foi inicialmente observado vermelho pela ausência de suporte completo a whitespace externo e linhas em branco.
* Linhas vazias passaram a ser ignoradas, e o whitespace externo das linhas passou a ser removido.
* Os valores depois de `MERCHANT:`, `DATE:`, `ITEM:` e `TOTAL:` são limpos.
* Os quatro campos de `ITEM` são limpos individualmente.
* `"Mercado Exemplo"` e `"Arroz"` são retornados sem espaços externos, preservando espaços internos significativos.
* Quantidades e valores monetários continuam sendo retornados como strings.
* Os cálculos continuam usando `Decimal`.
* `TEST-001` a `TEST-008` passam juntos.
* `FX-009` foi materializado e revisado com a quantidade inválida `0,750`.
* `TEST-009` foi inicialmente observado vermelho porque uma falha técnica de conversão decimal escapava pela interface pública.
* `InvalidOperation` passou a ser capturada especificamente durante a conversão da quantidade e é preservada como causa por encadeamento de exceções.
* A falha é traduzida para a exceção pública `ReceiptValidationError` com o código `invalid_quantity` e uma mensagem não vazia.
* `TEST-009` não estabelece exigência específica para `line_number`.
* A quantidade válida `"0.750"` continua preservada lexicalmente como string.
* `TEST-001` a `TEST-009` passam juntos.

Implemented and green:

* `TEST-001` / `SCN-001`
* `TEST-002` / `SCN-002`
* `TEST-003` / `SCN-003`
* `TEST-004` / `SCN-004`
* `TEST-005` / `SCN-005`
* `TEST-006` / `SCN-006`
* `TEST-007` / `SCN-007`
* `TEST-008` / `SCN-008`
* `TEST-009` / `SCN-009`

Planned but not yet implemented:

* `TEST-010` / `SCN-010`

### Resumo dos artefatos cobertos

Valid golden scenarios:

* `SCN-001`
* `SCN-002`
* `SCN-003`
* `SCN-008`

Structured-error scenarios:

* `SCN-004`
* `SCN-005`
* `SCN-006`
* `SCN-007`
* `SCN-009`

### Estado do harness inicial

Os nove cenários definidos no harness inicial estão materializados e possuem testes automatizados. A suíte completa está verde, e o harness inicial agora serve como rede de segurança para revisão e refatoração.

`SCN-010` inaugura uma expansão incremental das lacunas já definidas na SPEC. `TEST-010` ainda não foi criado nem executado e não faz parte dos nove testes verdes do harness inicial.

Novos comportamentos devem ser introduzidos por novos cenários e testes, sem expansão silenciosa dos contratos atuais. O escopo permanece limitado ao formato textual controlado definido pela SPEC e não representa suporte completo a notas fiscais reais.

## Harness Readiness Checklist

### Scope and strategy

* [x] O System Under Test está claramente definido.
* [x] Os limites de entrada e saída estão explícitos.
* [x] As estratégias de teste são proporcionais ao projeto.
* [x] O harness não tenta validar funcionalidades futuras.
* [x] As dependências relevantes estão identificadas.
* [x] A stack mínima está definida.

### Traceability

* [x] Todo acceptance criterion possui forma de validação planejada.
* [x] Todos os cenários principais estão relacionados a testes.
* [x] Regras e invariants importantes possuem cobertura identificável.
* [x] Erros centrais possuem testes planejados.
* [x] Edge cases relevantes possuem validação planejada.
* [x] A matriz de rastreabilidade está preenchida.

### Fixtures and expected outputs

* [x] As fixtures iniciais estão especificadas.
* [x] Todas as fixtures planejadas usam dados sintéticos.
* [x] Fixtures válidas e inválidas possuem finalidade clara.
* [x] Expected outputs estão definidos para cenários válidos.
* [x] Expected outputs são determinísticos.
* [x] Golden files podem ser revisados por humanos.
* [x] A atualização automática de goldens está proibida.
* [x] Os arquivos iniciais de fixture do primeiro ciclo foram criados no repositório.
* [x] Os expected outputs iniciais do primeiro ciclo foram criados no repositório.

### Execution

* [x] Os comandos de validação estão documentados.
* [x] O diretório de execução está definido.
* [x] Dependências e pré-requisitos estão explícitos.
* [x] A condição de falha é clara.
* [x] Mensagens de falha devem mostrar divergências.
* [x] Os comandos necessários ao primeiro ciclo `SCN-001` foram testados no ambiente local.

### Test quality

* [x] Os testes serão independentes.
* [x] Os testes serão reproduzíveis.
* [x] Fontes de instabilidade foram controladas.
* [x] O comportamento central não depende apenas de revisão manual.
* [x] Os testes validarão comportamento observável.
* [x] O primeiro teste foi criado.
* [x] O primeiro teste foi observado falhando pelo motivo esperado.

### Safety and boundaries

* [x] Nenhum dado sensível está planejado.
* [x] Dependências externas foram substituídas por fixtures.
* [x] Os limites do harness estão documentados.
* [x] Riscos residuais estão explícitos.
* [x] O harness não cria efeitos reais.
* [x] O conteúdo final de `FX-001` e `EXP-001` foi revisado antes do commit.

## Harness Approval

* **Reviewed by:** project owner
* **Decision:** `approved`
* **Notes:** `FX-001` e `EXP-001` foram materializados e revisados; Python 3.13, a `.venv` e o `pytest` foram validados; `TEST-001` foi criado; sua execução produziu o Red esperado por ausência de `src.receipt_parser`. O harness está aprovado para iniciar a implementação mínima de `SCN-001`.

## Implementation Entry Gate

Antes do primeiro código de produção, confirmar:

* [x] `SPEC.md` está `ready`.
* [x] Este harness está `ready`.
* [x] O primeiro cenário escolhido é `SCN-001`.
* [x] `FX-001` está especificada.
* [x] `EXP-001` está especificado.
* [x] `TEST-001` está definido.
* [x] O comando do primeiro teste está documentado.
* [x] A fixture `FX-001` existe no repositório.
* [x] O expected output `EXP-001` existe no repositório.
* [x] O ambiente virtual foi criado.
* [x] O `pytest` foi instalado.
* [x] O comando de `TEST-001` foi executado e produziu a falha Red esperada antes da implementação.
