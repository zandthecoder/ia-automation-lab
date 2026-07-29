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
| `FX-011` | `fixtures/inputs/invalid_item_format.txt`       | `SCN-011`        | Linha `ITEM` com somente três campos.           |              no |
| `FX-012` | `fixtures/inputs/invalid_item_description.txt`  | `SCN-012`        | Linha `ITEM` com descrição vazia e quatro campos. |            no |
| `FX-013` | `fixtures/inputs/invalid_unit_price.txt`        | `SCN-013`        | Preço unitário com somente uma casa decimal.    |              no |
| `FX-014` | `fixtures/inputs/negative_line_total.txt`       | `SCN-014`        | Total do item negativo.                         |              no |
| `FX-015` | `fixtures/inputs/invalid_receipt_total_format.txt` | `SCN-015`     | Total da nota usando vírgula como separador decimal. |          no |
| `FX-016` | `fixtures/inputs/invalid_line_total_format.txt` | `SCN-016`        | `line_total` com conteúdo não convertível.      |              no |
| `FX-017` | `fixtures/inputs/non_convertible_unit_price.txt` | `SCN-017`       | `unit_price` superficialmente válido, mas não convertível. |     no |
| `FX-018` | `fixtures/inputs/invalid_missing_total.txt` | `SCN-018`              | Nota sem o registro obrigatório `TOTAL`.        |              no |
| `FX-019` | `fixtures/inputs/invalid_duplicate_total.txt` | `SCN-019`            | Nota válida com segunda ocorrência reconhecida de `TOTAL`. |              no |
| `FX-020` | `fixtures/inputs/invalid_missing_merchant.txt` | `SCN-020`           | Nota válida nos demais registros, sem qualquer `MERCHANT`. |              no |
| `FX-021` | `fixtures/inputs/invalid_missing_date.txt` | `SCN-021`               | Nota válida nos demais registros, sem qualquer `DATE`. |                  no |
| `FX-022` | `fixtures/inputs/invalid_duplicate_merchant.txt` | `SCN-022`          | Nota válida nos demais registros, com segunda ocorrência reconhecida de `MERCHANT`. | no |
| `FX-023` | `fixtures/inputs/invalid_duplicate_date.txt` | `SCN-023`              | Nota válida nos demais registros, com segunda ocorrência reconhecida de `DATE`. | no |

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

**Status:** materialized

O arquivo `fixtures/inputs/invalid_empty_input.txt` possui exatamente `0 bytes`, sem quebra de linha ou qualquer outro conteúdo. Sua leitura textual produz `""`.

`FX-010` representa somente uma string completamente vazia. Uma entrada contendo apenas whitespace não faz parte de `SCN-010` e poderá ser avaliada separadamente no futuro.

### FX-011 — ITEM with invalid field count

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-11
ITEM: Arroz | 2 | 8.50
TOTAL: 17.00
```

Uma linha `ITEM` válida contém exatamente quatro campos:

```text
description | quantity | unit_price | line_total
```

Em `FX-011`, a linha reconhecida como `ITEM` contém somente:

```text
description | quantity | unit_price
```

A fixture isola a quantidade incorreta de campos: `MERCHANT`, `DATE`, ordem, prefixo `ITEM:` e formato de `TOTAL` permanecem válidos para o formato controlado. Como `line_total` está ausente, o parser não deve chegar à conversão numérica ou à validação matemática do item, e não se avalia se `TOTAL: 17.00` corresponde a um item que não pode ser construído validamente.

### FX-012 — ITEM with empty description

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-12
ITEM: | 2 | 8.50 | 17.00
TOTAL: 17.00
```

`FX-012` isola somente a descrição vazia. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida e existe exatamente um registro `ITEM`. A linha `ITEM` possui exatamente quatro campos separados por `|`, mas o primeiro campo se torna `""` depois de `strip()`.

Os demais valores permanecem válidos: `quantity == "2"`, `unit_price == "8.50"`, `line_total == "17.00"`, `2 × 8.50 == 17.00` e `TOTAL: 17.00` é consistente. Portanto, a entrada não deve ser classificada como `invalid_item_format`, `invalid_quantity`, `line_total_mismatch`, `receipt_total_mismatch`, `missing_item` ou `invalid_record_order`.

O arquivo `fixtures/inputs/invalid_item_description.txt` foi materializado e revisado.

### FX-013 — ITEM with invalid unit-price format

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-13
ITEM: Arroz | 2 | 8.5 | 17.00
TOTAL: 17.00
```

`FX-013` isola somente o formato lexical de `unit_price`. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida, a linha `ITEM` possui exatamente quatro campos, a descrição é `"Arroz"` e a quantidade `"2"` é válida.

`unit_price` é `"8.5"`, enquanto `line_total` e `TOTAL` são `"17.00"`. Matematicamente, `2 × 8.5 == 17.0`; portanto, não existe divergência matemática intencional e `line_total_mismatch` não deve ser a causa principal.

O arquivo `fixtures/inputs/invalid_unit_price.txt` foi materializado e revisado.

### FX-014 — ITEM with negative line total

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-14
ITEM: Arroz | 2 | 8.50 | -1.00
TOTAL: -1.00
```

`FX-014` isola a regra semântica de `line_total` negativo. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida, existe exatamente um registro `ITEM`, a linha possui quatro campos, a descrição é `"Arroz"`, a quantidade `"2"` é válida e `unit_price == "8.50"` possui formato válido.

`Decimal("-1.00")` é convertível e `"-1.00"` possui duas casas decimais, mas o valor é negativo e viola a regra de domínio. A divergência matemática `2 × 8.50 == 17.00` e `17.00 != -1.00` é inevitável e serve para comprovar que `invalid_line_total` deve preceder `line_total_mismatch`.

`TOTAL: -1.00` foi escolhido para manter consistência entre o `line_total` declarado e o total declarado da nota. O parser falha durante o processamento do item, antes da validação agregada; `SCN-014` não formaliza `invalid_receipt_total`.

O arquivo `fixtures/inputs/negative_line_total.txt` foi materializado e revisado.

### FX-015 — Receipt total with unsupported decimal separator

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-15
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10,00
```

`FX-015` isola somente o formato do total agregado. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida e existe exatamente um registro `ITEM` com quatro campos. `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"` são válidos, com `1 × 10.00 == 10.00`.

O total acumulado dos itens é `10.00`; somente `TOTAL` contém `"10,00"`. A vírgula não pertence ao formato numérico controlado, e não há divergência matemática intencional nem outro erro estrutural ou local do item.

O arquivo materializado é `fixtures/inputs/invalid_receipt_total_format.txt`. Ele não reutiliza nem sobrescreve `fixtures/inputs/invalid_receipt_total.txt`, que permanece associado a `FX-005` / `SCN-005` / `receipt_total_mismatch`.

`FX-015` foi materializada e revisada.

### FX-016 — ITEM with non-convertible line total

**Status:** materialized

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-16
ITEM: Arroz | 1 | 10.00 | abc
TOTAL: 10.00
```

`FX-016` isola somente a conversão de `line_total`. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida, existe exatamente um registro `ITEM` com quatro campos, `description == "Arroz"`, `quantity == "1"` é válida e `unit_price == "10.00"` possui formato válido e é convertível. Somente `line_total == "abc"` não é convertível.

`TOTAL == "10.00"` possui formato válido e não tenta reproduzir o conteúdo inválido de `line_total`. O parser falha durante o processamento do item, antes de acumular qualquer valor ou alcançar o total agregado. Não existe outro erro estrutural intencional.

O arquivo `fixtures/inputs/invalid_line_total_format.txt` foi materializado e revisado.

### FX-017 — ITEM with non-convertible unit price

**Status:** materialized

Conteúdo:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-17
ITEM: Arroz | 1 | ab.cd | 10.00
TOTAL: 10.00
```

`FX-017` isola somente a conversão de `unit_price`. `MERCHANT` e `DATE` estão presentes, a ordem estrutural é válida, existe exatamente um registro `ITEM` com quatro campos, `description == "Arroz"` e `quantity == "1"` é válida. `unit_price == "ab.cd"` possui uma parte antes do ponto, um ponto e exatamente dois caracteres depois do ponto, mas não é convertível para `Decimal`.

`line_total == "10.00"` é convertível e não negativo, e `TOTAL == "10.00"` também é convertível. Não existe outro erro estrutural intencional. O parser falha na conversão do preço antes de converter `line_total` ou executar a comparação matemática.

O arquivo `fixtures/inputs/non_convertible_unit_price.txt` foi materializado e revisado.

### FX-018 — Receipt without TOTAL

**Status:** materialized

Conteúdo:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-18
ITEM: Arroz | 1 | 10.00 | 10.00
```

`FX-018` possui exatamente três linhas e termina após o registro `ITEM`, sem linha `TOTAL:`. `MERCHANT` e `DATE` estão presentes e na ordem correta, existe exatamente um `ITEM` com quatro campos, `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"`. Quantidade, preço e total do item são positivos, convertíveis e matematicamente consistentes: `1 × 10.00 = 10.00`.

A fixture não contém valor zero ou negativo, conteúdo não convertível, separador decimal alternativo, linha desconhecida, registro duplicado, `TOTAL` duplicado nem registro posterior a `TOTAL`. Ela isola somente a ausência completa do registro obrigatório `TOTAL`; não representa total presente com formato inválido, total divergente da soma dos itens ou registro presente fora de ordem. O arquivo `fixtures/inputs/invalid_missing_total.txt` foi materializado e revisado.

### FX-019 — Receipt with duplicate TOTAL

**Status:** materialized and reviewed

**File:** `fixtures/inputs/invalid_duplicate_total.txt`

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-19
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10.00
TOTAL: 10.00
```

A entrada possui exatamente cinco linhas. O primeiro `TOTAL` está na linha 4, e a segunda ocorrência reconhecida está na linha 5. Essa posição evidencia a duplicidade, mas `SCN-019` não estabelece contrato obrigatório para `line_number`.

`MERCHANT` e `DATE` aparecem exatamente uma vez e na ordem correta. Existe exatamente um `ITEM`, com quatro campos, descrição `"Arroz"`, quantidade `"1"`, preço unitário `"10.00"` e total da linha `"10.00"`. Os valores são positivos e convertíveis, e `1 × 10.00 == 10.00`.

Os dois valores de `TOTAL` são individualmente válidos, idênticos e correspondem ao acumulado `10.00`. Não existe `receipt_total_mismatch`, `invalid_receipt_total`, prefixo desconhecido, linha sem prefixo, registro obrigatório ausente nem duplicidade de `MERCHANT` ou `DATE`. O único defeito intencional é a segunda ocorrência de `TOTAL`.

O segundo `TOTAL` possui prefixo conhecido e conteúdo numericamente válido. Ele não é um registro inesperado nem deve ser reduzido a uma classificação genérica de ordem: representa uma violação da cardinalidade singleton de `TOTAL`.

```text
segunda ocorrência reconhecida de TOTAL
→ duplicate_total
```

`FX-019` foi materializada em `fixtures/inputs/invalid_duplicate_total.txt` e revisada.

### FX-020 — Receipt without MERCHANT

**Status:** materialized and reviewed

**File:** `fixtures/inputs/invalid_missing_merchant.txt`

Conteúdo materializado:

```text
DATE: 2026-07-20
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10.00
```

A entrada possui exatamente três linhas e não contém o prefixo `MERCHANT` em nenhuma posição. Ela não usa `MERCHANT:` vazio, que representaria um registro presente com conteúdo inválido, não ausência estrutural.

Existe exatamente uma `DATE`, um `ITEM` e um `TOTAL`. `DATE` contém `"2026-07-20"`. A linha `ITEM` possui três separadores `|` e quatro campos: `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"`. Os valores são positivos e convertíveis, e `1 × 10.00 == 10.00`.

`TOTAL == "10.00"` é convertível e corresponde ao acumulado. Não existe duplicidade, prefixo desconhecido, conteúdo depois de `TOTAL` nem outro defeito estrutural ou numérico intencional. Somente `MERCHANT` está ausente.

```text
zero ocorrências de MERCHANT
→ missing_merchant
```

`FX-020` foi materializada e revisada no repositório.

### FX-021 — Receipt without DATE

**Status:** materialized and reviewed

**File:** `fixtures/inputs/invalid_missing_date.txt`

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10.00
```

A entrada planejada possui exatamente três linhas. Existe exatamente um `MERCHANT`, um `ITEM` e um `TOTAL`, e não existe prefixo `DATE` em nenhuma posição. `MERCHANT` possui conteúdo não vazio, não há registros duplicados, prefixos desconhecidos, conteúdo depois de `TOTAL` ou outro defeito estrutural intencional.

A linha `ITEM` possui três separadores `|` e quatro campos: `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"`. Os valores são positivos e convertíveis, `1 × 10.00 == 10.00`, e `TOTAL == "10.00"` corresponde ao item. Somente `DATE` está ausente.

```text
zero ocorrências de DATE
→ missing_date
```

`FX-021` foi materializada e revisada no repositório. Uma linha `DATE:` vazia não faz parte desta fixture porque representaria um registro estruturalmente presente com conteúdo vazio.

### FX-022 — Receipt with duplicate MERCHANT

**Status:** materialized and reviewed

**File:** `fixtures/inputs/invalid_duplicate_merchant.txt`

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
MERCHANT: Mercado Exemplo
DATE: 2026-07-22
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10.00
```

A entrada possui exatamente cinco linhas. As linhas 1 e 2 são duas ocorrências estruturalmente reconhecidas de `MERCHANT`, ambas com conteúdo não vazio e idêntico (`"Mercado Exemplo"`). Usar valores iguais isola a cardinalidade maior que um, sem introduzir interpretação sobre estabelecimentos conflitantes.

Existe exatamente uma `DATE`, um `ITEM` e um `TOTAL`. O `ITEM` possui três separadores `|` e quatro campos válidos: `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"`. Os valores são positivos e convertíveis, `1 × 10.00 == 10.00`, e `TOTAL == "10.00"` corresponde ao acumulado.

Não existe registro obrigatório ausente, `DATE` ou `TOTAL` duplicado, prefixo desconhecido, conteúdo depois de `TOTAL` ou outro defeito estrutural, numérico ou matemático intencional. Somente a segunda ocorrência de `MERCHANT` é defeituosa.

```text
duas ocorrências reconhecidas de MERCHANT
→ duplicate_merchant
```

`FX-022` existe no repositório e foi revisada. Uma linha `MERCHANT:` vazia não faz parte desta fixture porque representaria conteúdo inválido, não duas ocorrências individualmente válidas.

### FX-023 — Receipt with duplicate DATE

**Status:** materialized and reviewed

**File:** `fixtures/inputs/invalid_duplicate_date.txt`

