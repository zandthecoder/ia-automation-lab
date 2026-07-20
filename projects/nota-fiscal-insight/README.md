# Nota Fiscal Insight

O Nota Fiscal Insight é uma ferramenta local para transformar informações de notas fiscais brasileiras em dados estruturados, criando uma base confiável para futuras análises de gastos.

O projeto começa como um parser pequeno e testável. A primeira versão não tenta consultar notas reais, acessar QR Codes ou produzir dashboards. O foco inicial é aprender a especificar, validar e implementar um comportamento simples usando dados sintéticos.

## Overview

Notas fiscais contêm informações úteis sobre estabelecimentos, produtos, quantidades e preços, mas esses dados normalmente não ficam organizados de forma conveniente para análise pessoal.

O projeto busca transformar uma representação controlada de uma nota fiscal em uma saída JSON estruturada.

A primeira versão funciona apenas com arquivos sintéticos locais. Futuramente, o projeto poderá evoluir para importar documentos reais anonimizados e produzir análises de consumo.

## Problem

O usuário inicial do projeto deseja compreender melhor seus gastos em mercados, padarias e outros estabelecimentos.

Hoje, consultar notas fiscais individualmente dificulta responder perguntas como:

* em quais estabelecimentos o dinheiro é gasto;
* quais produtos são comprados com mais frequência;
* quanto é gasto em cada categoria;
* como os preços mudam ao longo do tempo;
* quais estabelecimentos oferecem melhores preços para determinados produtos.

A primeira versão não responderá ainda a todas essas perguntas.

Ela criará a base necessária para isso: uma representação estruturada e validável dos dados de uma nota fiscal.

## Target User

O usuário inicial é o próprio autor do projeto.

Ele deseja importar e organizar dados de compras pessoais para compreender padrões de consumo, especialmente em mercados e padarias.

Nesta fase, o projeto é uma ferramenta local de estudo e uso pessoal. Uma possível evolução para outros usuários será considerada somente depois que o núcleo estiver confiável e bem testado.

## Current Goal

O objetivo da primeira versão é:

> Transformar uma nota fiscal sintética em texto simples estruturado em uma saída JSON previsível e validável.

A entrada inicial será criada manualmente e seguirá um formato controlado.

Exemplo conceitual:

```text
MERCHANT: Mercado Exemplo
DATE: 2026-07-01
ITEM: Arroz | 2 | 8.50 | 17.00
TOTAL: 17.00
```

A saída será um documento JSON estruturado.

Exemplo conceitual:

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

Os campos definitivos, regras e formatos serão definidos em `SPEC.md`.

## Current Scope

A primeira versão inclui:

* leitura de uma entrada sintética local;
* parsing de texto simples estruturado;
* identificação do estabelecimento;
* identificação da data da compra;
* extração da lista de itens;
* extração de quantidade;
* extração de preço unitário;
* extração do total de cada item;
* extração do total da nota;
* geração de uma saída JSON estruturada;
* tratamento previsível de entradas inválidas;
* validação com fixtures e testes automatizados.

## Non-goals

A primeira versão não inclui:

* leitura automática de QR Codes;
* acesso a portais fiscais;
* download de notas reais;
* scraping;
* suporte a todos os formatos brasileiros de nota fiscal;
* uso de CPF ou chave de acesso;
* categorização automática de produtos;
* normalização avançada de nomes;
* banco de dados;
* histórico de compras;
* dashboard;
* interface gráfica;
* aplicativo mobile;
* análise de preços;
* comparação entre estabelecimentos;
* IA generativa.

Essas capacidades podem ser consideradas em fases futuras, depois que o parser local estiver especificado e validado.

## How It Works

O fluxo inicial será:

```text
synthetic receipt text
        ↓
local parser
        ↓
structured data
        ↓
JSON output
        ↓
comparison with expected output
```

A lógica principal será implementada primeiro como uma função Python testável.

Uma interface de linha de comando poderá ser adicionada posteriormente, desde que não complique o primeiro ciclo de aprendizado.

## Project Structure

```text
nota-fiscal-insight/
├── HARNESS.md
├── README.md
├── SPEC.md
├── fixtures/
│   ├── inputs/
│   └── expected/
├── src/
└── tests/
```

### `README.md`

Apresenta o projeto, seu objetivo atual, limites e modo de trabalho.

### `SPEC.md`

Define o comportamento esperado da primeira versão.

Deve conter:

* entradas;
* saídas;
* conceitos do domínio;
* regras de negócio;
* invariants;
* critérios de aceite;
* cenários Given–When–Then;
* erros;
* edge cases;
* non-goals.

### `HARNESS.md`

Define como o comportamento especificado será validado.

Deve relacionar:

* critérios de aceite;
* cenários;
* fixtures;
* resultados esperados;
* testes;
* comandos de validação;
* condições de sucesso e falha.

### `fixtures/inputs/`

Contém representações sintéticas de notas fiscais usadas como entrada nos testes.

### `fixtures/expected/`

Contém saídas esperadas usadas para validar o comportamento do parser.

### `src/`

Contém o código de produção.

A implementação deve começar somente depois que a SPEC e o harness estiverem prontos.

### `tests/`

Contém os testes automatizados que comprovam o comportamento definido na SPEC.

## Documentation

Os documentos devem ser consultados nesta ordem durante a implementação:

1. `/AGENTS.md`;
2. `README.md`;
3. `SPEC.md`;
4. `HARNESS.md`;
5. decisões relevantes em `/DECISIONS.md`;
6. arquivos diretamente relacionados à tarefa.

O `README.md` apresenta o projeto, mas não substitui a especificação.

