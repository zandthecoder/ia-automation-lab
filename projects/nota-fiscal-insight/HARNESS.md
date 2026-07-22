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
* nenhum resultado parcial é retornado.

### TEST-006 — Reject missing item

**Covers:** `AC-008`, `AC-011`, `SCN-006`

**Test level:** `unit`

**Fixture:** `FX-006`

**Expected error:** `missing_item`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_item"`.

### TEST-007 — Reject invalid record order

**Covers:** `AC-009`, `AC-011`, `SCN-007`

**Test level:** `unit`

**Fixture:** `FX-007`

**Expected error:** `invalid_record_order`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_record_order"`;
* a linha problemática é identificada.

### TEST-008 — Ignore blank lines and external whitespace

**Covers:** `AC-013`, `SCN-008`

**Test level:** `golden`

**Fixture:** `FX-008`

**Expected output:** `EXP-004`

**Pass condition:**

* linhas em branco são ignoradas;
* espaços externos são removidos;
* o resultado é exatamente igual a `EXP-004`.

### TEST-009 — Reject unsupported numeric format

**Covers:** `AC-010`, `AC-011`, `SCN-009`

**Test level:** `unit`

**Fixture:** `FX-009`

**Expected error:** `invalid_quantity`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_quantity"`;
* o formato com vírgula não é aceito.

## Additional Error Validation

Os demais códigos de erro definidos na SPEC podem ser validados por testes parametrizados depois dos primeiros cenários.

Para `AC-008`, deve existir cobertura planejada para a ausência de cada registro obrigatório: `MERCHANT`, `DATE`, `ITEM` e `TOTAL`. `TEST-006` cobre inicialmente apenas `missing_item`; portanto, sua implementação isolada não torna `AC-008` completamente coberto. Testes adicionais para `missing_merchant`, `missing_date` e `missing_total` deverão completar essa cobertura em incrementos posteriores.

Exemplo de tabela futura:

| Error code                 | Synthetic input condition |
| -------------------------- | ------------------------- |
| `empty_input`              | string vazia              |
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

Esta tabela é opcional e não deve registrar todas as execuções locais.

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