Conteúdo materializado:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-23
DATE: 2026-07-23
ITEM: Arroz | 1 | 10.00 | 10.00
TOTAL: 10.00
```

A entrada possui exatamente cinco linhas. Existe um único `MERCHANT` na linha 1; as linhas 2 e 3 são duas ocorrências estruturalmente reconhecidas de `DATE`, ambas com conteúdo não vazio, válido e idêntico (`"2026-07-23"`). Usar valores iguais isola a cardinalidade maior que um, sem introduzir interpretação sobre datas conflitantes.

Existe exatamente um `ITEM` e um `TOTAL`. O `ITEM` possui três separadores `|` e quatro campos válidos: `description == "Arroz"`, `quantity == "1"`, `unit_price == "10.00"` e `line_total == "10.00"`. Os valores são positivos e convertíveis, `1 × 10.00 == 10.00`, e `TOTAL == "10.00"` corresponde ao acumulado.

Não existe `MERCHANT` ou `TOTAL` duplicado, registro obrigatório ausente, prefixo desconhecido, conteúdo depois de `TOTAL` ou outro defeito estrutural, numérico ou matemático intencional. Somente a segunda ocorrência de `DATE` é defeituosa.

Removendo apenas a terceira linha, a entrada restante possui a sequência válida `MERCHANT → DATE → ITEM → TOTAL`, com todas as cardinalidades e cálculos corretos.

```text
duas ocorrências reconhecidas de DATE
→ duplicate_date
```

`FX-023` existe no repositório e foi revisada. Uma linha `DATE:` vazia não faz parte desta fixture porque representaria conteúdo inválido, não duas ocorrências individualmente válidas.

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
| N/A                  | `SCN-011`            | `ERR-009`, `invalid_item_format` | `FX-011` | N/A               | `TEST-011`             |
| N/A                  | `SCN-012`            | `ERR-010`, `invalid_item_description` | `FX-012` | N/A          | `TEST-012`             |
| N/A                  | `SCN-013`            | `ERR-012`, `invalid_unit_price` | `FX-013` | N/A               | `TEST-013`             |
| N/A                  | `SCN-014`            | `ERR-013`, `invalid_line_total` | `FX-014` | N/A               | `TEST-014`             |
| N/A                  | `SCN-015`            | `ERR-017`, `invalid_receipt_total` | `FX-015` | N/A            | `TEST-015`             |
| N/A                  | `SCN-016`            | `ERR-013`, `invalid_line_total` | `FX-016` | N/A               | `TEST-016`             |
| N/A                  | `SCN-017`            | `ERR-012`, `invalid_unit_price` | `FX-017` | N/A               | `TEST-017`             |
| `AC-008`             | `SCN-018`            | `ERR-015`, `missing_total` | `FX-018` | N/A                  | `TEST-018`             |
| N/A                  | `SCN-019`            | `ERR-016`, `BR-001`, `duplicate_total` | `FX-019` | N/A          | `TEST-019`             |
| `AC-008`             | `SCN-020`            | `ERR-002`, `BR-001`, `missing_merchant` | `FX-020` | N/A         | `TEST-020`             |
| `AC-008`             | `SCN-021`            | `ERR-005`, `BR-001`, `missing_date` | `FX-021` | N/A             | `TEST-021`             |
| N/A                  | `SCN-022`            | `ERR-003`, `BR-001`, `duplicate_merchant` | `FX-022` | N/A        | `TEST-022`             |
| N/A                  | `SCN-023`            | `ERR-006`, `BR-001`, `duplicate_date` | `FX-023` | N/A            | `TEST-023`             |

## Scenario Expansion

### SCN-010 — Empty input

**Status:** implemented and green

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

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-010`. O atributo `line_number` permanece na interface pública de `ReceiptValidationError`, mas `TEST-010` não verifica `error.line_number is None` nem qualquer número específico.

### SCN-011 — ITEM with invalid field count

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém somente três campos separados por `|`;
* o campo `line_total` está ausente;
* os demais registros são sintaticamente válidos.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_item_format"`;
* `error.message` é uma string não vazia e legível;
* nenhuma exceção técnica como `ValueError` escapa;
* nenhum item parcial é adicionado ou acumulado;
* nenhum resultado parcial é retornado.

O cenário valida somente o caso de três campos, não o conteúdo numérico nem outras quantidades de campos. O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-011`; `TEST-011` não verifica `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

### SCN-012 — ITEM with empty description

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém exatamente quatro campos separados por `|`;
* o campo `description` fica vazio depois da remoção de whitespace externo;
* `quantity`, `unit_price` e `line_total` são válidos;
* o total da nota é consistente com os valores declarados.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_item_description"`;
* `error.message` é uma string não vazia e legível;
* nenhuma conversão numérica é necessária antes de detectar o erro;
* nenhum item parcial é adicionado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-012`. O atributo permanece na interface pública de `ReceiptValidationError`, mas `TEST-012` não verifica `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

`SCN-012` é distinto de `SCN-011`. A linha `ITEM: Arroz | 2 | 8.50` possui somente três campos e produz `invalid_item_format`. A linha `ITEM: | 2 | 8.50 | 17.00` possui exatamente quatro campos, mas a descrição fica vazia após `strip()` e deve produzir `invalid_item_description`. A quantidade correta de separadores não torna a descrição válida.

Conceitualmente, tanto `""` quanto `"   "` são descrições vazias depois de `strip()`. Entretanto, `FX-012` formaliza somente `ITEM: | 2 | 8.50 | 17.00`; uma variação contendo apenas espaços no campo não será materializada nem parametrizada neste cenário.

### SCN-013 — ITEM with invalid unit-price format

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém exatamente quatro campos;
* a descrição não está vazia;
* a quantidade é válida;
* `unit_price == "8.5"`;
* `line_total == "17.00"`;
* `receipt_total == "17.00"`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_unit_price"`;
* `error.message` é uma string não vazia e legível;
* nenhuma exceção técnica escapa;
* nenhuma validação matemática é usada para aceitar o formato inválido;
* nenhum item parcial é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado.

`Decimal("8.5")` é convertível, mas a string `"8.5"` não possui as duas casas decimais exigidas pelo formato monetário controlado. `SCN-013` valida a representação lexical do preço, não apenas sua conversibilidade numérica:

```text
8.50 → formato válido
8.5  → formato inválido para SCN-013
```

O cenário formaliza somente `"8.5"` e não classifica a entrada como `invalid_quantity`, `line_total_mismatch`, `receipt_total_mismatch`, `invalid_item_format` ou `invalid_item_description`.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-013`. O atributo permanece na interface pública de `ReceiptValidationError`, mas `TEST-013` não verifica `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

### SCN-014 — ITEM with negative line total

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém exatamente quatro campos;
* a descrição não está vazia;
* a quantidade é válida;
* `unit_price` possui formato válido;
* `line_total == "-1.00"`;
* `receipt_total == "-1.00"` para manter consistência entre os totais declarados.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_line_total"`;
* `error.message` é uma string não vazia e legível;
* nenhuma exceção técnica escapa;
* o valor negativo é rejeitado antes da comparação `quantity × unit_price`;
* `line_total_mismatch` não substitui `invalid_line_total`;
* nenhum item parcial é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado.

`Decimal("-1.00")` é convertível e a string `"-1.00"` possui duas casas decimais. O valor é inválido porque o total do item é negativo. Trata-se de uma validação semântica de domínio, não de erro de separador, quantidade de casas, conversão decimal ou inconsistência matemática como causa principal.

Os contratos permanecem separados:

```text
ITEM: Arroz | 2 | 8.50 | 16.00
→ line_total_mismatch

ITEM: Arroz | 2 | 8.50 | -1.00
→ invalid_line_total
```

No primeiro caso, o valor é positivo, convertível, possui duas casas e diverge de `2 × 8.50`. No segundo, o valor é convertível e possui duas casas, mas é negativo; por isso, `invalid_line_total` deve ser emitido antes da comparação matemática.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-014`. O atributo permanece na interface pública de `ReceiptValidationError`, mas `TEST-014` não verifica `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

#### Distinção entre formato, valor semântico e consistência matemática

Formato textual, valor semântico e consistência matemática permanecem contratos separados:

* `SCN-013`: `unit_price == "8.5"` é convertível, mas não possui a representação monetária exigida e produz `invalid_unit_price`;
* `SCN-014`: `line_total == "-1.00"` é convertível e possui duas casas decimais, mas é semanticamente inválido por ser negativo e produz `invalid_line_total`;
* `SCN-004`: `ITEM: Arroz | 2 | 8.50 | 16.00` contém um total positivo e válido isoladamente, mas inconsistente com `2 × 8.50`, e produz `line_total_mismatch`.

Esses contratos não são combinados: formato é validado antes do valor semântico, e a consistência matemática somente é avaliada depois que os valores envolvidos forem individualmente válidos.

### SCN-015 — Receipt total with unsupported decimal separator

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* existe exatamente um registro `ITEM` válido;
* descrição, quantidade, preço unitário e total do item são válidos;
* o total calculado dos itens é `10.00`;
* o campo `TOTAL` contém `"10,00"`;
* o único defeito intencional é o uso da vírgula como separador decimal no total da nota.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_receipt_total"`;
* `error.message` é uma string não vazia e legível;
* `decimal.InvalidOperation` não escapa da interface pública;
* `receipt_total_mismatch` não substitui `invalid_receipt_total`;
* nenhum resultado parcial é retornado.

`"10,00"` não usa o separador decimal aceito pelo formato controlado. O cenário representa uma falha de formato e conversão no campo agregado `TOTAL`; não representa soma incorreta, total negativo, ausência ou duplicidade de `TOTAL`, ordem estrutural inválida nem erro dentro de `ITEM`.

A falha técnica é traduzida para o contrato público:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_receipt_total")
```

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-015`. `TEST-015` não deverá verificar `error.line_number == 4`, `error.line_number is None` nem qualquer outro valor.

#### Distinção de `receipt_total_mismatch`

##### Formato inválido

```text
TOTAL: 10,00
```

Em `SCN-015`, a conversão decimal falha, o resultado é `invalid_receipt_total` e nenhuma comparação matemática é executada.

##### Total válido, mas divergente

`SCN-005` cobre um total válido, convertível e formatado com ponto decimal, mas inconsistente:

```text
ITEM: Arroz | 2 | 8.50 | 17.00
ITEM: Café | 1 | 12.00 | 12.00
TOTAL: 30.00
```

A soma correta é `29.00`, portanto a conversão funciona, mas a comparação falha e o resultado é `receipt_total_mismatch`.

### SCN-016 — ITEM with non-convertible line total

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém exatamente quatro campos;
* a descrição não está vazia;
* a quantidade é válida;
* `unit_price` possui formato válido e é convertível;
* `line_total` contém `"abc"`;
* `TOTAL` contém `"10.00"`;
* o único defeito intencional é o conteúdo não convertível de `line_total`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_line_total"`;
* `error.message` é uma string não vazia e legível;
* `decimal.InvalidOperation` não escapa da interface pública;
* `line_total_mismatch` não é emitido;
* nenhum item inválido é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado.

`Decimal("abc")` produz `decimal.InvalidOperation`. Essa exceção técnica não deve escapar da interface pública; a tradução esperada é:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_line_total")
```

`SCN-016` representa uma falha de conversão. Não representa valor negativo, divergência matemática, quantidade incorreta de campos, descrição vazia, quantidade inválida, preço unitário inválido nem erro no total agregado.

#### Relação com SCN-014

`SCN-014` e `SCN-016` compartilham o código público `invalid_line_total`, mas representam causas diferentes:

* em `SCN-014`, `Decimal("-1.00")` funciona, o valor é negativo e a falha é semântica;
* em `SCN-016`, `Decimal("abc")` produz `InvalidOperation`, não existe valor decimal para validar e a falha ocorre na conversão.

Não existe código separado para distinguir essas duas causas, e o texto exato da mensagem não precisa ser igual.

#### Relação com `line_total_mismatch`

`line_total_mismatch` somente pode ocorrer depois que `line_total` foi convertido com sucesso e validado semanticamente. `SCN-004` comprova esse contrato com:

```text
ITEM: Arroz | 2 | 8.50 | 16.00
```

Para `ITEM: Arroz | 1 | 10.00 | abc`, o resultado esperado é `invalid_line_total`. A comparação `quantity × unit_price == line_total` não pode ser executada porque não existe um `Decimal` válido para `line_total`.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-016`. `TEST-016` não deverá verificar `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

### SCN-017 — ITEM with non-convertible unit price

**Status:** implemented and green

**Given**

* a nota possui `MERCHANT`, `DATE`, `ITEM` e `TOTAL` na ordem correta;
* a linha `ITEM` contém exatamente quatro campos;
* a descrição não está vazia;
* a quantidade é válida;
* `unit_price` contém `"ab.cd"`;
* `line_total` contém `"10.00"`;
* `TOTAL` contém `"10.00"`;
* o único defeito intencional é o conteúdo não convertível de `unit_price`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_unit_price"`;
* `error.message` é uma string não vazia e legível;
* `decimal.InvalidOperation` não escapa da interface pública;
* `line_total_mismatch` não é emitido;
* nenhum item inválido é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado.

`"ab.cd"` possui uma parte antes do ponto, um ponto e exatamente dois caracteres depois do ponto. Mesmo assim, `Decimal("ab.cd")` produz `decimal.InvalidOperation`; a forma superficial não garante conteúdo numérico. A tradução esperada é:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_unit_price")
```

#### Relação com SCN-013

`SCN-013` e `SCN-017` compartilham o código público `invalid_unit_price`, mas protegem caminhos diferentes:

* em `SCN-013`, `unit_price == "8.5"` é convertível, mas possui somente uma casa decimal e é rejeitado pela guarda lexical antes da conversão;
* em `SCN-017`, `unit_price == "ab.cd"` satisfaz a forma superficial verificada pela guarda, mas não pode ser convertido para `Decimal`.

Os cenários permanecem independentes e não exigem mensagens idênticas.

#### Relação com `line_total_mismatch`

Em `SCN-017`, não existe `Decimal` válido para `unit_price`, portanto o parser não pode executar `quantity × unit_price == line_total`. O resultado esperado é `invalid_unit_price`, não `line_total_mismatch`.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-017`. `TEST-017` não deverá verificar `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

### SCN-018 — Receipt without TOTAL

**Status:** implemented and green

**Given**

* a nota possui exatamente um `MERCHANT`, um `DATE` e um `ITEM`, nessa ordem;
* o item contém os quatro campos obrigatórios;
* a descrição do item é válida;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* a quantidade e os valores monetários do item são válidos, positivos e convertíveis;
* `quantity × unit_price == line_total`;
* nenhum registro `TOTAL` está presente;
* não existem linhas desconhecidas nem registros duplicados;
* o único defeito intencional é a ausência de `TOTAL`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_total"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `receipt_total_mismatch` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado ou parcial é retornado.

O cenário formaliza `ERR-015`, contribui para `AC-008` e protege a exigência de exatamente um registro `TOTAL` definida por `BR-001`. O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-018`; `TEST-018` não deverá verificar `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

#### Distinção entre erros relacionados a TOTAL

* `invalid_record_order`: registros válidos estão presentes, mas fora da ordem obrigatória, como `DATE` antes de `MERCHANT`;
* `missing_total`: um prefixo estruturalmente válido termina após `ITEM`, sem qualquer registro `TOTAL`;
* `invalid_receipt_total`: `TOTAL` está presente, mas seu valor não possui formato aceito, como `"10,00"`;
* `receipt_total_mismatch`: `TOTAL` está presente e é convertível, mas diverge da soma dos `line_total`.

### SCN-019 — Receipt with duplicate TOTAL

**Status:** implemented and green

**Covers:** `ERR-016`, `BR-001`, `duplicate_total`, Error Contract

**Given**

* a entrada contém exatamente um `MERCHANT` e exatamente uma `DATE`;
* `MERCHANT` aparece antes de `DATE`;
* existe exatamente um `ITEM`, depois de `DATE`;
* o item possui quatro campos;
* `description == "Arroz"`;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* `quantity × unit_price == line_total`;
* existe um primeiro registro `TOTAL` com `"10.00"`;
* existe um segundo registro `TOTAL` com `"10.00"`;
* ambos os totais são convertíveis, idênticos e correspondem ao valor acumulado;
* o único defeito intencional é a segunda ocorrência de `TOTAL`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "duplicate_total"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `unexpected_record` não é emitido;
* `invalid_receipt_total` não é emitido;
* `receipt_total_mismatch` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-019`. Embora a segunda ocorrência exista fisicamente na linha 5, `TEST-019` não exige `error.line_number == 5`, `error.line_number is None` nem qualquer outro valor.

#### Structural distinctions

