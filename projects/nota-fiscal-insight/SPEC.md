# Nota Fiscal Insight — Project Specification

## Metadata

- **Project:** `nota-fiscal-insight`
- **Status:** `ready`
- **Stage:** `now`

O status deve mudar para `ready` somente após revisão humana e aprovação explícita desta especificação.

## Problem

Notas fiscais contêm dados úteis sobre estabelecimentos, produtos, quantidades e preços, mas essas informações não ficam organizadas de forma conveniente para análise pessoal.

O usuário precisa consultar documentos individualmente para tentar entender:

* quanto gastou;
* quais produtos comprou;
* onde realizou as compras;
* quais itens aparecem com mais frequência;
* como preços e gastos mudam ao longo do tempo.

Antes de produzir análises, o projeto precisa de uma forma confiável de transformar os dados de uma nota fiscal em uma estrutura previsível e validável.

A primeira versão resolve apenas essa etapa inicial.

## Target User

**Primary user:** o autor do projeto.

**Usage context:** processamento local de representações sintéticas de notas fiscais durante o desenvolvimento e a validação do parser.

O usuário inicial possui familiaridade básica com arquivos, terminal e execução de testes. Uma interface voltada a usuários não técnicos não faz parte desta versão.

## Goal

Transformar uma nota fiscal sintética, escrita em um formato de texto simples e controlado, em uma estrutura de dados que possa ser serializada como JSON.

A primeira versão também deve validar:

* a estrutura da entrada;
* o formato dos campos;
* o cálculo do total de cada item;
* a soma total da nota.

Entradas estruturalmente inválidas ou matematicamente inconsistentes devem ser rejeitadas com uma exceção estruturada.

## Scope

Esta versão inclui:

* recebimento de uma única nota fiscal sintética em texto;
* parsing de linhas com prefixos definidos;
* extração do estabelecimento;
* extração da data da compra;
* extração de um ou mais itens;
* suporte a quantidades inteiras e decimais;
* extração de preço unitário;
* extração do total de cada item;
* extração do total da nota;
* validação do cálculo de cada item;
* validação da soma total da nota;
* produção de uma estrutura compatível com JSON;
* erros estruturados com código e mensagem;
* suporte a linhas em branco;
* remoção de espaços externos dos valores.

## Non-goals

Esta versão não inclui:

* leitura de QR Code;
* download de notas fiscais;
* consulta a portais estaduais;
* parsing de HTML;
* parsing de NFC-e real;
* suporte a múltiplos formatos de entrada;
* suporte a vírgula como separador decimal;
* descontos;
* acréscimos;
* impostos;
* frete;
* arredondamentos específicos de estabelecimentos;
* formas de pagamento;
* CPF ou CNPJ;
* endereço do estabelecimento;
* chave de acesso fiscal;
* categorização de produtos;
* normalização de nomes de produtos;
* processamento em lote;
* armazenamento em banco de dados;
* API;
* CLI;
* frontend;
* dashboard;
* IA generativa.

O caractere `|` não pode fazer parte da descrição de um item nesta versão.

## Inputs

### IN-001 — Synthetic receipt text

**Description:** representação textual de uma única nota fiscal sintética.

**Format:** string de texto UTF-8 dividida em linhas.

A entrada deve seguir este formato:

```text
MERCHANT: <merchant_name>
DATE: <purchase_date>
ITEM: <description> | <quantity> | <unit_price> | <line_total>
ITEM: <description> | <quantity> | <unit_price> | <line_total>
TOTAL: <receipt_total>
```