Em caso de divergência, o comportamento aprovado em `SPEC.md` e a estratégia descrita em `HARNESS.md` devem orientar a implementação.

## Development Workflow

O projeto seguirá este fluxo:

```text
SPEC
→ HARNESS
→ fixture
→ expected output
→ failing test
→ minimum implementation
→ validation
→ human review
→ commit
```

### 1. Specification

Definir o comportamento antes de escrever código de produção.

### 2. Harness design

Definir como cada comportamento será comprovado.

### 3. Fixtures

Criar entradas sintéticas pequenas e representativas.

### 4. Expected outputs

Definir a saída correta antes da implementação.

### 5. Failing test

Criar um teste que falhe pelo motivo esperado.

### 6. Minimum implementation

Adicionar apenas o código necessário para fazer o cenário atual passar.

### 7. Validation

Executar o teste relacionado e o harness do projeto.

### 8. Human review

Revisar o diff, o comportamento, os testes e possíveis ampliações de escopo.

### 9. Commit

Criar um commit pequeno e compreensível depois da revisão humana.

## Testing Approach

O projeto combinará três abordagens leves.

### Spec-Driven Development

A implementação deriva de uma especificação revisada.

### Behavior-Driven Development

Comportamentos importantes serão descritos em cenários Given–When–Then dentro da SPEC.

### Test-Driven Development

Cada comportamento será implementado usando o ciclo:

```text
Red
→ Green
→ Refactor
```

* `Red`: criar um teste que falha pelo motivo esperado;
* `Green`: implementar o mínimo para fazê-lo passar;
* `Refactor`: melhorar o código sem alterar o comportamento.

O projeto pode utilizar golden tests para comparar a saída JSON produzida com um arquivo esperado.

## Privacy and Data Safety

O projeto começa exclusivamente com dados sintéticos.

Não devem ser adicionados ao repositório:

* notas fiscais reais;
* CPF;
* CNPJ real associado a uma compra pessoal;
* endereços reais;
* chaves de acesso fiscal;
* QR Codes reais;
* histórico pessoal de consumo;
* informações de pagamento;
* tokens;
* credenciais;
* cookies;
* sessões de portais fiscais.

Fixtures devem representar o formato e o comportamento necessários sem preservar dados de pessoas, documentos ou compras reais.

Caso uma nota real seja usada futuramente para validação:

* ela deve ser anonimizada;
* deve permanecer fora do Git;
* deve ser processada localmente;
* dados identificáveis devem ser removidos;
* o uso deve ser documentado;
* a saída deve ser revisada antes de ser compartilhada.

## Current Status

* **Stage:** `now`
* **SPEC:** `ready`
* **HARNESS:** `draft`

O comportamento da primeira versão está definido e aprovado na SPEC. O harness está documentado, mas ainda precisa ser materializado e validado antes do primeiro código de produção.

Ainda não existe implementação de produção.

O foco atual é:

* criar a primeira fixture sintética e seu expected output;
* revisar esses artefatos contra a SPEC;
* preparar o ambiente de teste definido no harness;
* criar e executar o primeiro teste para observar a falha esperada;
* tornar o harness pronto para autorizar a implementação mínima de `SCN-001`.

## Known Limitations

A primeira versão trabalhará com um formato sintético controlado.

Portanto, mesmo quando todos os testes estiverem passando, isso não demonstrará que o parser consegue processar:

* páginas reais de NFC-e;
* HTML produzido por diferentes estados;
* notas de diferentes estabelecimentos;
* abreviações reais de produtos;
* descontos;
* impostos;
* unidades variadas;
* cancelamentos;
* documentos incompletos;
* mudanças em portais fiscais;
* grandes volumes de notas.

Essas limitações devem ser tratadas como parte explícita do escopo, e não como falhas escondidas.

## Future Possibilities

Depois que o núcleo local estiver confiável, o projeto poderá explorar:

* importação por QR Code;
* leitura de páginas reais anonimizadas;
* consolidação de várias notas;
* armazenamento de histórico;
* normalização de nomes de produtos;
* categorização de itens;
* análise de gastos por categoria;
* comparação entre estabelecimentos;
* acompanhamento de preços;
* detecção de recorrência de compra;
* relatórios e visualizações.

Cada evolução deverá ter uma nova especificação, um novo harness e critérios de aceite próprios.

## Running the Project

Ainda não existe uma aplicação ou um comando de produção. A primeira interface será a função Python `parse_receipt(raw_text: str)`, chamada diretamente pelos testes.

A tecnologia inicial já definida é:

* ambiente de desenvolvimento: Windows 11;
* shell: PowerShell;
* runtime: Python 3.13;
* test runner: `pytest`;
* ambiente virtual: `venv`;
* dependências de produção: apenas a biblioteca padrão do Python.

Os comandos automatizados usam diretamente:

```text
.\.venv\Scripts\python.exe
```

A ativação por `Activate.ps1` não é exigida. Os comandos detalhados de preparação e validação estão documentados em `HARNESS.md` e ainda precisam ser executados no ambiente local.

Frontend, API, banco de dados e arquitetura web permanecem indefinidos e fora do escopo atual.

## Next Milestone

O próximo marco é:

> Materializar e validar o primeiro ciclo do harness antes de implementar o parser.

Esse marco estará concluído quando:

* `FX-001` existir no repositório;
* `EXP-001` existir e tiver sido revisado contra a SPEC;
* o ambiente virtual e o `pytest` estiverem disponíveis;
* `TEST-001` puder ser importado e executado;
* o primeiro teste tiver falhado pelo motivo esperado;
* o harness tiver sido revisado e estiver `ready`.