Ordem inválida pressupõe cardinalidades corretas e uma sequência proibida:

```text
DATE
MERCHANT
ITEM
TOTAL
→ invalid_record_order
```

Em `SCN-019`, a primeira sequência completa já possui um `TOTAL`, e a segunda ocorrência repete um registro singleton reconhecido:

```text
MERCHANT
DATE
ITEM
TOTAL
TOTAL
→ duplicate_total
```

Por isso, `duplicate_total` prevalece sobre `invalid_record_order` para a ocorrência repetida.

`unexpected_record` corresponde a prefixo desconhecido, conteúdo sem prefixo válido ou linha não classificável:

```text
COUPON: 5.00
→ unexpected_record
```

`TOTAL: 10.00` continua sendo um registro reconhecido quando repetido; portanto, a segunda ocorrência produz `duplicate_total`, não `unexpected_record`.

`invalid_receipt_total` exige conteúdo inválido ou não convertível, como `TOTAL: 10,00`. Em `SCN-019`, ambos os totais usam `"10.00"` e são individualmente válidos.

`receipt_total_mismatch` exige divergência entre um total convertível e a soma dos itens. Em `SCN-019`, `quantity × unit_price == line_total == 10.00`, e os dois totais também contêm `"10.00"`. A falha é estrutural e deve ser classificada antes da comparação matemática.

O parser não deve escolher silenciosamente o primeiro ou o último `TOTAL`, ignorar a segunda ocorrência, retornar normalmente porque os valores são idênticos nem reduzir a validação à comparação matemática.

#### Protected structural precedence

```text
empty_input
→ reconhecer ocorrências estruturais de TOTAL
→ detectar mais de uma ocorrência
→ duplicate_total
→ validar ordem quando há no máximo um TOTAL
→ invalid_record_order
→ processar itens
→ missing_total quando não existe TOTAL
→ validar conteúdo do único TOTAL
→ invalid_receipt_total
→ receipt_total_mismatch
```

Para `FX-019`, a entrada não está vazia e `TOTAL` aparece duas vezes. A duplicidade é identificada antes da classificação genérica de ordem e antes das validações numéricas e matemáticas do total.

Essa sequência descreve o contrato público e não exige uma implementação em múltiplas passagens.

`SCN-019` define somente um defeito estrutural principal isolado. Ele não estabelece precedência para combinações com `MERCHANT` ou `DATE` ausente, prefixo desconhecido, `TOTAL` não convertível, totais divergentes, item inválido ou outra duplicidade estrutural.

#### Relationship with SCN-018

```text
SCN-018: zero ocorrências de TOTAL
→ missing_total

SCN-019: duas ocorrências de TOTAL
→ duplicate_total
```

Os dois cenários protegem cardinalidades diferentes do mesmo registro singleton e não devem ser combinados nem parametrizados.

#### Proven TOTAL cardinality

O harness executável protege três caminhos independentes:

```text
zero ocorrências de TOTAL
→ missing_total
→ SCN-018 / TEST-018

uma ocorrência de TOTAL
→ validação normal do total agregado
→ saída válida, invalid_receipt_total ou receipt_total_mismatch

mais de uma ocorrência de TOTAL
→ duplicate_total
→ SCN-019 / TEST-019
```

`missing_total` representa ausência; `duplicate_total` representa cardinalidade maior que um; e `invalid_record_order` permanece reservado, nos cenários protegidos, a registros reconhecidos com cardinalidade válida em sequência proibida. Para a mesma ocorrência repetida, a classificação específica `duplicate_total` prevalece sobre a classificação genérica de ordem.

`TOTAL: 10.00` possui prefixo reconhecido mesmo quando repetido. Portanto, a segunda ocorrência não é `unexpected_record`. Esse contrato permanece especificado, mas ainda não está protegido por cenário executável.

Essa evidência é específica à cardinalidade de `TOTAL` e não constitui uma implementação genérica das cardinalidades de todos os registros.

### SCN-020 — Receipt without MERCHANT

**Status:** implemented and green

**Covers:** `ERR-002`, `BR-001`, `AC-008`, `missing_merchant`, Error Contract

**Given**

* a entrada não está vazia;
* não existe nenhum registro `MERCHANT`;
* existe exatamente uma `DATE` com `"2026-07-20"`;
* existe exatamente um `ITEM` com quatro campos;
* `description == "Arroz"`;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* `quantity × unit_price == line_total`;
* existe exatamente um `TOTAL` com `"10.00"`;
* o total corresponde à soma dos itens;
* todos os prefixos presentes são reconhecidos;
* o único defeito intencional é a ausência global de `MERCHANT`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_merchant"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `missing_date` não é emitido;
* `missing_item` não é emitido;
* `missing_total` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-020`. A ausência global de `MERCHANT` não corresponde necessariamente a uma linha física, e `TEST-020` não exige `error.line_number == 1`, `error.line_number is None` nem qualquer outro valor.

#### Absence versus empty content

```text
DATE
ITEM
TOTAL
→ missing_merchant
```

Nenhum registro `MERCHANT` foi encontrado. Isso é diferente de:

```text
MERCHANT:
DATE
ITEM
TOTAL
```

Nesse segundo caso, o registro existe fisicamente, mas seu conteúdo está vazio. `SCN-020` não formaliza esse contrato.

#### Absence versus invalid order

```text
DATE
ITEM
TOTAL
→ missing_merchant
```

Quando a contagem global de `MERCHANT` é zero, a ausência específica prevalece sobre `invalid_record_order`.

```text
DATE
MERCHANT
ITEM
TOTAL
→ invalid_record_order
```

Quando `MERCHANT` existe exatamente uma vez, mas está deslocado, sua cardinalidade está correta e a sequência é proibida.

`SCN-020` contém `DATE`, um `ITEM` válido e um `TOTAL` válido. Portanto, não representa `missing_date`, `missing_item` ou `missing_total`.

#### Protected structural precedence

```text
empty_input
→ reconhecer os tipos dos registros
→ verificar registros obrigatórios ausentes
→ missing_merchant quando não existe MERCHANT
→ verificar duplicidades
→ verificar ordem quando a cardinalidade é válida
→ invalid_record_order
→ validar conteúdo
```

Para `FX-020`, a entrada não está vazia, os três registros presentes possuem prefixos reconhecidos e a contagem global de `MERCHANT` é zero. `missing_merchant` deve ser emitido antes da classificação genérica de ordem, sem retorno normal.

Essa sequência descreve o contrato e não exige uma implementação em múltiplas passagens. A SPEC contém o código e a política, e `SCN-020` agora comprova esse comportamento no harness executável.

O cenário isola um único defeito. Não define precedência para combinações com `DATE`, `ITEM` ou `TOTAL` ausente; `TOTAL` duplicado; prefixo desconhecido; item inválido; erro numérico; ou `MERCHANT` duplicado.

### SCN-021 — Receipt without DATE

**Status:** implemented and green

**Covers:** `ERR-005`, `BR-001`, `AC-008`, `missing_date`, Error Contract

**Given**

* a entrada não está vazia;
* existe exatamente um `MERCHANT` com `"Mercado Exemplo"`;
* não existe qualquer registro `DATE`;
* existe exatamente um `ITEM` com quatro campos;
* `description == "Arroz"`;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* `quantity × unit_price == line_total`;
* existe exatamente um `TOTAL` com `"10.00"`;
* o total corresponde à soma dos itens;
* todos os prefixos presentes são reconhecidos;
* o único defeito intencional é a ausência global de `DATE`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_date"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `missing_merchant` não é emitido;
* `missing_item` não é emitido;
* `missing_total` não é emitido;
* `duplicate_total` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-021`. A ausência global de `DATE` não corresponde necessariamente a uma linha física, e `TEST-021` não exige `error.line_number == 2`, `error.line_number is None` nem qualquer outro valor.

#### Absence versus empty content

```text
MERCHANT
ITEM
TOTAL
→ missing_date
```

Nenhum registro `DATE` foi encontrado. Isso é diferente de:

```text
MERCHANT
DATE:
ITEM
TOTAL
```

Nesse segundo caso, o registro existe estruturalmente, mas seu conteúdo está vazio. `SCN-021` não formaliza esse contrato.

#### Absence versus invalid order

```text
MERCHANT
ITEM
TOTAL
→ missing_date
```

Quando a contagem global de `DATE` é zero, a ausência específica prevalece sobre `invalid_record_order`.

```text
MERCHANT
ITEM
DATE
TOTAL
→ invalid_record_order
```

Quando `DATE` existe exatamente uma vez, mas está deslocada, sua cardinalidade está correta e a sequência é proibida.

`SCN-021` contém um `MERCHANT`, um `ITEM` e um `TOTAL` válidos. Portanto, não representa `missing_merchant`, `missing_item`, `missing_total` ou `duplicate_total`. O fato de `ITEM` ocupar a segunda linha não significa que o item esteja ausente.

#### Protected structural precedence

```text
empty_input
→ reconhecer os tipos dos registros
→ verificar registros obrigatórios ausentes
→ missing_merchant quando não existe MERCHANT
→ missing_date quando não existe DATE
→ verificar duplicidades
→ verificar ordem quando as cardinalidades são válidas
→ invalid_record_order
→ validar conteúdos
```

Para `FX-021`, a entrada não está vazia, `MERCHANT`, `ITEM` e `TOTAL` possuem tipos reconhecidos, `MERCHANT` está presente e a contagem global de `DATE` é zero. `missing_date` deve ser emitido antes da classificação genérica de ordem, sem retorno normal.

Essa sequência descreve o contrato, sem exigir uma arquitetura específica. `SCN-021` não estabelece precedência para uma entrada que omita simultaneamente `MERCHANT` e `DATE`, nem para combinações com `ITEM` ou `TOTAL` ausente, `TOTAL` duplicado, prefixo desconhecido, item inválido, erro numérico, `DATE` duplicada ou `MERCHANT` duplicado.

### SCN-022 — Receipt with duplicate MERCHANT

**Status:** implemented and green

**Covers:** `ERR-003`, `BR-001`, `duplicate_merchant`, Error Contract

**Given**

* a entrada não está vazia;
* existem duas ocorrências estruturalmente reconhecidas de `MERCHANT`;
* ambas contêm `"Mercado Exemplo"` e possuem conteúdo não vazio;
* existe exatamente uma `DATE` com `"2026-07-22"`;
* existe exatamente um `ITEM` com quatro campos;
* `description == "Arroz"`;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* `quantity × unit_price == line_total`;
* existe exatamente um `TOTAL` com `"10.00"`;
* o total corresponde à soma dos itens;
* todos os prefixos são reconhecidos;
* o único defeito intencional é a segunda ocorrência de `MERCHANT`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "duplicate_merchant"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `missing_merchant` não é emitido;
* `unexpected_record` não é emitido;
* `missing_date` não é emitido;
* `missing_item` não é emitido;
* `missing_total` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-022`. A segunda ocorrência está na linha 2, mas `TEST-022` não exige `error.line_number == 2`, `error.line_number is None` nem qualquer outro valor.

#### Duplication versus absence

```text
DATE
ITEM
TOTAL
→ missing_merchant
```

Zero ocorrências são protegidas por `SCN-020` / `TEST-020`.

```text
MERCHANT
MERCHANT
DATE
ITEM
TOTAL
→ duplicate_merchant
```

Duas ocorrências são planejadas por `SCN-022` / `TEST-022`; `missing_merchant` não se aplica.

#### Duplication versus invalid order

```text
DATE
MERCHANT
ITEM
TOTAL
→ invalid_record_order
```

Nesse caso existe um único `MERCHANT`, com cardinalidade válida e posição proibida.

```text
MERCHANT
MERCHANT
DATE
ITEM
TOTAL
→ duplicate_merchant
```

Nesse caso o primeiro registro ocupa a posição correta e o segundo repete um singleton. A duplicidade específica deve prevalecer sobre a mensagem genérica de `DATE` esperada na linha 2.

#### Duplication versus empty content and unknown records

Uma linha `MERCHANT:` vazia representa um registro presente com conteúdo inválido e não é coberta por `SCN-022`. Em `FX-022`, as duas ocorrências contêm `"Mercado Exemplo"`.

`MERCHANT:` é um prefixo estrutural conhecido também na segunda ocorrência. Portanto, a repetição produz `duplicate_merchant`, não `unexpected_record`; este último permanece reservado para prefixos desconhecidos ou linhas não classificáveis.

`FX-022` contém uma única `DATE`, um único `ITEM` válido e um único `TOTAL` válido. Não representa `missing_date`, `duplicate_date`, `missing_total`, `duplicate_total`, `invalid_receipt_total` ou `receipt_total_mismatch`.

#### Protected structural precedence

```text
empty_input
→ missing_merchant quando MERCHANT possui zero ocorrências
→ missing_date quando DATE possui zero ocorrências
→ duplicate_merchant quando MERCHANT possui mais de uma ocorrência
→ duplicate_total quando TOTAL possui mais de uma ocorrência
→ invalid_record_order quando as cardinalidades protegidas são válidas
→ validar conteúdos
```

Para `FX-022`, a entrada não está vazia, `MERCHANT` e `DATE` estão presentes e `MERCHANT` possui duas ocorrências. `duplicate_merchant` deve ser emitido antes da validação posicional da linha 2; nenhum item ou total precisa ser processado e nenhum resultado normal é produzido.

A posição relativa entre `duplicate_merchant` e `duplicate_total` não é generalizada para entradas que contenham ambos os defeitos. `SCN-022` também não define precedência para `DATE` ausente ou duplicada, `ITEM` ou `TOTAL` ausente, prefixo desconhecido, item inválido, erro numérico, mais de dois `MERCHANT` ou estabelecimentos com valores diferentes.

#### Structural review decision

`TASK-REVIEW-007` concluiu:

```text
Decision: Keep explicit guards
```

A implementação de `SCN-022` reutilizou o reconhecimento explícito existente de `MERCHANT`, acrescentou somente a guarda de cardinalidade necessária e manteve a precedência visível em `parse_receipt`. Helper, índice estrutural, enum, classe de registro, máquina de estados e refatoração das demais guardas permaneceram fora do escopo.

### SCN-023 — Receipt with duplicate DATE

**Status:** implemented and green

**Covers:** `ERR-006`, `BR-001`, `duplicate_date`, Error Contract

**Given**

* a entrada não está vazia;
* existe exatamente um `MERCHANT` com `"Mercado Exemplo"`;
* existem duas ocorrências estruturalmente reconhecidas de `DATE`;
* ambas contêm `"2026-07-23"` e possuem conteúdo não vazio;
* existe exatamente um `ITEM` com quatro campos;
* `description == "Arroz"`;
* `quantity == "1"`;
* `unit_price == "10.00"`;
* `line_total == "10.00"`;
* `quantity × unit_price == line_total`;
* existe exatamente um `TOTAL` com `"10.00"`;
* o total corresponde à soma dos itens;
* todos os prefixos são reconhecidos;
* o único defeito intencional é a segunda ocorrência de `DATE`.

**When**

* `parse_receipt(raw_text)` é executado.

**Then**

* `ReceiptValidationError` é lançada;
* `error.code == "duplicate_date"`;
* `error.message` é uma string não vazia e legível;
* `invalid_record_order` não é emitido;
* `missing_date` não é emitido;
* `unexpected_record` não é emitido;
* `missing_merchant` não é emitido;
* `duplicate_merchant` não é emitido;
* `missing_item` não é emitido;
* `missing_total` não é emitido;
* o parser não retorna normalmente;
* nenhum resultado estruturado é retornado.

O texto exato da mensagem e o valor de `line_number` não fazem parte do contrato de `SCN-023`. A segunda ocorrência está na linha 3, mas `TEST-023` não exige `error.line_number == 3`, `error.line_number is None` nem qualquer outro valor.

#### Duplication versus absence

```text
MERCHANT
ITEM
TOTAL
→ missing_date
```

Zero ocorrências são protegidas por `SCN-021` / `TEST-021`.

```text
MERCHANT
DATE
DATE
ITEM
TOTAL
→ duplicate_date
```

Duas ocorrências são planejadas por `SCN-023` / `TEST-023`; `missing_date` não se aplica.

#### Duplication versus invalid order

```text
MERCHANT
ITEM
DATE
TOTAL
→ invalid_record_order
```

Nesse caso existe uma única `DATE`, com cardinalidade válida e posição proibida.

```text
MERCHANT
DATE
DATE
ITEM
TOTAL
→ duplicate_date
```

Nesse caso a primeira `DATE` ocupa a posição correta e a segunda repete um singleton. A duplicidade específica deve prevalecer sobre a mensagem genérica de `ITEM` esperado na linha 3.

#### Duplication versus content

Uma linha `DATE:` vazia representa um registro presente com conteúdo inválido e não é coberta por `SCN-023`. Em `FX-023`, as duas ocorrências contêm `"2026-07-23"`.

Os dois valores são idênticos para evitar uma interpretação adicional sobre datas conflitantes. A cardinalidade maior que um é suficiente para a rejeição; `SCN-023` não define comportamento específico para duas datas diferentes.

`DATE:` é um prefixo estrutural conhecido também na segunda ocorrência. Portanto, a repetição produz `duplicate_date`, não `unexpected_record`; este último permanece reservado para prefixos desconhecidos ou linhas não classificáveis.

#### Relation to other records

`FX-023` contém um único `MERCHANT`, portanto não representa `missing_merchant` nem `duplicate_merchant`.

Também contém um único `ITEM` válido e um único `TOTAL` válido. Não representa `missing_item`, `missing_total`, `duplicate_total`, `invalid_receipt_total`, `receipt_total_mismatch` ou erros numéricos e matemáticos do item.

Nenhuma `DATE` deve ser escolhida, sobrescrita, ignorada ou combinada silenciosamente. A cardinalidade inválida impede qualquer saída normal.

#### Protected structural precedence

```text
empty_input
→ missing_merchant quando MERCHANT possui zero ocorrências
→ missing_date quando DATE possui zero ocorrências
→ duplicate_merchant quando MERCHANT possui mais de uma ocorrência
→ duplicate_date quando DATE possui mais de uma ocorrência
→ duplicate_total quando TOTAL possui mais de uma ocorrência
→ invalid_record_order quando as cardinalidades protegidas são válidas
→ validar conteúdos
```

Para `FX-023`, a entrada não está vazia, `MERCHANT` e `DATE` estão presentes e `DATE` possui duas ocorrências. `duplicate_date` deve ser emitido antes da validação posicional da linha 3; nenhum item ou total precisa ser processado e nenhum resultado normal é produzido.

Essa sequência não estabelece precedência geral para entradas com duas duplicidades ou outros defeitos independentes simultâneos. `SCN-023` também não define comportamento para `MERCHANT` ausente ou duplicado, `ITEM` ou `TOTAL` ausente, `TOTAL` duplicado, prefixo desconhecido, item inválido, erro numérico, mais de duas `DATE` ou datas diferentes.

#### Structural review decision

`TASK-REVIEW-007` permanece vigente:

```text
Decision: Keep explicit guards
```

A implementação de `SCN-023` reutilizou `date_records`, acrescentou somente a guarda explícita de cardinalidade necessária e manteve a precedência visível em `parse_receipt`. Uma nova busca por `DATE:`, helper, índice estrutural, enum, classe de registro, máquina de estados e refatoração das demais guardas permaneceram fora do escopo.

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

**Status:** implemented and green

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

### TEST-011 — Reject ITEM with invalid field count

**Status:** implemented and green

**Covers:** `SCN-011`, `ERR-009`, `invalid_item_format`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-011`