### Example

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-01
ITEM: Arroz | 2 | 8.50 | 17.00
ITEM: Tomate | 0.750 | 10.00 | 7.50
TOTAL: 24.50
```

### Required record order

As linhas não vazias devem aparecer nesta ordem:

1. uma linha `MERCHANT`;
2. uma linha `DATE`;
3. uma ou mais linhas `ITEM`;
4. uma linha `TOTAL`.

Não pode haver linha não vazia depois de `TOTAL`.

### General parsing rules

* Linhas em branco devem ser ignoradas.
* Espaços no início e no final de cada linha devem ser ignorados.
* Espaços no início e no final de cada valor devem ser ignorados.
* Prefixos são case-sensitive.
* Apenas os prefixos `MERCHANT:`, `DATE:`, `ITEM:` e `TOTAL:` são aceitos.
* Uma linha não vazia com prefixo desconhecido deve causar erro.
* Campos obrigatórios não podem ficar vazios.
* A entrada deve representar exatamente uma nota fiscal.

### `MERCHANT`

Formato:

```text
MERCHANT: <merchant_name>
```

Regras:

* deve aparecer exatamente uma vez;
* deve ser a primeira linha não vazia;
* o nome deve permanecer não vazio depois da remoção de espaços externos;
* o nome será preservado como texto;
* nenhuma normalização avançada será realizada.

Exemplo válido:

```text
MERCHANT: Mercado Exemplo
```

### `DATE`

Formato:

```text
DATE: YYYY-MM-DD
```

Regras:

* deve aparecer exatamente uma vez;
* deve aparecer depois de `MERCHANT` e antes do primeiro `ITEM`;
* deve usar o formato ISO `YYYY-MM-DD`;
* deve representar uma data válida do calendário.

Exemplo válido:

```text
DATE: 2026-07-01
```

Exemplos inválidos:

```text
DATE: 01/07/2026
DATE: 2026-02-30
DATE: July 1, 2026
```

### `ITEM`

Formato:

```text
ITEM: <description> | <quantity> | <unit_price> | <line_total>
```

Cada linha deve conter exatamente quatro campos separados por `|`.

#### `description`

* deve ser uma string não vazia;
* espaços externos devem ser removidos;
* o texto interno deve ser preservado;
* não pode conter o caractere `|`.

#### `quantity`

* deve ser representada como string decimal;
* deve usar ponto como separador decimal;
* pode ser inteira ou decimal;
* pode ter no máximo três casas decimais;
* deve ser maior que zero;
* não pode conter sinal;
* não pode usar notação científica.

Exemplos válidos:

```text
1
2
0.750
1.5
```

Exemplos inválidos:

```text
0
-1
0,750
1.2345
1e3
```

#### `unit_price`

* deve usar exatamente duas casas decimais;
* deve usar ponto como separador decimal;
* deve ser maior que zero;
* não pode conter sinal;
* não pode usar notação científica.

Exemplos válidos:

```text
1.00
8.50
10.99
```

Exemplos inválidos:

```text
0
8.5
8,50
-8.50
1e2
```

#### `line_total`

* deve seguir as mesmas regras de formato monetário de `unit_price`;
* deve ser maior que zero;
* deve ser matematicamente igual a `quantity × unit_price`.

A comparação deve ser realizada com aritmética decimal exata, sem uso de ponto flutuante binário.

### `TOTAL`

Formato:

```text
TOTAL: <receipt_total>
```

Regras:

* deve aparecer exatamente uma vez;
* deve aparecer depois de todos os itens;
* deve ser a última linha não vazia;
* deve seguir o formato monetário com exatamente duas casas decimais;
* deve ser maior que zero;
* deve ser igual à soma dos valores `line_total`.

## Outputs

### OUT-001 — Structured receipt

**Description:** estrutura de dados representando a nota fiscal validada.

**Format:** objeto Python serializável como JSON.

### Schema

| Field                 | Type     | Required | Description                             |
| --------------------- | -------- | -------: | --------------------------------------- |
| `merchant`            | `object` |      yes | Informações do estabelecimento.         |
| `merchant.name`       | `string` |      yes | Nome extraído de `MERCHANT`.            |
| `purchase_date`       | `string` |      yes | Data ISO `YYYY-MM-DD`.                  |
| `items`               | `array`  |      yes | Itens na mesma ordem da entrada.        |
| `items[].description` | `string` |      yes | Descrição do item.                      |
| `items[].quantity`    | `string` |      yes | Quantidade textual validada.            |
| `items[].unit_price`  | `string` |      yes | Preço unitário com duas casas decimais. |
| `items[].line_total`  | `string` |      yes | Total do item com duas casas decimais.  |
| `receipt_total`       | `string` |      yes | Total da nota com duas casas decimais.  |

### Output rules

* A ordem dos itens deve ser preservada.
* Valores monetários devem permanecer como strings com duas casas decimais.
* A quantidade deve ser devolvida como a string recebida após remoção de espaços externos.
* A data deve permanecer no formato `YYYY-MM-DD`.
* Nenhum campo adicional deve ser produzido nesta versão.
* Uma entrada inválida não deve produzir uma saída parcial válida.

### Synthetic example

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
    },
    {
      "description": "Tomate",
      "quantity": "0.750",
      "unit_price": "10.00",
      "line_total": "7.50"
    }
  ],
  "receipt_total": "24.50"
}
```