**Expected error:** `invalid_item_format`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_item_format"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* nenhuma exceção técnica como `ValueError` escapa;
* nenhum resultado parcial é retornado;
* nenhum item inválido é adicionado à lista ou ao total acumulado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-012 — Reject ITEM with empty description

**Status:** implemented and green

**Covers:** `SCN-012`, `ERR-010`, `invalid_item_description`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-012`

**Expected error:** `invalid_item_description`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_item_description"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* nenhuma outra exceção técnica escapa;
* nenhum item inválido é retornado;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-013 — Reject unit price without two decimal places

**Status:** implemented and green

**Covers:** `SCN-013`, `ERR-012`, `invalid_unit_price`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-013`

**Expected error:** `invalid_unit_price`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_unit_price"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* nenhuma exceção técnica escapa;
* o parser não retorna normalmente;
* nenhum item inválido é retornado;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-014 — Reject negative line total

**Status:** implemented and green

**Covers:** `SCN-014`, `ERR-013`, `invalid_line_total`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-014`

**Expected error:** `invalid_line_total`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_line_total"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* nenhuma exceção técnica escapa;
* `line_total_mismatch` não é emitido para `FX-014`;
* o parser não retorna normalmente;
* nenhum item inválido é retornado;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-015 — Reject receipt total with comma decimal separator

**Status:** implemented and green

**Covers:** `SCN-015`, `ERR-017`, `invalid_receipt_total`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-015`

**Expected error:** `invalid_receipt_total`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_receipt_total"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `decimal.InvalidOperation` não escapa;
* o parser não retorna normalmente;
* `receipt_total_mismatch` não é emitido;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-016 — Reject non-convertible line total

**Status:** implemented and green

**Covers:** `SCN-016`, `ERR-013`, `invalid_line_total`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-016`

**Expected error:** `invalid_line_total`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_line_total"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `decimal.InvalidOperation` não escapa;
* `line_total_mismatch` não é emitido;
* o parser não retorna normalmente;
* nenhum item inválido é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-017 — Reject non-convertible unit price

**Status:** implemented and green

**Covers:** `SCN-017`, `ERR-012`, `invalid_unit_price`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-017`

**Expected error:** `invalid_unit_price`

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "invalid_unit_price"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `decimal.InvalidOperation` não escapa;
* `line_total_mismatch` não é emitido;
* o parser não retorna normalmente;
* nenhum item inválido é retornado;
* nenhum valor é acumulado;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-018 — Reject receipt without TOTAL

**Status:** implemented and green

**Covers:** `SCN-018`, `ERR-015`, `AC-008`, `missing_total`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-018`

**Expected error:** `missing_total`

**Execution:**

1. Carregar `invalid_missing_total.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `ReceiptValidationError` é lançada;
* `error.code == "missing_total"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* a ausência de `TOTAL` não é classificada como `invalid_record_order`;
* nenhuma conversão nem comparação do total agregado é tentada;
* o parser não retorna normalmente;
* nenhum resultado parcial é retornado;
* nenhum requisito específico é imposto a `line_number`.

### TEST-019 — Reject receipt with duplicate TOTAL

**Status:** implemented and green

**Covers:** `SCN-019`, `ERR-016`, `BR-001`, `duplicate_total`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-019`

**Expected error:** `duplicate_total`

**Execution:**

1. Carregar `invalid_duplicate_total.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `error.code == "duplicate_total"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `invalid_record_order` não é aceito;
* `unexpected_record` não é aceito;
* o parser não retorna normalmente;
* nenhum total é escolhido silenciosamente;
* nenhuma ocorrência duplicada é ignorada;
* nenhum resultado estruturado é retornado;
* nenhum requisito específico é imposto a `line_number`.

O teste aceita somente `duplicate_total`, sem uma lista de códigos alternativos. Ele não estabelece condição de aprovação para `line_number`.

**Observed Red before implementation:**

```text
ReceiptValidationError
code: invalid_record_order
message: Record is out of order; expected ITEM on line 4.
line_number: 4
```

Antes da implementação, `TEST-019` ficou vermelho ao comparar o código esperado `duplicate_total` com o código observado `invalid_record_order`. Esse Red demonstrou que a entrada já era rejeitada, mas a duplicidade era identificada indiretamente como ordem inválida. Depois da guarda de cardinalidade, o teste passou com `duplicate_total`.

### TEST-020 — Reject receipt without MERCHANT

**Status:** implemented and green

**Covers:** `SCN-020`, `ERR-002`, `BR-001`, `AC-008`, `missing_merchant`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-020`

**Expected error:** `missing_merchant`

**Execution:**

1. Carregar `invalid_missing_merchant.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `error.code == "missing_merchant"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `invalid_record_order` não é aceito;
* o parser não retorna normalmente;
* nenhum resultado estruturado é produzido;
* nenhum requisito específico é imposto a `line_number`.

O teste aceita somente `missing_merchant`, sem códigos alternativos.

**Observed Red before implementation:**

```text
ReceiptValidationError
code: invalid_record_order
message: Record is out of order; expected MERCHANT on line 1.
line_number: 1
```

`TEST-020` ficou vermelho ao comparar `missing_merchant` com `invalid_record_order`. Esse Red demonstrou que o parser já rejeitava a entrada e validava a primeira posição esperada, mas ainda não distinguia ausência global de deslocamento. Depois da guarda de ausência global, o teste passou com `missing_merchant`.

### TEST-021 — Reject receipt without DATE

**Status:** implemented and green

**Covers:** `SCN-021`, `ERR-005`, `BR-001`, `AC-008`, `missing_date`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-021`

**Expected error:** `missing_date`

**Execution:**

1. Carregar `invalid_missing_date.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `error.code == "missing_date"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `invalid_record_order` não é aceito;
* `missing_merchant` não é aceito;
* o parser não retorna normalmente;
* nenhum resultado estruturado é produzido;
* nenhum requisito específico é imposto a `line_number`.

O teste aceita somente `missing_date`, sem códigos alternativos.

**Observed Red before implementation:**

```text
ReceiptValidationError
code: invalid_record_order
message: Record is out of order; expected DATE on line 2.
line_number: 2
```

`TEST-021` ficou vermelho ao comparar `missing_date` com `invalid_record_order`. Esse Red demonstrou que o parser já rejeitava a entrada e validava a segunda posição esperada, mas ainda não distinguia ausência global de deslocamento para `DATE`. Depois da guarda de ausência global, o teste passou com `missing_date`.

### TEST-022 — Reject receipt with duplicate MERCHANT

**Status:** implemented and green

**Covers:** `SCN-022`, `ERR-003`, `BR-001`, `duplicate_merchant`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-022`

**Expected error:** `duplicate_merchant`

**Execution:**

1. Carregar `invalid_duplicate_merchant.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `error.code == "duplicate_merchant"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `invalid_record_order` não é aceito;
* `missing_merchant` não é aceito;
* `unexpected_record` não é aceito;
* o parser não retorna normalmente;
* nenhum resultado estruturado é produzido;
* nenhum requisito específico é imposto a `line_number`.

O teste aceitará somente `duplicate_merchant`, sem códigos alternativos.

**Observed Red before implementation:**

```text
ReceiptValidationError
code: invalid_record_order
message: Record is out of order; expected DATE on line 2.
line_number: 2
```

Esse Red demonstrou que o parser já rejeitava a segunda ocorrência de `MERCHANT`, mas ainda a classificava indiretamente como uma violação posicional. A guarda explícita de cardinalidade passou a emitir `duplicate_merchant` antes da validação posicional, sem criar requisito específico para `line_number`.

### TEST-023 — Reject receipt with duplicate DATE

**Status:** implemented and green

**Covers:** `SCN-023`, `ERR-006`, `BR-001`, `duplicate_date`, Error Contract

**Test level:** `unit`

**Fixture:** `FX-023`

**Expected error:** `duplicate_date`

**Execution:**

1. Carregar `invalid_duplicate_date.txt` como texto UTF-8.
2. Chamar somente `parse_receipt(raw_text)`.
3. Exigir e capturar `ReceiptValidationError`.

**Pass condition:**

* `error.code == "duplicate_date"`;
* `error.message` é uma string;
* `error.message.strip() != ""`;
* `invalid_record_order` não é aceito;
* `missing_date` não é aceito;
* `unexpected_record` não é aceito;
* o parser não retorna normalmente;
* nenhum resultado estruturado é produzido;
* nenhum requisito específico é imposto a `line_number`.

O teste aceitará somente `duplicate_date`, sem códigos alternativos.

**Observed Red before implementation:**

```text
ReceiptValidationError
code: invalid_record_order
message: Record is out of order; expected ITEM on line 3.
line_number: 3
```

Esse Red demonstrou que o parser já rejeitava a segunda ocorrência de `DATE`, mas ainda a classificava indiretamente como uma violação posicional. A guarda explícita de cardinalidade passou a emitir `duplicate_date` antes de `duplicate_total` e da validação posicional, sem criar requisito específico para `line_number`.

## Additional Error Validation

Os demais códigos de erro definidos na SPEC podem ser validados por testes parametrizados depois dos primeiros cenários.

Para `AC-008`, existe cobertura para a ausência de cada registro obrigatório: `TEST-006` cobre `missing_item`, `TEST-018` cobre `missing_total`, `TEST-020` cobre `missing_merchant` e `TEST-021` cobre `missing_date`.

`empty_input` foi promovido da lista genérica futura para o cenário formal `SCN-010` / `FX-010` / `TEST-010`, que está implementado e verde.

`invalid_item_format` foi promovido da lista genérica futura para o cenário formal `SCN-011` / `FX-011` / `TEST-011`, que está implementado e verde.

`invalid_item_description` foi promovido da lista genérica futura para o cenário formal `SCN-012` / `FX-012` / `TEST-012`, que está implementado e verde.

`invalid_unit_price` foi promovido da lista genérica futura para o cenário formal `SCN-013` / `FX-013` / `TEST-013`, que está implementado e verde.

`invalid_line_total` foi promovido da lista genérica futura para o cenário formal `SCN-014` / `FX-014` / `TEST-014`, que está materializado, implementado e verde.

`invalid_receipt_total` foi promovido da lista genérica futura para o cenário formal `SCN-015` / `FX-015` / `TEST-015`, que está materializado, implementado e verde.

O caso não convertível de `invalid_line_total` foi promovido para o cenário formal `SCN-016` / `FX-016` / `TEST-016`, que está materializado, implementado e verde. O mesmo código possui dois cenários independentes: `SCN-014` comprova o valor negativo, enquanto `SCN-016` comprova a falha de conversão. O contrato comprovado de `SCN-014` permanece inalterado.

O caso não convertível de `invalid_unit_price` foi promovido para o cenário formal `SCN-017` / `FX-017` / `TEST-017`, que está materializado, implementado e verde. `SCN-013` continua comprovando separadamente a forma lexical com uma casa decimal, enquanto `SCN-017` comprova a tradução da falha de conversão.

`missing_total` foi promovido da lista genérica futura para o cenário formal `SCN-018` / `FX-018` / `TEST-018`, que está materializado, implementado e verde.

`duplicate_total` foi promovido para o cenário formal `SCN-019` / `FX-019` / `TEST-019`, que está materializado, implementado e verde.

`missing_merchant` foi promovido para `SCN-020` / `FX-020` / `TEST-020`, que estão materializados, implementados e verdes.

`missing_date` foi promovido para `SCN-021` / `FX-021` / `TEST-021`, que estão materializados, implementados e verdes.

`duplicate_merchant` foi promovido para `SCN-022` / `FX-022` / `TEST-022`, que estão materializados, implementados e verdes.

`duplicate_date` foi promovido para `SCN-023` / `FX-023` / `TEST-023`, que estão materializados, implementados e verdes.

Exemplo de tabela futura:

| Error code                 | Synthetic input condition |
| -------------------------- | ------------------------- |
| `invalid_merchant`         | nome vazio                |
| `invalid_date`             | `2026-02-30`              |
| `unexpected_record`        | prefixo desconhecido      |

Esses testes não precisam ser todos implementados no primeiro incremento.

Eles devem ser adicionados em tarefas pequenas, mantendo rastreabilidade com a SPEC.

## Pendências de planejamento não bloqueantes

Antes da implementação completa dos cenários inválidos, uma decisão humana deverá definir a precedência quando uma mesma entrada puder corresponder a mais de um código de erro.

### Comportamento comprovado para SCN-010

Quando nenhuma linha lógica permanece após a normalização, `empty_input` é emitido antes da validação de registros obrigatórios individuais e antes da validação de ordem.

Essa precedência comprovada se limita a uma sequência lógica vazia. Nesse caso, a entrada não é classificada primeiro como `missing_merchant`, `missing_date`, `missing_item`, `missing_total` ou `invalid_record_order`. Nenhuma política geral é estabelecida para entradas parcialmente preenchidas ou outras combinações de erros.

### Comportamento comprovado para SCN-011

Quando uma linha reconhecida como `ITEM` não possui exatamente quatro campos, `invalid_item_format` é emitido antes das conversões numéricas e antes das validações matemáticas do item.

Para `FX-011`, não ocorrem antes a conversão da quantidade, do preço unitário ou do total do item, a validação de `line_total_mismatch`, a acumulação do item ou a validação do total agregado. Essa precedência comprovada se limita ao caso de três campos em um registro já reconhecido como `ITEM` e não estabelece uma política geral para outras quantidades ou combinações de erros.

Uma linha `ITEM` malformada não entra na lista `items`, não altera o total acumulado e não produz dicionário parcial. O parsing termina com `ReceiptValidationError`; essa é uma condição observável do contrato, não uma exigência sobre a estrutura interna do código.

### Comportamento comprovado para SCN-012

Quando uma linha reconhecida como `ITEM` possui exatamente quatro campos, mas a descrição fica vazia depois da normalização, `invalid_item_description` é emitido depois da validação da quantidade de campos e antes das conversões numéricas.

A ordem localizada comprovada é:

1. dividir e normalizar os campos;
2. validar que existem exatamente quatro campos;
3. validar que a descrição não está vazia;
4. converter a quantidade;
5. converter os valores monetários;
6. validar o total matemático do item;
7. retornar o item validado.

Essa ordem preserva `invalid_item_format` antes de `invalid_item_description` quando a quantidade de campos estiver incorreta. Para o caso de quatro campos com descrição vazia, `invalid_item_description` precede `invalid_quantity`, `line_total_mismatch`, a acumulação do item e `receipt_total_mismatch`.

Essa precedência está limitada ao cenário de descrição vazia. Um item rejeitado não entra em `items`, não altera o total acumulado, não gera dicionário retornável e interrompe o parsing com `ReceiptValidationError`; trata-se de uma condição observável, sem impor uma estrutura interna específica.

Os contratos permanecem distintos:

```text
ITEM: Arroz | 2 | 8.50
→ invalid_item_format