## Domain Concepts and Glossary

### `Receipt`

Representa uma única nota fiscal sintética válida.

Contém um estabelecimento, uma data, pelo menos um item e o total da compra.

### `Merchant`

Representa o estabelecimento emissor da nota.

Nesta versão, contém apenas o nome textual.

### `ReceiptItem`

Representa uma linha de produto dentro da nota.

Contém descrição, quantidade, preço unitário e total da linha.

### `Quantity`

Representa a quantidade adquirida de um item.

Pode representar unidades inteiras ou quantidades decimais, como produtos vendidos por peso.

### `UnitPrice`

Representa o preço de uma unidade do item.

É um valor monetário com duas casas decimais.

### `LineTotal`

Representa o total declarado de um item.

Deve ser igual a:

```text
quantity × unit_price
```

### `ReceiptTotal`

Representa o valor total declarado da nota.

Deve ser igual à soma de todos os `line_total`.

### `StructuredReceipt`

Representa a saída validada e serializável como JSON.

### Glossary

| Term            | Meaning                                                  |
| --------------- | -------------------------------------------------------- |
| `raw_text`      | Texto completo recebido pelo parser.                     |
| `receipt`       | Nota fiscal processada pelo sistema.                     |
| `merchant`      | Estabelecimento associado à nota.                        |
| `receipt_item`  | Item individual presente na nota.                        |
| `quantity`      | Quantidade adquirida.                                    |
| `unit_price`    | Preço por unidade.                                       |
| `line_total`    | Total declarado para um item.                            |
| `receipt_total` | Total final declarado na nota.                           |
| `parser`        | Componente que transforma o texto em dados estruturados. |

## Business Rules

### BR-001 — Required structure

A entrada deve conter exatamente um `MERCHANT`, uma `DATE`, um ou mais `ITEM` e exatamente um `TOTAL`.

### BR-002 — Fixed record order

Os registros devem seguir a ordem:

```text
MERCHANT → DATE → ITEM... → TOTAL
```

### BR-003 — Item field count

Cada linha `ITEM` deve conter exatamente quatro campos separados por `|`.

### BR-004 — Positive quantity

A quantidade de cada item deve ser maior que zero.

### BR-005 — Positive monetary values

`unit_price`, `line_total` e `receipt_total` devem ser maiores que zero.

### BR-006 — Exact line-total validation

Para cada item:

```text
line_total = quantity × unit_price
```

A validação deve usar aritmética decimal exata.

### BR-007 — Exact receipt-total validation

O total da nota deve ser igual à soma de todos os `line_total`.

### BR-008 — Item order preservation

A saída deve preservar a ordem em que os itens aparecem na entrada.

### BR-009 — Atomic parsing

Uma entrada inválida deve ser rejeitada por inteiro.

O parser não deve retornar uma nota parcialmente válida.

### BR-010 — Unknown records are invalid

Qualquer linha não vazia que não corresponda a um registro suportado deve causar erro.

## Invariants

### INV-001 — At least one item

Uma nota válida sempre contém pelo menos um item.

### INV-002 — Positive values

Uma nota válida nunca contém quantidade ou valor monetário igual ou inferior a zero.

### INV-003 — Consistent item totals

Em uma nota válida, todo `line_total` corresponde exatamente ao produto de `quantity` por `unit_price`.

### INV-004 — Consistent receipt total

Em uma nota válida, `receipt_total` corresponde exatamente à soma dos totais dos itens.

### INV-005 — Complete valid output

Uma saída válida sempre contém:

* estabelecimento;
* data;
* pelo menos um item;
* total da nota.

### INV-006 — No partial result on failure

Quando houver qualquer erro, nenhuma estrutura parcial deve ser retornada como resultado válido.

## Error Contract

Falhas de parsing ou validação devem lançar:

```text
ReceiptValidationError
```

A exceção deve fornecer pelo menos:

| Attribute     | Type                | Required | Description                                  |
| ------------- | ------------------- | -------: | -------------------------------------------- |
| `code`        | `string`            |      yes | Identificador estável do erro.               |
| `message`     | `string`            |      yes | Explicação legível em inglês.                |
| `line_number` | `integer` ou `null` |      yes | Linha relacionada ao erro, quando aplicável. |

Exemplo conceitual:

```text
ReceiptValidationError
code: line_total_mismatch
message: Item line total does not match quantity multiplied by unit price.
line_number: 3
```

Os testes devem validar principalmente o `code`. A mensagem pode fornecer contexto humano, mas não deve ser usada como único contrato automatizado.

## Invalid Inputs and Error Behavior

### ERR-001 — `empty_input`

**Invalid condition:** a entrada está vazia ou contém apenas espaços e linhas em branco.

**Expected behavior:** lançar `ReceiptValidationError`.

**Line number:** `null`.

### ERR-002 — `missing_merchant`

**Invalid condition:** nenhum registro `MERCHANT` foi encontrado.

**Expected behavior:** rejeitar a entrada.

### ERR-003 — `duplicate_merchant`

**Invalid condition:** mais de um registro `MERCHANT` foi encontrado.

**Expected behavior:** rejeitar a entrada na segunda ocorrência.

### ERR-004 — `invalid_merchant`

**Invalid condition:** o nome do estabelecimento está vazio.

**Expected behavior:** rejeitar a entrada.

### ERR-005 — `missing_date`

**Invalid condition:** nenhum registro `DATE` foi encontrado.

**Expected behavior:** rejeitar a entrada.

### ERR-006 — `duplicate_date`

**Invalid condition:** mais de um registro `DATE` foi encontrado.

**Expected behavior:** rejeitar a entrada na segunda ocorrência.

### ERR-007 — `invalid_date`

**Invalid condition:** a data não usa `YYYY-MM-DD` ou não representa uma data válida.

**Expected behavior:** rejeitar a entrada.

### ERR-008 — `missing_item`

**Invalid condition:** nenhum registro `ITEM` foi encontrado.

**Expected behavior:** rejeitar a entrada.

### ERR-009 — `invalid_item_format`

**Invalid condition:** a linha `ITEM` não contém exatamente quatro campos separados por `|`.

**Expected behavior:** rejeitar a entrada.

### ERR-010 — `invalid_item_description`

**Invalid condition:** a descrição do item está vazia.

**Expected behavior:** rejeitar a entrada.

### ERR-011 — `invalid_quantity`

**Invalid condition:** a quantidade não respeita o formato definido ou não é maior que zero.

**Expected behavior:** rejeitar a entrada.

### ERR-012 — `invalid_unit_price`

**Invalid condition:** o preço unitário não respeita o formato monetário definido ou não é maior que zero.

**Expected behavior:** rejeitar a entrada.

### ERR-013 — `invalid_line_total`

**Invalid condition:** o total do item não respeita o formato monetário definido ou não é maior que zero.

**Expected behavior:** rejeitar a entrada.

### ERR-014 — `line_total_mismatch`

**Invalid condition:** `line_total` é diferente de `quantity × unit_price`.

**Expected behavior:** rejeitar a nota inteira.

### ERR-015 — `missing_total`

**Invalid condition:** nenhum registro `TOTAL` foi encontrado.

**Expected behavior:** rejeitar a entrada.

### ERR-016 — `duplicate_total`

**Invalid condition:** mais de um registro `TOTAL` foi encontrado.

**Expected behavior:** rejeitar a segunda ocorrência.

### ERR-017 — `invalid_receipt_total`

**Invalid condition:** o total da nota não respeita o formato monetário definido ou não é maior que zero.

**Expected behavior:** rejeitar a entrada.

### ERR-018 — `receipt_total_mismatch`

**Invalid condition:** `receipt_total` é diferente da soma dos `line_total`.

**Expected behavior:** rejeitar a nota inteira.

### ERR-019 — `unexpected_record`

**Invalid condition:** uma linha não vazia possui um prefixo desconhecido ou conteúdo sem prefixo válido.

**Expected behavior:** rejeitar a entrada.

### ERR-020 — `invalid_record_order`

**Invalid condition:** um registro válido aparece fora da ordem obrigatória.