ITEM: | 2 | 8.50 | 17.00
→ invalid_item_description
```

### Comportamento comprovado para SCN-013

Para as regras atualmente cobertas de `ITEM`, a ordem localizada comprovada é:

```text
invalid_item_format
→ invalid_item_description
→ invalid_quantity
→ invalid_unit_price
→ line_total_mismatch
```

Em `SCN-013`, a quantidade de campos e a descrição já são válidas, e a quantidade também é válida. O formato lexical do preço unitário é validado antes das conversões e validações que dependem desse preço. O item somente é retornado depois de todas as validações.

Essa precedência está limitada ao preço `"8.5"` coberto por `SCN-013` e não estabelece uma política geral para outros campos ou formatos ainda não materializados. Um item com preço em formato inválido não entra em `items`, não altera o total acumulado, não gera item retornável e interrompe o parsing com `ReceiptValidationError`.

Como `Decimal("8.5")` é válido e o cálculo `2 × 8.5` equivale a `17.00`, o Red observado foi o parser aceitar a entrada e `TEST-013` falhar com:

```text
Failed: DID NOT RAISE ReceiptValidationError
```

Esse Red demonstrou a ausência de validação lexical do preço unitário, não uma falha de conversão decimal.

### Comportamento comprovado para SCN-014

Para as regras atualmente cobertas de `ITEM`, a ordem localizada comprovada é:

```text
invalid_item_format
→ invalid_item_description
→ invalid_quantity
→ invalid_unit_price
→ invalid_line_total
→ line_total_mismatch
```

Em `SCN-014`, a quantidade de campos, a descrição, a quantidade e o formato de `unit_price` já são válidos. `unit_price` é convertido, `line_total` é convertido e seu valor negativo é rejeitado antes da comparação matemática. Somente um item totalmente válido é retornado.

A validação negativa reutiliza o `Decimal` já convertido, sem uma segunda conversão. Essa precedência está limitada ao `line_total == "-1.00"` coberto por `SCN-014` e não estabelece política geral para outros campos negativos.

O Red observado foi `TEST-014` receber `ReceiptValidationError` com o código `line_total_mismatch`, produzindo a divergência:

```text
assert "line_total_mismatch" == "invalid_line_total"
```

Esse Red demonstrou a ausência da validação semântica e da precedência esperada. Após a guarda localizada, o parser emite `invalid_line_total` com mensagem não vazia. Um item com total negativo não entra em `items`, não altera o acumulador, não gera item retornável e não alcança a validação do total agregado.

### Precedência comprovada para SCN-015

O fluxo agregado localizado comprovado é:

```text
itens estruturalmente válidos
→ itens localmente válidos
→ existência de pelo menos um item
→ extração do texto de TOTAL
→ conversão de TOTAL
→ invalid_receipt_total
→ comparação com o total acumulado
→ receipt_total_mismatch
→ saída final
```

Para `SCN-015`, todos os itens são processados e o total decimal `10.00` é acumulado. Depois da extração de `TOTAL: 10,00`, a falha de conversão é traduzida para `invalid_receipt_total`; a comparação com o total acumulado não é executada e nenhum dicionário final é retornado.

`invalid_receipt_total` precede `receipt_total_mismatch`, pois não é possível comparar corretamente um total que ainda não foi convertido para um valor decimal válido. Essa precedência está limitada a `SCN-015`; a cardinalidade duplicada é protegida separadamente por `duplicate_total` em `SCN-019`.

O Red observado foi `decimal.InvalidOperation` escapar de `Decimal("10,00")` em vez de o parser lançar `ReceiptValidationError` com `code == "invalid_receipt_total"`. Esse Red demonstrou que a entrada era rejeitada, mas ainda atravessava a fronteira pública com um tipo técnico.

Um `TOTAL` com formato inválido não produz dicionário final nem nota parcial observável e não alcança `receipt_total_mismatch`. Esse contrato não impõe rollback ou limpeza manual como detalhe de implementação.

A tradução é específica da conversão do registro `TOTAL`:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_receipt_total")
```

O bloco `try` envolve somente `Decimal(receipt_total)` e captura apenas `InvalidOperation`; não existe captura ampla com `except Exception`.

`InvalidOperation` é uma exceção técnica da biblioteca `decimal`. Consumidores de `parse_receipt` não precisam conhecer esse detalhe interno: `ReceiptValidationError` é o contrato público estável, e seu `code` distingue a causa sem depender do texto da mensagem. Essa tradução comprovada é específica da conversão do campo `TOTAL`, não uma tradução genérica de todas as exceções internas.

### Precedência comprovada para SCN-016

O fluxo localizado de `ITEM` comprovado é:

```text
invalid_item_format
→ invalid_item_description
→ invalid_quantity
→ invalid_unit_price
→ conversão de line_total
→ invalid_line_total
→ line_total_mismatch
```

Para `SCN-016`, os quatro campos são confirmados, a descrição é validada, a quantidade é convertida e validada, e o preço unitário é validado e convertido. Em seguida, a conversão de `line_total` é tentada e `InvalidOperation` é traduzida para `invalid_line_total`. A validação de valor negativo e a comparação matemática não são executadas, e `_parse_item_record` lança antes de retornar um item.

O mesmo código público `invalid_line_total` pode resultar de uma falha de conversão ou de um valor decimal negativo. O Red observado foi `decimal.InvalidOperation` escapar da execução direta de `Decimal(line_total)` antes que `TEST-016` recebesse uma `ReceiptValidationError`. Esse Red demonstrou que a entrada já interrompia o processamento, mas ainda expunha um tipo técnico; `line_total_mismatch` não era alcançado.