Exemplos:

* `DATE` antes de `MERCHANT`;
* `ITEM` antes de `DATE`;
* `ITEM` depois de `TOTAL`;
* conteúdo não vazio depois de `TOTAL`.

**Expected behavior:** rejeitar a entrada.

## Acceptance Criteria

* **AC-001:** Uma entrada válida com um item deve produzir uma estrutura com estabelecimento, data, item e total.
* **AC-002:** Uma entrada válida com vários itens deve preservar a ordem dos itens na saída.
* **AC-003:** Quantidades inteiras devem ser aceitas e devolvidas como strings.
* **AC-004:** Quantidades decimais com até três casas devem ser aceitas e devolvidas como strings.
* **AC-005:** Valores monetários devem ser devolvidos como strings com exatamente duas casas decimais.
* **AC-006:** O parser deve rejeitar uma linha cujo `line_total` não corresponda a `quantity × unit_price`.
* **AC-007:** O parser deve rejeitar uma nota cujo `TOTAL` não corresponda à soma dos itens.
* **AC-008:** O parser deve rejeitar entradas sem estabelecimento, data, itens ou total.
* **AC-009:** O parser deve rejeitar registros fora da ordem definida.
* **AC-010:** O parser deve rejeitar formatos numéricos não suportados.
* **AC-011:** Erros devem ser representados por `ReceiptValidationError` com `code`, `message` e `line_number`.
* **AC-012:** Uma falha não deve produzir uma estrutura parcial válida.
* **AC-013:** Linhas em branco e espaços externos não devem alterar o resultado válido.
* **AC-014:** Nenhuma chamada de rede ou serviço externo deve ser necessária.

## Behavior Scenarios

### SCN-001 — Parse a valid receipt with one item

**Covers:** `AC-001`, `AC-003`, `AC-005`

**Given**

Uma entrada sintética válida contendo estabelecimento, data, um item e total.

**When**

O parser processar a entrada.

**Then**

A saída deve conter todos os campos definidos no schema.

**And**

Os valores monetários devem permanecer como strings com duas casas decimais.

### SCN-002 — Parse a valid receipt with multiple items

**Covers:** `AC-002`, `AC-007`

**Given**

Uma nota válida com vários itens e total igual à soma dos itens.

**When**

O parser processar a entrada.

**Then**

Todos os itens devem aparecer na saída.

**And**

A ordem dos itens deve ser igual à ordem da entrada.

### SCN-003 — Parse an item with decimal quantity

**Covers:** `AC-004`, `AC-005`

**Given**

Uma nota válida contendo um item com quantidade `0.750`.

**When**

O parser processar a entrada.

**Then**

A quantidade deve aparecer como a string `"0.750"`.

**And**

O cálculo do total deve usar aritmética decimal exata.

### SCN-004 — Reject an inconsistent item total

**Covers:** `AC-006`, `AC-011`, `AC-012`

**Given**

Uma nota em que `quantity × unit_price` não corresponde ao `line_total`.

**When**

O parser processar a entrada.

**Then**

Deve lançar `ReceiptValidationError`.

**And**

O código deve ser `line_total_mismatch`.

**And**

Nenhuma estrutura parcial deve ser retornada.

### SCN-005 — Reject an inconsistent receipt total

**Covers:** `AC-007`, `AC-011`, `AC-012`

**Given**

Uma nota em que a soma dos itens não corresponde ao valor `TOTAL`.

**When**

O parser processar a entrada.

**Then**

Deve lançar `ReceiptValidationError`.

**And**

O código deve ser `receipt_total_mismatch`.

### SCN-006 — Reject a missing required record

**Covers:** `AC-008`, `AC-011`

**Given**

Uma entrada sem um dos registros obrigatórios.

**When**

O parser processar a entrada.

**Then**

Deve lançar uma exceção com o código correspondente ao registro ausente.

### SCN-007 — Reject records in the wrong order

**Covers:** `AC-009`, `AC-011`

**Given**

Uma entrada contendo registros suportados em ordem inválida.

**When**

O parser processar a entrada.

**Then**

Deve lançar `ReceiptValidationError`.

**And**

O código deve ser `invalid_record_order`.

### SCN-008 — Ignore blank lines and external whitespace