A tradução comprovada na fronteira pública é:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_line_total")
```

`InvalidOperation` é uma exceção técnica da biblioteca `decimal`; consumidores de `parse_receipt` recebem o contrato público do parser. O código `invalid_line_total` indica que o campo não pode ser usado como total válido, enquanto mensagens distintas podem explicar falha de conversão ou valor negativo.

O bloco `try` envolve somente `Decimal(line_total)` e captura apenas `InvalidOperation`. A guarda negativa, a comparação matemática e a construção do item ficam fora do bloco; não existe `except Exception`, e erros de programação não relacionados continuam visíveis.

Como `_parse_item_record` lança antes de retornar, nenhum dicionário inválido chega a `parse_receipt`, `items.append(...)` não é executado, o acumulador não é atualizado e o registro `TOTAL` não é processado. Nenhum rollback manual é necessário.

### Precedência comprovada para SCN-017

O fluxo localizado de `ITEM` comprovado é:

```text
invalid_item_format
→ invalid_item_description
→ invalid_quantity
→ validação lexical de unit_price
→ conversão de unit_price
→ invalid_unit_price
→ conversão de line_total
→ invalid_line_total
→ line_total_mismatch
```

Para `SCN-017`, os quatro campos são confirmados, a descrição é validada e a quantidade é convertida. A guarda lexical superficial do preço é satisfeita; em seguida, `_convert_decimal` tenta converter `unit_price` e traduz `InvalidOperation` para `invalid_unit_price`. `line_total` não é convertido, a comparação matemática não é executada e `_parse_item_record` não retorna um item.

O Red observado foi `decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]` escapar da execução direta de `Decimal(unit_price)` antes que `TEST-017` recebesse uma `ReceiptValidationError`. Esse Red demonstrou que a guarda lexical não garante conversibilidade e que o tipo técnico atravessava a fronteira pública; `line_total_mismatch` não era alcançado.

`InvalidOperation` é uma exceção técnica da biblioteca `decimal`; consumidores de `parse_receipt` recebem o contrato público do parser. A tradução comprovada é:

```text
decimal.InvalidOperation
→ ReceiptValidationError(code="invalid_unit_price")
```

O código identifica o campo responsável, a causa técnica permanece encadeada internamente por `from exc` e nenhuma captura genérica foi adicionada. Essa evidência não declara que todos os formatos inválidos de preço estão formalmente cobertos.

`_convert_decimal` permaneceu com responsabilidade exclusivamente técnica: converter o valor, capturar `InvalidOperation`, lançar o contrato indicado pelo chamador e preservar a causa. O helper não conhece `unit_price`, não valida duas casas decimais e não escolhe código ou mensagem. A guarda lexical continua dentro de `_parse_item_record`, antes da conversão; `invalid_unit_price` e a mensagem permanecem explícitos na chamada. A assinatura do helper não mudou, e `SCN-017` validou um novo uso sem alterar seu contrato.

Os dois caminhos comprovados de `invalid_unit_price` permanecem independentes:

1. `SCN-013`, com `unit_price == "8.5"`: o valor é convertível, mas a guarda lexical rejeita a única casa decimal antes de `_convert_decimal`;
2. `SCN-017`, com `unit_price == "ab.cd"`: a forma superficial possui ponto e dois caracteres posteriores, mas `_convert_decimal` traduz a falha de conversão.

As mensagens não precisam ser idênticas. Em contraste, `ITEM: Arroz | 2 | 8.50 | 16.00` possui campos numericamente válidos e produz `line_total_mismatch`; `ITEM: Arroz | 1 | ab.cd | 10.00` não possui preço decimal válido e produz `invalid_unit_price` antes de qualquer comparação matemática.

Como `_convert_decimal` lança antes de `_parse_item_record` retornar, nenhum item inválido chega a `parse_receipt`, `items.append(...)` não é executado, o acumulador não é atualizado e o registro `TOTAL` não é processado. Nenhum rollback manual é necessário.

### Precedência comprovada para SCN-018

Para `SCN-018`, a precedência estrutural protegida é:

```text
empty_input
→ validar a ordem dos registros presentes
→ validar os registros ITEM presentes
→ missing_item
→ missing_total
→ converter receipt_total
→ invalid_receipt_total
→ receipt_total_mismatch
```

Essa sequência comprova que um prefixo válido contendo `MERCHANT`, `DATE` e ao menos um `ITEM` válido é classificado como `missing_total` quando o registro final está completamente ausente. Ela não redefine a precedência geral de erros concorrentes além do caso isolado por `FX-018`.

Para `FX-018`, a entrada não está vazia, `MERCHANT` e `DATE` estão nas posições corretas, o `ITEM` é processado com sucesso, existe ao menos um item e o fim da entrada é alcançado sem que um `TOTAL` tenha sido encontrado. Nesse ponto, `missing_total` é emitido antes de qualquer conversão ou comparação agregada.

O Red observado foi `invalid_record_order` com `line_number == 3`: o parser rejeitava a entrada, mas tratava o último `ITEM` como se ocupasse a posição esperada de `TOTAL`. O Green foi obtido ao distinguir uma sequência proibida de registros presentes, que continua produzindo `invalid_record_order`, do fim de uma sequência válida sem o registro obrigatório, que agora produz `missing_total`.

Os contratos relacionados a `TOTAL` permanecem independentes:

* fim após `MERCHANT → DATE → ITEM`, sem registro `TOTAL` → `missing_total`;
* mais de um registro reconhecido `TOTAL` → `duplicate_total`;
* `TOTAL: 10,00`, presente mas não convertível → `invalid_receipt_total`;
* `TOTAL` presente e convertível, mas divergente da soma dos itens → `receipt_total_mismatch`.

`missing_item` também permanece separado. `SCN-018` possui um item completamente válido e protege apenas o fim da entrada sem `TOTAL`; os testes atuais não estabelecem uma precedência geral para todas as entradas que omitam simultaneamente `ITEM` e `TOTAL`.

O item pode ser validado e acumulado internamente, mas o fim da entrada é detectado antes da saída: nenhum resultado estruturado é retornado, `_convert_decimal` não é chamada para `receipt_total`, nenhuma comparação agregada ocorre e nenhum rollback manual é necessário.

A positividade de `quantity` e de `unit_price` é um contrato explícito ainda sem teste. Valores zero ou negativos podem introduzir erros concorrentes em `line_total` e `receipt_total`, portanto esses cenários permanecem adiados até uma decisão própria de precedência. `SCN-018` foi priorizado por isolar uma única falha estrutural e não elimina nem redefine os contratos numéricos.

A precedência específica de duplicidades sobre `invalid_record_order` para a mesma ocorrência repetida foi comprovada por `SCN-019` para `TOTAL`, por `SCN-022` para `MERCHANT` e por `SCN-023` para `DATE`. `missing_merchant` e `missing_date` são comprovados por `SCN-020` e `SCN-021`; permanecem sem cenário executável `unexpected_record`, outras ordens estruturais e as precedências entre defeitos independentes simultâneos.

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
* `missing_merchant`
* `missing_date`
* `missing_total`
* `duplicate_merchant`
* `duplicate_date`
* `duplicate_total`
* `invalid_record_order`
* `invalid_quantity`
* `empty_input`
* `invalid_item_format`
* `invalid_item_description`
* `invalid_unit_price`
* `invalid_line_total`
* `invalid_receipt_total`

Specified but not yet implemented or protected:

* `unexpected_record`

Os demais contratos sem cenário executável também não devem ser interpretados como implementados. `SCN-019` comprova `duplicate_total`, `SCN-022` comprova `duplicate_merchant`, e `SCN-023` comprova `duplicate_date`. `SCN-020` e `SCN-021` comprovam somente as ausências globais isoladas de `MERCHANT` e `DATE`, sem implementar conteúdo vazio, formato inválido ou combinações de ausências. `unexpected_record` permanece sem implementação.

`SCN-008` é um cenário válido e não adiciona código de erro. O contrato `invalid_quantity` está comprovado somente para a quantidade com vírgula coberta por `SCN-009`; essa evidência não estabelece suporte geral para outros formatos numéricos inválidos.

O contrato `empty_input` está comprovado por `SCN-010` usando uma string completamente vazia. Essa evidência não declara suporte formal para entradas contendo somente whitespace e não implementa outros códigos de registros ausentes.

O contrato `invalid_item_format` está comprovado somente pelo registro `ITEM` de três campos coberto por `SCN-011`. Essa evidência não formaliza descrição ou campos vazios, formatos inválidos de outros campos nem outras quantidades de campos.

O contrato `invalid_item_description` está comprovado somente pela descrição vazia coberta por `SCN-012`. Essa evidência não formaliza quantidade, preço unitário ou total do item vazios; formatos monetários inválidos; limites de tamanho da descrição; nem uma variação materializada contendo apenas espaços.

O contrato `invalid_unit_price` está comprovado por dois cenários independentes: `SCN-013`, com `unit_price == "8.5"` convertível, mas sem duas casas decimais, e `SCN-017`, com `unit_price == "ab.cd"` superficialmente compatível com a guarda lexical, mas não convertível. Essa evidência não formaliza preço vazio, negativo, zero, com três casas, com vírgula ou em notação científica, nem outros formatos monetários ainda não materializados.

O contrato `invalid_line_total` está comprovado por dois cenários independentes: `SCN-014`, com `line_total == "-1.00"` convertível e negativo, e `SCN-016`, com `line_total == "abc"` não convertível. Essa evidência não formaliza `line_total == "0.00"`, campo vazio ou vírgula decimal em `line_total`, quantidade negativa, preço unitário negativo, `invalid_receipt_total` ou `TOTAL` negativo isoladamente.

O contrato `invalid_receipt_total` está comprovado somente por `TOTAL == "10,00"` em `SCN-015`. Essa evidência não formaliza total negativo ou vazio; uma ou três casas decimais; notação científica; nem outros separadores ou formatos ainda não materializados. A ausência completa de `TOTAL` é protegida por `missing_total` em `SCN-018`, e a duplicidade é protegida por `duplicate_total` em `SCN-019`.

O contrato `missing_total` está comprovado somente por `SCN-018`: uma sequência válida `MERCHANT → DATE → ITEM` termina sem registro `TOTAL`. Essa evidência não formaliza `TOTAL:` vazio, `TOTAL` antecipado, registro posterior a `TOTAL` nem combinações com outros registros obrigatórios ausentes. `TOTAL` duplicado é protegido separadamente por `SCN-019`.

Fluxo atualmente comprovado pelos testes:

1. enumerar e normalizar as linhas preservando seus números originais;
2. detectar entrada vazia;
3. reconhecer ocorrências estruturais relevantes nas linhas normalizadas;
4. detectar zero ocorrências de `MERCHANT`;
5. emitir `missing_merchant` antes da classificação posicional;
6. detectar zero ocorrências de `DATE`;
7. emitir `missing_date` antes da classificação posicional;
8. detectar mais de uma ocorrência de `MERCHANT`;
9. emitir `duplicate_merchant` antes da classificação posicional;
10. detectar mais de uma ocorrência de `DATE`;
11. emitir `duplicate_date` antes de `duplicate_total` e da classificação posicional;
12. detectar mais de uma ocorrência de `TOTAL` e emitir `duplicate_total`;
13. validar a ordem dos registros quando os contratos anteriores não se aplicam;
14. processar e validar os registros `ITEM`;
15. confirmar a existência de pelo menos um item e emitir `missing_item` nos cenários protegidos;
16. detectar o fim da entrada sem `TOTAL` e emitir `missing_total`;
17. quando existe exatamente um `TOTAL`, validá-lo e convertê-lo;
18. emitir os erros numéricos ou matemáticos aplicáveis;
19. produzir a saída estruturada somente quando estrutura e conteúdo são válidos.

A normalização mantém uma associação equivalente a `(original_line_number, normalized_text)`. Linhas vazias são removidas da sequência lógica, registros não vazios mantêm o número original, a validação estrutural usa o texto normalizado e os erros continuam reportando a posição original no arquivo.

Esse fluxo descreve o comportamento coberto pelos testes atuais, não uma arquitetura definitiva. As detecções de `missing_merchant`, `missing_date`, `duplicate_merchant`, `duplicate_date` e `duplicate_total` usam as linhas já normalizadas e ocorrem antes da validação posicional, sem processar itens ou converter o total agregado nesses caminhos.

O desenho atual evita rollback: `_parse_item_record` valida completamente o registro e lança antes de retornar quando o item é inválido. `parse_receipt` somente adiciona o item e atualiza o acumulador depois do retorno bem-sucedido; portanto, itens inválidos não deixam estado parcial observável.

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

## TDD Sequence for SCN-010

1. Formalizar `SCN-010` no harness.
2. Criar `FX-010` como arquivo de zero bytes.
3. Criar `TEST-010`.
4. Executar `TEST-010` e observar o Red.
5. Implementar uma guarda mínima após a normalização.
6. Executar a suíte completa.
7. Registrar as evidências.

Esta sequência foi concluída. A implementação adicionou somente uma guarda mínima de comportamento após a normalização, sem refatoração estrutural, seguindo a recomendação `No refactor now`.

## TDD Sequence for SCN-011

1. Formalizar `SCN-011` no harness.
2. Criar `FX-011` com um `ITEM` de três campos.
3. Criar `TEST-011`.
4. Executar `TEST-011` e observar o Red.
5. Traduzir a falha de quantidade de campos para `invalid_item_format`.
6. Executar `TEST-011` e a suíte completa.
7. Registrar as evidências.
8. Reavaliar se o processamento de `ITEM` ganhou complexidade suficiente para justificar uma pequena refatoração.

Esta sequência foi concluída. A implementação adicionou uma verificação explícita de quantidade de campos antes do desempacotamento, sem captura ampla de exceções e sem refatoração estrutural.

### Relação com a refatoração de ITEM

`_parse_item_record` continua concentrando as regras locais de parsing e validação de um item. `invalid_item_description` foi adicionada naturalmente nessa fronteira, sem mudança na assinatura do helper.

A extração anterior continua preservando os contratos, conforme confirmado pela suíte verde. Nenhuma nova refatoração foi realizada durante `SCN-012`.

## TDD Sequence for SCN-012

1. Formalizar `SCN-012` no harness.
2. Criar `FX-012` com descrição vazia e quatro campos.
3. Criar `TEST-012`.
4. Executar `TEST-012` e observar o Red.
5. Implementar a validação mínima dentro de `_parse_item_record`.
6. Executar `TEST-012` e a suíte completa.
7. Registrar as evidências.

Esta sequência foi concluída. O Red demonstrou que nenhuma exceção era emitida e que o item com descrição vazia era aceito. O Green foi obtido com uma guarda mínima dentro de `_parse_item_record`, depois de `invalid_item_format` e antes das conversões numéricas.

### Relação de SCN-013 com `_parse_item_record`

A validação lexical de `unit_price` foi mantida localmente em `_parse_item_record`, sem mudança na assinatura do helper e sem transferir responsabilidade para `parse_receipt`.

Nenhum helper monetário genérico foi criado. Ainda existe somente um contrato formal de formato monetário inválido; uma abstração compartilhada deve aguardar evidência de repetição, que poderá surgir em um futuro cenário de `line_total`. Nenhuma refatoração adicional ocorreu em `SCN-013`.

## TDD Sequence for SCN-013

1. Formalizar `SCN-013` no harness.
2. Criar `FX-013` com `unit_price` igual a `"8.5"`.
3. Criar `TEST-013`.
4. Executar `TEST-013` e observar o Red.
5. Implementar validação lexical mínima em `_parse_item_record`.
6. Executar `TEST-013` e a suíte completa.
7. Registrar as evidências.

Esta sequência foi concluída. O Red demonstrou que o parser aceitava `"8.5"` por sua conversibilidade numérica e retornava normalmente. O Green foi obtido com uma validação lexical mínima em `_parse_item_record`, antes da conversão do preço e da validação matemática.

### Relação de SCN-014 com `_parse_item_record`

A regra de `line_total` negativo pertence ao processamento local de um item e foi implementada em `_parse_item_record`, não em `parse_receipt`. A assinatura do helper permaneceu inalterada, e o `Decimal` de `line_total` já convertido é reutilizado.

`SCN-014` não demonstra repetição da regra lexical de duas casas de `SCN-013`: um cenário valida o formato lexical de `unit_price`, enquanto o outro valida semanticamente o valor negativo de `line_total`. A mudança foi uma guarda localizada; nenhum helper monetário genérico foi criado e nenhuma refatoração ocorreu.

## TDD Sequence for SCN-014

1. Formalizar `SCN-014` no harness.
2. Criar `FX-014` com `line_total` igual a `"-1.00"`.
3. Criar `TEST-014`.
4. Executar `TEST-014` e observar o Red.
5. Implementar a validação mínima em `_parse_item_record`.
6. Executar `TEST-014` e os testes de precedência.
7. Executar a suíte completa.
8. Registrar as evidências.

Esta sequência foi concluída. `TEST-014` foi inicialmente observado vermelho porque recebia `line_total_mismatch`. O Green foi obtido com uma guarda semântica localizada depois da conversão decimal e antes da comparação matemática. `TEST-001` a `TEST-014` passam juntos.

### Responsabilidades após SCN-015

`invalid_receipt_total` pertence ao processamento agregado da nota e permanece em `parse_receipt`. `_parse_item_record` continua responsável somente pela validação local de registros `ITEM` e não assume responsabilidade pelo registro `TOTAL`.

A implementação captura somente `InvalidOperation` durante `Decimal(receipt_total)`, sem `except Exception`, sem recalcular o total acumulado e sem alterar a assinatura pública de `parse_receipt`.

O processamento completo da nota permanece fora desse bloco `try`, de modo que erros de programação não relacionados continuam visíveis e não são classificados incorretamente como `invalid_receipt_total`.

SCN-013 valida o formato lexical de `unit_price`, SCN-014 valida o valor negativo de `line_total` e SCN-015 valida o formato não convertível de `receipt_total`. As regras são relacionadas, mas possuem falhas e precedências diferentes. Nenhum helper monetário genérico, alteração de assinatura ou refatoração foi introduzido, e os códigos distintos por campo foram preservados. A suíte verde protege a separação atual de responsabilidades.

## TDD Sequence for SCN-015

1. Formalizar `SCN-015` no harness.
2. Criar `FX-015` com `TOTAL` igual a `"10,00"`.
3. Criar `TEST-015`.
4. Executar `TEST-015` e observar o Red.
5. Traduzir a falha de conversão para `invalid_receipt_total`.
6. Executar `TEST-015` e `TEST-005`.
7. Executar a suíte completa.
8. Registrar as evidências.

Esta sequência foi concluída. `TEST-015` foi inicialmente observado vermelho porque `InvalidOperation` escapava da conversão do total da nota. O Green foi obtido com a tradução localizada para `invalid_receipt_total`, e `TEST-001` a `TEST-015` passam juntos.

## TDD Sequence for SCN-016

1. Formalizar `SCN-016` no harness.
2. Criar `FX-016` com `line_total` igual a `"abc"`.
3. Criar `TEST-016`.
4. Executar `TEST-016` e observar `InvalidOperation` escapando.
5. Traduzir somente a conversão de `line_total`.
6. Executar `TEST-016`, `TEST-014` e `TEST-004`.
7. Executar a suíte completa.
8. Registrar as evidências.

Esta sequência foi concluída. `TEST-016` foi inicialmente observado vermelho porque `InvalidOperation` escapava da conversão de `line_total`. O Green foi obtido com a tradução localizada para `invalid_line_total`, e `TEST-001` a `TEST-016` passam juntos.

`TASK-REVIEW-003` recomendou inicialmente manter as validações numéricas localizadas. Depois do terceiro bloco comprovado, `TASK-REVIEW-004` recomendou extrair a conversão mínima, e `TASK-REFACTOR-002` criou `_convert_decimal` sem mover regras lexicais, semânticas ou matemáticas. O helper atende `quantity`, `unit_price`, `line_total` e `receipt_total`; a guarda lexical do preço permanece localizada em `_parse_item_record`.

## TDD Sequence for SCN-017

1. Formalizar `SCN-017` no harness.
2. Criar `FX-017` com `unit_price` igual a `"ab.cd"`.
3. Criar `TEST-017`.
4. Executar `TEST-017` e observar `InvalidOperation` escapando.
5. Manter a validação lexical na posição atual.
6. Usar `_convert_decimal` somente na conversão de `unit_price`.
7. Executar `TEST-017` e `TEST-013`.
8. Executar os testes de precedência de `ITEM`.
9. Executar a suíte completa.
10. Registrar as evidências.

Esta sequência foi concluída. `TEST-017` foi inicialmente observado vermelho porque `InvalidOperation` escapava da conversão direta de `unit_price`. O Green foi obtido ao usar `_convert_decimal` somente nessa conversão, preservando a guarda lexical, e `TEST-001` a `TEST-017` passam juntos.

## TDD Sequence for SCN-018

1. Formalizar `SCN-018` no harness.
2. Criar `FX-018` sem linha `TOTAL`.
3. Criar `TEST-018` exigindo `missing_total`.
4. Executar `TEST-018` e registrar o código público atual.
5. Confirmar o Red de classificação estrutural.
6. Implementar a detecção mínima de `TOTAL` ausente.
7. Preservar `invalid_record_order` para sequências realmente inválidas.
8. Executar `TEST-018` e os testes estruturais anteriores.
9. Executar a suíte completa.
10. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-018` e `TEST-018` foram materializados, o Red expôs `invalid_record_order`, e o Green foi obtido ao distinguir o fim da entrada sem `TOTAL`. `TEST-001` a `TEST-018` passam juntos.

## TDD Sequence for SCN-019

1. Formalizar `SCN-019` no harness.
2. Criar `FX-019` com dois registros `TOTAL` idênticos.
3. Criar `TEST-019` exigindo `duplicate_total`.
4. Executar `TEST-019` e registrar o código público atual.
5. Confirmar o Red de `invalid_record_order`.
6. Implementar a contagem ou detecção mínima de `TOTAL` duplicado.
7. Preservar `missing_total` para zero ocorrências.
8. Preservar `invalid_record_order` para cardinalidade válida em sequência proibida.
9. Executar `TEST-019` e os testes estruturais anteriores.
10. Executar a suíte completa.
11. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-019` foi materializada, `TEST-019` expôs inicialmente `invalid_record_order`, a guarda de cardinalidade passou a emitir `duplicate_total` antes da validação posicional genérica, e `TEST-001` a `TEST-019` passam juntos.

## TDD Sequence for SCN-020

1. Formalizar `SCN-020` no harness.
2. Criar `FX-020` sem qualquer registro `MERCHANT`.
3. Criar `TEST-020` exigindo `missing_merchant`.
4. Executar `TEST-020` e registrar o código público atual.
5. Confirmar o Red de `invalid_record_order`.
6. Implementar a detecção mínima de ausência global de `MERCHANT`.
7. Preservar `invalid_record_order` quando `MERCHANT` existe, mas está deslocado.
8. Executar `TEST-020` e os testes estruturais anteriores.
9. Executar a suíte completa.
10. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-020` foi materializada, `TEST-020` expôs inicialmente `invalid_record_order`, a guarda de ausência global passou a emitir `missing_merchant` antes da validação posicional, e `TEST-001` a `TEST-020` passam juntos.

## TDD Sequence for SCN-021

1. Formalizar `SCN-021` no harness.
2. Criar `FX-021` sem qualquer registro `DATE`.
3. Criar `TEST-021` exigindo `missing_date`.
4. Executar `TEST-021` e registrar o código público atual.
5. Confirmar o Red de `invalid_record_order`.
6. Implementar a detecção mínima de ausência global de `DATE`.
7. Preservar `invalid_record_order` quando `DATE` existe, mas está deslocada.
8. Preservar `missing_merchant` para zero ocorrências de `MERCHANT`.
9. Executar `TEST-021` e os testes estruturais anteriores.
10. Executar a suíte completa.
11. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-021` foi materializada, `TEST-021` expôs inicialmente `invalid_record_order`, a guarda de ausência global passou a emitir `missing_date` depois de `missing_merchant` e antes da validação posicional, e `TEST-001` a `TEST-021` passam juntos.

## TDD Sequence for SCN-022

1. Formalizar `SCN-022` no harness.
2. Criar `FX-022` com dois registros `MERCHANT` idênticos e individualmente válidos.
3. Criar `TEST-022` exigindo `duplicate_merchant`.
4. Executar `TEST-022` e registrar o código público atual.
5. Confirmar o Red esperado de `invalid_record_order`.
6. Adicionar a guarda explícita mínima para mais de uma ocorrência reconhecida de `MERCHANT`.
7. Preservar `missing_merchant` para zero ocorrências.
8. Preservar `invalid_record_order` quando existe um único `MERCHANT` em posição proibida.
9. Não extrair helper, índice estrutural, enum, classe de registro ou máquina de estados.
10. Executar `TEST-022` e os testes estruturais anteriores.
11. Executar a suíte completa.
12. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-022` foi materializada, `TEST-022` expôs inicialmente `invalid_record_order`, a guarda explícita passou a emitir `duplicate_merchant` antes da validação posicional, e `TEST-001` a `TEST-022` passam juntos.

## TDD Sequence for SCN-023

1. Formalizar `SCN-023` no harness.
2. Criar `FX-023` com duas ocorrências `DATE` idênticas e individualmente válidas.
3. Criar `TEST-023` exigindo `duplicate_date`.
4. Executar `TEST-023` e registrar o código público atual.
5. Confirmar o Red esperado de `invalid_record_order`.
6. Adicionar a guarda explícita mínima para mais de uma ocorrência reconhecida de `DATE`.
7. Reutilizar `date_records` sem criar nova busca.
8. Preservar `missing_date` para zero ocorrências.
9. Preservar `invalid_record_order` quando existe uma única `DATE` em posição proibida.
10. Preservar `duplicate_merchant` e `duplicate_total`.
11. Não extrair helper, índice estrutural, enum, classe de registro ou máquina de estados.
12. Executar `TEST-023` e os testes estruturais anteriores.
13. Executar a suíte completa.
14. Registrar as evidências no harness.

Esta sequência foi concluída. `FX-023` foi materializada, `TEST-023` expôs inicialmente `invalid_record_order`, a guarda explícita passou a emitir `duplicate_date` antes de `duplicate_total` e da validação posicional, e `TEST-001` a `TEST-023` passam juntos.

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
| `2026-07-23` | `315f80a`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-010 passed; empty input now raises ReceiptValidationError with code empty_input instead of IndexError.` |
| `2026-07-24` | `8a9eb8d`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-011 passed; malformed ITEM records now raise invalid_item_format before unpacking or numeric conversion.` |
| `2026-07-25` | `748f1db`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-012 passed; empty ITEM descriptions now raise invalid_item_description before numeric conversion.` |
| `2026-07-25` | `52a15c3`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-013 passed; unit_price 8.5 now raises invalid_unit_price before mathematical validation.` |
| `2026-07-25` | `1c17888`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-014 passed; negative line totals now raise invalid_line_total before line_total_mismatch.` |
| `2026-07-25` | `07d1373`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-015 passed; invalid receipt totals now translate InvalidOperation to invalid_receipt_total.` |
| `2026-07-25` | `9b7c759`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass (warning)`  | `TEST-001 through TEST-015 passed; pytest could not create .pytest_cache due to WinError 5; SCN-016 remains planned.` |
| `2026-07-26` | `d7fd01a`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-016 passed; non-convertible line totals now translate InvalidOperation to invalid_line_total.` |
| `2026-07-26` | `a6f49e0`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-017 passed; non-convertible unit prices now translate InvalidOperation to invalid_unit_price.` |
| `2026-07-26` | `8ef261e`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-018 passed; receipts without a TOTAL record now produce missing_total instead of invalid_record_order.` |
| `2026-07-26` | `cbf9118`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-019 passed; duplicate TOTAL records now produce duplicate_total before generic order validation.` |
| `2026-07-26` | `971154e`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-020 passed; receipts with no MERCHANT record now produce missing_merchant before positional order validation.` |
| `2026-07-27` | `fe95871`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-021 passed; receipts with no DATE record now produce missing_date before positional order validation.` |
| `2026-07-27` | `f468279`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-022 passed; duplicate MERCHANT records now produce duplicate_merchant before positional order validation.` |
| `2026-07-28` | `174e967`     | `.\.venv\Scripts\python.exe -m pytest -q`                                                                                                                                                           | `pass`            | `TEST-001 through TEST-023 passed; duplicate DATE records now produce duplicate_date before duplicate-total and positional validation.` |

Na validação de `2026-07-27`, o pytest também informou que não pôde criar `.pytest_cache` devido a `WinError 5`; o warning ambiental foi não bloqueante. Com `SCN-021`, os vinte e um testes passaram.

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
* `FX-010` foi materializado como um arquivo de zero bytes, cuja leitura textual produz `""`.
* `TEST-010` foi inicialmente observado vermelho porque `IndexError` escapava da interface pública.
* Uma guarda mínima foi adicionada imediatamente após a normalização para verificar a ausência de linhas lógicas, antes de qualquer acesso por índice.
* A entrada completamente vazia passou a emitir `ReceiptValidationError` com o código `empty_input` e uma mensagem não vazia.
* Nenhum contrato específico para `line_number` foi introduzido por `SCN-010`.
* Quando a sequência lógica está vazia, `empty_input` precede a validação dos registros obrigatórios individuais e a validação de ordem.
* `SCN-010` foi implementado sem refatoração estrutural, seguindo a recomendação `No refactor now`.
* `TEST-001` a `TEST-010` passam juntos.
* `FX-011` foi materializada e revisada com a linha `ITEM: Arroz | 2 | 8.50`.
* A linha contém três campos e não possui `line_total`.
* `TEST-011` foi inicialmente observado vermelho porque `ValueError` escapava durante o desempacotamento.
* O parser passou a verificar explicitamente `len(item_fields) != 4` antes do desempacotamento.
* A linha malformada passou a emitir `ReceiptValidationError` com o código `invalid_item_format` e uma mensagem não vazia.
* Nenhum requisito específico para `line_number` e nenhuma captura ampla de exceções foram introduzidos.
* O item malformado não é convertido, adicionado ou acumulado.
* `TEST-001` a `TEST-011` passam juntos.
* A extração do processamento de `ITEM` para `_parse_item_record` preservou os 11 testes existentes.
* `FX-012` foi materializada e revisada com a linha `ITEM: | 2 | 8.50 | 17.00`, que possui exatamente quatro campos e descrição normalizada igual a `""`.
* `TEST-012` foi inicialmente observado vermelho porque nenhuma exceção era emitida e o item com descrição vazia era aceito.
* A validação foi adicionada dentro de `_parse_item_record`, depois de `invalid_item_format` e antes das conversões numéricas.
* A entrada passou a emitir `ReceiptValidationError` com o código `invalid_item_description` e uma mensagem não vazia.
* Nenhum contrato específico para `line_number` foi introduzido.
* O item inválido não é retornado, adicionado ou acumulado.
* `TEST-001` a `TEST-012` passam juntos.
* `FX-013` foi materializada e revisada com a linha `ITEM: Arroz | 2 | 8.5 | 17.00`, que possui exatamente quatro campos, descrição válida e quantidade válida.
* `Decimal("8.5")` é válido numericamente, mas `"8.5"` não satisfaz o formato monetário controlado de duas casas decimais.
* `line_total` e `TOTAL` permanecem matematicamente consistentes.
* `TEST-013` foi inicialmente observado vermelho porque o parser aceitava o preço e retornava a nota normalmente.
* A validação lexical foi adicionada em `_parse_item_record` antes da conversão do preço e da validação matemática.
* A entrada passou a emitir `ReceiptValidationError` com o código `invalid_unit_price` e uma mensagem não vazia.
* Nenhum contrato específico para `line_number` foi introduzido.
* O item inválido não é retornado, adicionado ou acumulado.
* `TEST-001` a `TEST-013` passam juntos.
* `FX-014` foi materializada e revisada com exatamente quatro campos, descrição `"Arroz"`, quantidade `"2"`, `unit_price == "8.50"` e `line_total == "-1.00"`.
* `Decimal("-1.00")` é convertível e possui duas casas decimais, mas o valor é semanticamente inválido por ser negativo.
* `TEST-014` foi inicialmente observado vermelho porque recebia `line_total_mismatch` em vez de `invalid_line_total`.
* Uma guarda semântica localizada foi adicionada em `_parse_item_record` depois da conversão de `line_total` para `Decimal` e antes da comparação `quantity × unit_price`.
* O parser passou a lançar `ReceiptValidationError` com o código `invalid_line_total` e uma mensagem não vazia.
* Nenhum contrato específico para `line_number` foi criado.
* O mesmo `Decimal` é reutilizado, sem conversão duplicada.
* O helper lança antes de retornar; o item inválido não é adicionado nem acumulado, e a validação do total agregado não é alcançada.
* Nenhum helper adicional foi criado e nenhuma refatoração ocorreu.
* `TEST-001` a `TEST-014` passam juntos.
* `FX-015` foi materializada e revisada em `fixtures/inputs/invalid_receipt_total_format.txt`, sem reutilizar ou sobrescrever `fixtures/inputs/invalid_receipt_total.txt`.
* O único item é válido: `1 × 10.00 == 10.00`, e o total acumulado é `10.00`; somente `TOTAL == "10,00"` possui formato inválido.
* `TEST-015` foi inicialmente observado vermelho porque `InvalidOperation` escapava da conversão do total da nota.
* A tradução foi adicionada de forma localizada em `parse_receipt`, com o bloco `try` limitado a `Decimal(receipt_total)` e captura exclusiva de `InvalidOperation`.
* A interface pública agora emite `ReceiptValidationError` com o código `invalid_receipt_total` e uma mensagem não vazia.
* `TEST-015` não estabelece contrato específico para `line_number`.
* A comparação com o total acumulado não é alcançada após a falha de conversão, e nenhum resultado parcial é retornado.
* `receipt_total_mismatch` permanece comprovado separadamente por `SCN-005`, no qual `TOTAL == "30.00"` é convertível, mas diverge da soma `29.00`.
* `_parse_item_record` permanece responsável pela validação local dos itens; o comportamento agregado continua em `parse_receipt`.
* Nenhum helper, assinatura pública ou estrutura foi alterado para registrar este comportamento.
* `TEST-001` a `TEST-015` passam juntos.
* `FX-016` foi materializada e revisada em `fixtures/inputs/invalid_line_total_format.txt`, com exatamente quatro campos e `line_total == "abc"`.
* Descrição, quantidade e `unit_price` são válidos; somente `line_total` não é convertível.
* `TEST-016` foi inicialmente observado vermelho porque `InvalidOperation` escapava da conversão de `line_total`.
* A tradução foi adicionada de forma localizada em `_parse_item_record`, com o bloco `try` limitado a `Decimal(line_total)` e captura exclusiva de `InvalidOperation`.
* A interface pública agora emite `ReceiptValidationError` com o código `invalid_line_total` e uma mensagem não vazia.
* `TEST-016` não estabelece contrato específico para `line_number`.
* Quando a conversão falha, a guarda negativa e `line_total_mismatch` não são alcançados.
* O helper lança antes de retornar; nenhum item inválido é retornado, adicionado ou acumulado.
* `SCN-014` comprova separadamente o valor negativo, e `SCN-004` comprova separadamente a divergência matemática.
* Nenhum helper ou refatoração adicional foi introduzido.
* `TEST-001` a `TEST-016` passam juntos.
* `FX-017` foi materializada e revisada em `fixtures/inputs/non_convertible_unit_price.txt`, com quatro campos e `unit_price == "ab.cd"`; descrição e quantidade são válidas.
* A forma superficial do preço possui conteúdo antes do ponto e dois caracteres posteriores, portanto satisfaz a guarda lexical existente, mas `Decimal("ab.cd")` produz `InvalidOperation`.
* `TEST-017` foi inicialmente observado vermelho porque `InvalidOperation` escapava da interface pública.
* A guarda lexical foi preservada na posição original, antes da conversão.
* Somente a conversão de `unit_price` passou a usar `_convert_decimal`, com o código `invalid_unit_price` e a mensagem explícitos no chamador.
* A interface pública agora emite `ReceiptValidationError` com `error.code == "invalid_unit_price"` e uma mensagem não vazia.
* `TEST-017` não estabelece requisito específico para `line_number`.
* Quando a conversão falha, `line_total` não é convertido, a validação matemática não é alcançada e nenhum item inválido é retornado, adicionado ou acumulado.
* `SCN-013` continua comprovando separadamente a forma lexical incorreta com uma casa decimal.
* `_convert_decimal` não foi modificado, nenhum helper adicional foi criado e nenhuma refatoração adicional ocorreu.
* `TEST-001` a `TEST-017` passam juntos.
* `FX-018` foi materializada em `fixtures/inputs/invalid_missing_total.txt` com exatamente três linhas, sem prefixo `TOTAL` e com os registros presentes em ordem válida.
* O único `ITEM` possui quatro campos válidos e satisfaz `quantity × unit_price == line_total`.
* `TEST-018` foi inicialmente observado vermelho: o parser lançava `ReceiptValidationError` com `invalid_record_order`, não retornava normalmente, mas classificava incorretamente o fim da entrada.
* A implementação passou a distinguir registros presentes em sequência proibida do fim de uma sequência válida sem `TOTAL`.
* A interface pública agora lança `ReceiptValidationError` com `error.code == "missing_total"` e mensagem não vazia; nenhum requisito específico para `line_number` foi criado.
* Para `SCN-018`, `_convert_decimal` não é chamada para `receipt_total`, nenhuma comparação agregada ocorre e nenhum resultado estruturado é retornado.
* `TEST-001` a `TEST-018` passam juntos.
* `FX-019` foi materializada em `fixtures/inputs/invalid_duplicate_total.txt` com exatamente cinco linhas.
* O primeiro `TOTAL` está na linha 4 e o segundo na linha 5; ambos possuem prefixo reconhecido, valor `"10.00"`, são convertíveis e correspondem ao acumulado.
* A duplicidade é o único defeito intencional de `FX-019`.
* `TEST-019` foi inicialmente observado vermelho com `invalid_record_order`; o parser já rejeitava a entrada, mas classificava incorretamente o primeiro `TOTAL` como registro na faixa de `ITEM`.
* A implementação passou a detectar mais de uma ocorrência reconhecida pelo prefixo `TOTAL:` antes da validação posicional que produzia o Red.
* A interface pública agora lança `ReceiptValidationError` com `error.code == "duplicate_total"` e mensagem não vazia.
* `TEST-019` não estabelece requisito específico para `line_number`.
* Nenhum dos totais é escolhido silenciosamente, e nenhuma saída estruturada é retornada.
* `TEST-001` a `TEST-019` passam juntos.
* `FX-020` foi materializada e revisada em `fixtures/inputs/invalid_missing_merchant.txt` com exatamente três linhas: `DATE`, `ITEM` e `TOTAL`, sem qualquer ocorrência de `MERCHANT`.
* O `ITEM` possui quatro campos válidos, satisfaz `quantity × unit_price == line_total`, e o único `TOTAL` corresponde ao item.
* `TEST-020` foi inicialmente observado vermelho com `invalid_record_order` e a mensagem indicando `MERCHANT` esperado na linha 1; o parser rejeitava a entrada, mas classificava incorretamente a ausência global.
* A implementação passou a reconhecer ocorrências pelo prefixo estrutural `MERCHANT:` depois de `empty_input` e antes da validação posicional.
* Quando a contagem global é zero, a interface pública lança `ReceiptValidationError` com `error.code == "missing_merchant"` e mensagem não vazia.
* Nenhum requisito específico para `line_number` foi criado; nenhum item ou total agregado é processado depois da detecção, e nenhum resultado estruturado é retornado.
* Ausência global (`DATE → ITEM → TOTAL`) produz `missing_merchant`; um `MERCHANT` existente, mas deslocado (`DATE → MERCHANT → ITEM → TOTAL`), continua produzindo `invalid_record_order`.
* Uma entrada sem linhas significativas continua produzindo `empty_input` antes de `missing_merchant`. `SCN-020` possui um item e um total válidos, portanto não redefine `missing_item`, `missing_total` ou `duplicate_total`.
* Nenhuma linha `MERCHANT` produz `missing_merchant`; `MERCHANT:` vazio é uma ocorrência estrutural existente e permanece fora do escopo de `SCN-020`.
* `TEST-001` a `TEST-020` passam juntos.
* `FX-021` foi materializada e revisada em `fixtures/inputs/invalid_missing_date.txt` com exatamente três linhas: `MERCHANT`, `ITEM` e `TOTAL`, sem qualquer ocorrência de `DATE`.
* O `ITEM` possui quatro campos válidos, satisfaz `quantity × unit_price == line_total`, e o único `TOTAL` corresponde ao item.
* `TEST-021` foi inicialmente observado vermelho com `invalid_record_order` e a mensagem indicando `DATE` esperada na linha 2; o parser rejeitava a entrada, mas classificava incorretamente a ausência global.
* A implementação passou a reconhecer ocorrências pelo prefixo estrutural `DATE:` depois de `empty_input` e `missing_merchant`, e antes da validação posicional.
* Quando a contagem global é zero, a interface pública lança `ReceiptValidationError` com `error.code == "missing_date"` e mensagem não vazia.
* Nenhum requisito específico para `line_number` foi criado; nenhum item ou total agregado é processado depois da detecção, e nenhum resultado estruturado é retornado.
* Ausência global (`MERCHANT → ITEM → TOTAL`) produz `missing_date`; uma `DATE` existente, mas deslocada (`MERCHANT → ITEM → DATE → TOTAL`), continua pertencendo a `invalid_record_order`.
* Nenhuma linha `DATE` produz `missing_date`; `DATE:` vazia é uma ocorrência estrutural existente e conteúdo vazio ou formato inválido permanecem fora do escopo de `SCN-021`.
* Os cenários isolados comprovam `empty_input → missing_merchant → missing_date`, sem estabelecer precedência geral para uma entrada que omita simultaneamente `MERCHANT` e `DATE`.
* `SCN-021` possui um item e um total válidos, portanto não redefine `missing_item`, `missing_total`, `duplicate_total`, `invalid_receipt_total` ou `receipt_total_mismatch`.
* `TEST-001` a `TEST-021` passam juntos.
* `FX-022` foi materializada e revisada em `fixtures/inputs/invalid_duplicate_merchant.txt` com exatamente cinco linhas.
* O primeiro `MERCHANT` está na linha 1 e o segundo na linha 2; ambos contêm `"Mercado Exemplo"`, são válidos, não vazios e idênticos.
* Existe uma única `DATE`, um único `ITEM` com quatro campos válidos e um único `TOTAL`.
* O item satisfaz `1 × 10.00 == 10.00`, e o `TOTAL == "10.00"` corresponde ao acumulado; a segunda ocorrência de `MERCHANT` é o único defeito intencional.
* `TEST-022` foi inicialmente observado vermelho com `invalid_record_order` e a mensagem indicando `DATE` esperada na linha 2.
* O parser já rejeitava a entrada, mas classificava a duplicidade como uma violação posicional genérica.
* A implementação reutilizou `merchant_records`, sem criar uma segunda busca estrutural por `MERCHANT:`, e adicionou uma guarda explícita para `len(merchant_records) > 1`.
* A guarda ocorre depois de `missing_merchant` e `missing_date`, antes de `duplicate_total`, da validação posicional, do processamento de itens e das conversões numéricas.
* A interface pública agora lança `ReceiptValidationError` com `error.code == "duplicate_merchant"` e mensagem não vazia.
* A segunda ocorrência fornece `line_number == 2` na implementação atual, mas `TEST-022` e o contrato de `SCN-022` não exigem valor específico para `line_number`.
* Nenhum estabelecimento é escolhido, sobrescrito ou combinado silenciosamente; nenhum item ou total precisa ser processado, nenhum resultado parcial é exposto e nenhuma saída estruturada é retornada.
* `TEST-001` a `TEST-022` passam juntos.