**Covers:** `AC-013`

**Given**

Uma entrada válida com linhas em branco e espaços externos adicionais.

**When**

O parser processar a entrada.

**Then**

A saída deve ser equivalente à saída da mesma entrada sem os espaços adicionais.

### SCN-009 — Reject unsupported numeric formats

**Covers:** `AC-010`, `AC-011`

**Given**

Uma entrada que usa vírgula como separador decimal ou quantidade com mais de três casas.

**When**

O parser processar a entrada.

**Then**

Deve lançar a exceção estruturada correspondente ao campo inválido.

## Edge Cases

### EDGE-001 — Decimal quantity with three places

**Condition:** um item possui quantidade `0.750`.

**Expected behavior:** aceitar a quantidade, preservar a string e validar o cálculo usando `Decimal`.

### EDGE-002 — Leap-day purchase

**Condition:** a data é `2028-02-29`.

**Expected behavior:** aceitar a data por ser válida no calendário.

### EDGE-003 — Blank lines between records

**Condition:** existem linhas em branco entre registros válidos.

**Expected behavior:** ignorar as linhas em branco.

### EDGE-004 — External spaces around item fields

**Condition:**

```text
ITEM:   Arroz   |  2  |  8.50  |  17.00
```

**Expected behavior:** remover espaços externos e produzir os mesmos valores do formato sem espaços adicionais.

### EDGE-005 — Similar decimal values with different textual precision

**Condition:** a quantidade é `1.0` ou `1.00`.

**Expected behavior:** aceitar ambas, desde que respeitem o limite de três casas, e preservar a representação textual recebida.

## Privacy and Security

**Sensitive data involved:** `potentially`, mas não na primeira versão.

O domínio futuro pode envolver dados fiscais e histórico pessoal de consumo. A versão atual deve usar exclusivamente dados sintéticos.

### Risks

* fixtures podem copiar acidentalmente dados de notas reais;
* mensagens de erro podem reproduzir conteúdo sensível;
* futuras entradas reais podem conter identificadores pessoais e fiscais.

### Required protections

* usar apenas estabelecimentos, produtos, datas e valores fictícios;
* não adicionar notas reais ao Git;
* não usar CPF, chave de acesso, endereço ou QR Code real;
* evitar incluir o conteúdo completo da entrada em mensagens de erro;
* manter validações locais e sem rede;
* revisar fixtures antes de commits.

### Human validation required for

* qualquer uso futuro de nota fiscal real;
* qualquer alteração que permita acesso externo;
* qualquer integração com portais fiscais;
* qualquer armazenamento de histórico pessoal.

## External Dependencies

| ID        | Dependency      | Purpose                        | Required now? | Test substitute                         |
| --------- | --------------- | ------------------------------ | ------------: | --------------------------------------- |
| `DEP-001` | Portal de NFC-e | Obter notas reais no futuro.   |            no | Fixtures sintéticas locais.             |
| `DEP-002` | QR Code reader  | Ler URLs fiscais no futuro.    |            no | Texto sintético fornecido diretamente.  |
| `DEP-003` | Database        | Persistir histórico no futuro. |            no | Objetos em memória e arquivos expected. |

Nenhuma dependência externa é necessária para a primeira versão.

A implementação deve preferir a biblioteca padrão do Python.

## Assumptions

### ASM-001 — Controlled synthetic format

A primeira versão pode usar um formato artificial e rígido para ensinar parsing, validação e testes antes de lidar com documentos reais.

**Validation plan:** revisar a utilidade do formato depois que o primeiro ciclo de SPEC, harness e TDD estiver concluído.

### ASM-002 — Dot decimal separator

A entrada sintética usará ponto como separador decimal, mesmo que documentos brasileiros frequentemente apresentem vírgula.

**Validation plan:** tratar formatos brasileiros reais em uma fase futura com SPEC própria.

### ASM-003 — No discounts or adjustments

O total de uma nota corresponde diretamente à soma dos totais dos itens.

**Validation plan:** revisar quando descontos, acréscimos ou outras linhas fiscais entrarem no escopo.

### ASM-004 — Exact decimal arithmetic

Os cálculos podem ser representados com `Decimal` sem regras adicionais de arredondamento na primeira versão.

**Validation plan:** reconsiderar quando dados reais introduzirem arredondamento fiscal ou mais casas decimais.