### Cardinalidade de MERCHANT comprovada

Zero ocorrências são protegidas por `SCN-020` / `TEST-020`:

```text
DATE
ITEM
TOTAL
→ missing_merchant
```

Uma ocorrência em posição válida segue o fluxo normal, conforme os cenários válidos:

```text
MERCHANT
DATE
ITEM+
TOTAL
→ saída válida
```

Uma ocorrência em posição proibida mantém cardinalidade válida e continua pertencendo a `invalid_record_order`:

```text
DATE
MERCHANT
ITEM
TOTAL
→ invalid_record_order
```

Mais de uma ocorrência é protegida por `SCN-022` / `TEST-022`:

```text
MERCHANT
MERCHANT
DATE
ITEM
TOTAL
→ duplicate_merchant
```

Assim, zero ocorrências produzem `missing_merchant`, enquanto mais de uma produz `duplicate_merchant`. No segundo caso, o primeiro registro está na posição correta e o segundo repete um singleton; a classificação específica de duplicidade prevalece sobre a expectativa genérica de `DATE` na linha 2.

Uma linha `MERCHANT:` vazia representa uma ocorrência estrutural presente com conteúdo vazio e permanece fora do escopo. Os dois valores de `FX-022` são idênticos, mas a implementação não compara nomes, não decide conflitos e não define comportamento específico para estabelecimentos diferentes: a cardinalidade maior que um é suficiente.

`MERCHANT:` é um prefixo reconhecido, inclusive na segunda ocorrência. Portanto, a repetição produz `duplicate_merchant`, não `unexpected_record`; este último permanece especificado, mas sem cenário executável.

`FX-022` contém uma única `DATE`, fisicamente na linha 3. `missing_date` e `duplicate_date` não se aplicam a esse cenário. O `ITEM` e o `TOTAL` são válidos, portanto também não se aplicam `missing_item`, `missing_total`, `duplicate_total`, `invalid_receipt_total`, `receipt_total_mismatch` ou erros numéricos e matemáticos do item.

O fluxo conceitual atualmente protegido é:

```text
empty_input
→ missing_merchant
→ missing_date
→ duplicate_merchant
→ duplicate_date
→ duplicate_total
→ invalid_record_order
→ validações dos ITEMs
→ missing_item
→ missing_total
→ validação do único TOTAL
→ saída válida
```

Essa sequência descreve os cenários isolados comprovados, não uma política geral para defeitos independentes simultâneos. Em `FX-022`, a detecção de `duplicate_merchant` interrompe o fluxo antes da validação posicional, do processamento de `ITEM` e da conversão de `TOTAL`.

`TASK-REVIEW-007` permanece vigente:

```text
Decision: Keep explicit guards
```

O Green de `SCN-022` preservou essa decisão: `merchant_records` foi reutilizado, a precedência permaneceu visível em `parse_receipt`, e nenhum helper, índice estrutural, enum, classe de registro, máquina de estados ou refatoração das demais guardas foi introduzido.

* `FX-023` foi materializada e revisada em `fixtures/inputs/invalid_duplicate_date.txt` com exatamente cinco linhas.
* A primeira `DATE` está na linha 2 e a segunda na linha 3; ambas contêm `"2026-07-23"`, são válidas, não vazias e idênticas.
* Existe um único `MERCHANT`, um único `ITEM` com quatro campos válidos e um único `TOTAL`.
* O item satisfaz `1 × 10.00 == 10.00`, e o `TOTAL == "10.00"` corresponde ao acumulado; a segunda ocorrência de `DATE` é o único defeito intencional.
* `TEST-023` foi inicialmente observado vermelho com `invalid_record_order` e a mensagem indicando `ITEM` esperado na linha 3.
* O parser já rejeitava a entrada, mas classificava a duplicidade como uma violação posicional genérica.
* A implementação reutilizou `date_records`, sem criar uma segunda busca estrutural por `DATE:`, e adicionou uma guarda explícita para `len(date_records) > 1`.
* A guarda ocorre depois de `duplicate_merchant`, antes de `duplicate_total`, da validação posicional, do processamento de itens e das conversões numéricas.
* A interface pública agora lança `ReceiptValidationError` com `error.code == "duplicate_date"` e mensagem não vazia.
* A segunda ocorrência fornece `line_number == 3` na implementação atual, mas `TEST-023` e o contrato de `SCN-023` não exigem valor específico para `line_number`.
* Nenhuma data é escolhida, sobrescrita ou combinada silenciosamente; nenhum item ou total precisa ser processado, nenhum resultado parcial é exposto e nenhuma saída estruturada é retornada.
* `TEST-001` a `TEST-023` passam juntos.

### Cardinalidade de DATE comprovada

Zero ocorrências são protegidas por `SCN-021` / `TEST-021`:

```text
MERCHANT
ITEM
TOTAL
→ missing_date
```

Uma ocorrência em posição válida segue o fluxo normal, conforme os cenários válidos:

```text
MERCHANT
DATE
ITEM+
TOTAL
→ saída válida
```

Uma ocorrência em posição proibida mantém cardinalidade válida e continua pertencendo a `invalid_record_order`:

```text
MERCHANT
ITEM
DATE
TOTAL
→ invalid_record_order
```

Mais de uma ocorrência é protegida por `SCN-023` / `TEST-023`:

```text
MERCHANT
DATE
DATE
ITEM
TOTAL
→ duplicate_date
```

Assim, zero ocorrências produzem `missing_date`, enquanto mais de uma produz `duplicate_date`. No segundo caso, a primeira `DATE` está na posição correta e a segunda repete um singleton; a classificação específica prevalece sobre a expectativa genérica de `ITEM` na linha 3.

Uma linha `DATE:` vazia representa uma ocorrência estrutural presente com conteúdo vazio, e conteúdo vazio ou formato inválido permanecem fora do escopo. Os dois valores de `FX-023` são idênticos, mas a implementação não compara datas, não valida se representam o mesmo dia e não define comportamento específico para valores diferentes: a cardinalidade maior que um é suficiente.

`DATE:` é um prefixo reconhecido, inclusive na segunda ocorrência. Portanto, a repetição produz `duplicate_date`, não `unexpected_record`; este último permanece especificado, mas sem cenário executável.

`FX-023` contém um único `MERCHANT`; `missing_merchant` e `duplicate_merchant` não se aplicam, e a guarda de `duplicate_merchant` permanece anterior à de `duplicate_date`. O `ITEM` e o `TOTAL` são válidos, portanto também não se aplicam `missing_item`, `missing_total`, `duplicate_total`, `invalid_receipt_total`, `receipt_total_mismatch` ou erros numéricos e matemáticos do item.

O fluxo conceitual atualmente protegido é:

```text
empty_input
→ missing_merchant
→ missing_date
→ duplicate_merchant
→ duplicate_date
→ duplicate_total
→ invalid_record_order
→ validações dos ITEMs
→ missing_item
→ missing_total
→ validação do único TOTAL
→ saída válida
```

Essa sequência descreve os cenários isolados comprovados, não uma política geral para defeitos independentes simultâneos. Em `FX-023`, a detecção de `duplicate_date` interrompe o fluxo antes de `duplicate_total`, da validação posicional, do processamento de `ITEM` e da conversão de `TOTAL`.

O Green de `SCN-023` preservou `Decision: Keep explicit guards`: `date_records` foi reutilizado, a precedência permaneceu visível em `parse_receipt`, e nenhuma nova busca, helper, índice estrutural, enum, classe de registro, máquina de estados ou refatoração das demais guardas foi introduzida.

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
* `TEST-010` / `SCN-010`
* `TEST-011` / `SCN-011`
* `TEST-012` / `SCN-012`
* `TEST-013` / `SCN-013`
* `TEST-014` / `SCN-014`
* `TEST-015` / `SCN-015`
* `TEST-016` / `SCN-016`
* `TEST-017` / `SCN-017`
* `TEST-018` / `SCN-018`
* `TEST-019` / `SCN-019`
* `TEST-020` / `SCN-020`
* `TEST-021` / `SCN-021`
* `TEST-022` / `SCN-022`
* `TEST-023` / `SCN-023`

Planned but not yet implemented:

* None in the currently materialized harness.

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
* `SCN-010`
* `SCN-011`
* `SCN-012`
* `SCN-013`
* `SCN-014`
* `SCN-015`
* `SCN-016`
* `SCN-017`
* `SCN-018`
* `SCN-019`
* `SCN-020`
* `SCN-021`
* `SCN-022`
* `SCN-023`

### Estado do harness inicial

Os nove cenários definidos no harness inicial estão materializados e possuem testes automatizados. A suíte completa está verde, e o harness inicial agora serve como rede de segurança para revisão e refatoração.

`SCN-010` a `SCN-023` são expansões incrementais das lacunas já definidas na SPEC. O harness inicial continua sendo o conjunto de `TEST-001` a `TEST-009`; com as expansões implementadas, `TEST-001` a `TEST-023` estão verdes.

Não existem testes pendentes entre os artefatos atualmente materializados. Todos os vinte e três testes estão verdes.

### Lacunas ainda abertas

Permanecem abertas: `unexpected_record`; conteúdo vazio ou inválido de `MERCHANT`; conteúdo vazio ou formato inválido de `DATE`; `MERCHANT` deslocado em outras posições; `DATE` depois de `ITEM` como cenário dedicado; conteúdo depois de `TOTAL`; mais de duas ocorrências de registros singleton; positividade de `quantity`, `unit_price` e `receipt_total`; e precedências entre defeitos independentes simultâneos.

Antes de materializar `unexpected_record`, é necessária uma nova revisão da estrutura de reconhecimento. Essa revisão deverá avaliar manter guardas explícitas, introduzir uma classificação estrutural mínima, extrair somente um helper de reconhecimento ou adiar qualquer abstração, sem escolher uma solução antecipadamente neste harness.

O parser agora reconhece ocorrências estruturais de `MERCHANT`, `DATE` e `TOTAL`, com verificações locais de cardinalidade para mais de um tipo de registro. A repetição permanece pequena e explícita; uma revisão separada poderá avaliar se existe benefício concreto em extrair uma abstração. Nenhum helper deve ser criado apenas para reduzir linhas, e qualquer refatoração futura deverá preservar ordem, precedência, códigos públicos e números de linha já protegidos.

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