## Open Questions

Não existem perguntas abertas bloqueantes para o primeiro cenário.

Decisões futuras, fora do escopo desta versão:

### Q-001 — Canonical quantity normalization

**Blocking:** `no`

**Question:** versões futuras devem preservar a representação textual da quantidade ou normalizar valores equivalentes?

**Current resolution:** preservar a string recebida após remoção de espaços externos.

### Q-002 — Public function signature

**Blocking:** `no`

**Question:** qual será o nome definitivo da função Python?

**Current resolution:** definir no `HARNESS.md` antes do primeiro teste. Uma opção inicial é `parse_receipt(raw_text: str)`.

### Q-003 — Package structure

**Blocking:** `no`

**Question:** o código será inicialmente um único módulo ou um pequeno package Python?

**Current resolution:** decidir junto da stack mínima e do primeiro comando de teste, evitando estrutura antecipada.

## Traceability

| Acceptance criterion | Related rules                  | Scenarios            |
| -------------------- | ------------------------------ | -------------------- |
| `AC-001`             | `BR-001`, `INV-005`            | `SCN-001`            |
| `AC-002`             | `BR-008`                       | `SCN-002`            |
| `AC-003`             | `BR-004`                       | `SCN-001`            |
| `AC-004`             | `BR-004`                       | `SCN-003`            |
| `AC-005`             | `BR-005`                       | `SCN-001`, `SCN-003` |
| `AC-006`             | `BR-006`, `INV-003`            | `SCN-004`            |
| `AC-007`             | `BR-007`, `INV-004`            | `SCN-002`, `SCN-005` |
| `AC-008`             | `BR-001`, `INV-001`, `INV-005` | `SCN-006`            |
| `AC-009`             | `BR-002`                       | `SCN-007`            |
| `AC-010`             | `BR-004`, `BR-005`             | `SCN-009`            |
| `AC-011`             | Error Contract                 | `SCN-004`–`SCN-009`  |
| `AC-012`             | `BR-009`, `INV-006`            | `SCN-004`, `SCN-005` |
| `AC-013`             | General parsing rules          | `SCN-008`            |
| `AC-014`             | `DEC-004`                      | Todos os cenários    |

## Specification Readiness Checklist

### Problem and scope

* [x] O problema está descrito sem presumir uma aplicação web ou arquitetura final.
* [x] O usuário principal está identificado.
* [x] O objetivo desta versão é pequeno e observável.
* [x] O escopo incluído está explícito.
* [x] Os non-goals estão explícitos.
* [x] O projeto continua dentro da fase definida no `ROADMAP.md`.

### Behavior

* [x] A entrada está definida.
* [x] A saída está definida.
* [x] Os conceitos principais do domínio estão descritos.
* [x] As regras de negócio estão identificadas.
* [x] As invariants relevantes estão identificadas.
* [x] Os critérios de aceite são verificáveis.
* [x] Todo critério de aceite possui cenário ou forma de validação relacionada.
* [x] Existem cenários Given–When–Then para os comportamentos principais.
* [x] Entradas inválidas possuem comportamento de erro definido.
* [x] Casos extremos relevantes foram considerados.

### Safety and dependencies

* [x] Os riscos de privacidade e segurança foram avaliados.
* [x] Os exemplos usam somente dados sintéticos.
* [x] Dependências externas foram identificadas.
* [x] Dependências não essenciais foram adiadas ou substituídas.
* [x] A necessidade futura de validação humana está explícita.

### Readiness

* [x] As assumptions relevantes estão registradas.
* [x] Não existem contradições conhecidas.
* [x] Não existem perguntas abertas que bloqueiem o primeiro incremento.
* [x] A rastreabilidade entre critérios, regras e cenários foi preenchida.
* [x] O comportamento pode ser transformado em fixtures e testes.
* [x] O `HARNESS.md` pode ser elaborado a partir desta SPEC.
- [x] A SPEC foi revisada e aprovada pelo usuário.
- [x] O status foi alterado de `draft` para `ready`.

## Specification Approval

- **Reviewed by:** project owner
- **Decision:** `approved`
- **Notes:** A especificação foi revisada e aprovada para orientar a elaboração do harness e o primeiro ciclo de implementação.
