# IA Automation Lab

Este repositório é um laboratório privado de estudo e prática para construir pequenos sistemas usando IA, automação, Spec-Driven Development, harnesses e agent coding.

O objetivo não é apenas criar projetos funcionando, mas desenvolver um processo disciplinado para transformar ideias em software pequeno, testável, verificável e evolutivo.

## Objetivo

O IA Automation Lab existe para estudar e praticar:

* desenvolvimento incremental;
* escrita de especificações antes do código;
* criação de harnesses de validação;
* uso de fixtures sintéticas;
* automação local;
* agent coding com validação humana;
* construção de pequenos produtos a partir de ideias reais.

A prioridade é aprender a construir sistemas com clareza, segurança e confiança, em vez de simplesmente acelerar a implementação.

## Como este laboratório funciona

Cada projeto deve começar pequeno.

Antes de criar aplicações completas, dashboards, integrações externas ou automações reais, os projetos devem passar por uma versão mínima local, com entradas e saídas explícitas.

O fluxo de trabalho recomendado é:

1. Entender o problema e o usuário real.
2. Definir o menor produto útil.
3. Escrever uma especificação curta.
4. Identificar entradas, saídas, regras e casos extremos.
5. Criar um harness mínimo para validar o comportamento.
6. Implementar em pequenos passos.
7. Testar com fixtures sintéticas ou dados anonimizados.
8. Refatorar apenas depois de validar.
9. Registrar decisões e próximos passos.

## Projeto ativo

O projeto ativo no momento é:

```text
projects/nota-fiscal-insight
```

Este projeto explora a leitura e estruturação de dados de notas fiscais, começando por uma versão local, pequena e testável.

O foco inicial é:

* definir o escopo;
* escrever a especificação;
* criar fixtures sintéticas;
* construir um harness mínimo;
* validar uma saída estruturada antes de evoluir para análises mais complexas.

Outras ideias de projeto ficam registradas em `PROJECT_IDEAS.md`.

## Estrutura do repositório

```text
.
├── AGENTS.md
├── DECISIONS.md
├── PROJECT_IDEAS.md
├── README.md
├── ROADMAP.md
├── projects
│   └── nota-fiscal-insight
│       ├── HARNESS.md
│       ├── README.md
│       ├── SPEC.md
│       ├── fixtures
│       ├── src
│       └── tests
└── templates
    ├── AGENT_PROMPT-template.md
    ├── HARNESS-template.md
    └── SPEC-template.md
```

## Arquivos principais

### `PROJECT_IDEAS.md`

Backlog de ideias de projetos.

Serve para registrar, comparar e priorizar projetos com base em valor didático, complexidade, risco, clareza de entrada e saída, facilidade de criar harness e dependência de integrações externas.

### `ROADMAP.md`

Ordem sugerida de execução dos projetos.

Deve explicar por que um projeto vem antes de outro e qual aprendizado cada etapa busca desenvolver.

### `DECISIONS.md`

Registro de decisões importantes.

Deve documentar trade-offs, mudanças de direção, escolhas técnicas e motivos para manter ou reduzir escopo.

### `AGENTS.md`

Instruções para agentes de programação, como Codex.

Define como agentes devem atuar neste repositório: ler especificações antes de codar, preferir tarefas pequenas, criar ou atualizar testes e evitar dados sensíveis.

### `templates/`

Modelos reutilizáveis para novos projetos.

Inclui templates de especificação, harness e prompts para agentes.

### `projects/`

Pasta com os projetos individuais do laboratório.

Cada projeto deve ter sua própria documentação, especificação, harness, fixtures, código e testes.

## Uso com ChatGPT

O ChatGPT é usado como mentor técnico, revisor crítico e parceiro de planejamento.

Seu papel neste laboratório é ajudar a:

* transformar ideias vagas em projetos pequenos;
* definir escopo;
* escrever especificações;
* propor harnesses;
* revisar decisões;
* criar prompts para agentes;
* avaliar riscos;
* sugerir próximos passos.

O ChatGPT não deve substituir a validação humana. As decisões finais, revisões de código e uso de dados reais continuam sendo responsabilidade do autor do projeto.

## Uso com Codex e agentes

Agentes de programação podem ser usados de forma experimental para implementar tarefas pequenas e bem especificadas.

Antes de pedir código a um agente, o projeto deve ter pelo menos:

* objetivo claro;
* entrada esperada;
* saída esperada;
* critérios de aceite;
* harness ou testes mínimos;
* restrições explícitas.

O uso ideal de agentes neste laboratório é:

1. revisar documentação;
2. propor melhorias de especificação;
3. criar estrutura inicial;
4. implementar pequenas funções;
5. criar ou ajustar testes;
6. explicar o que foi alterado.

Agentes não devem receber instruções amplas como “crie o app inteiro”. As tarefas devem ser pequenas, verificáveis e reversíveis.

## Segurança e privacidade

Este repositório é privado por enquanto.

Alguns projetos podem envolver dados sensíveis, como notas fiscais, gastos, aniversários, contatos ou informações de saúde. Por isso, a regra padrão é:

* não commitar dados pessoais reais;
* não usar CPF, endereço, telefone, e-mail ou identificadores reais em fixtures;
* não enviar dados sensíveis para prompts de agentes;
* usar dados sintéticos sempre que possível;
* anonimizar qualquer exemplo real antes de salvar;
* validar manualmente qualquer automação que possa causar efeito real.

Fixtures devem representar o formato dos dados, não preservar dados reais.

## Convenções de idioma

A documentação principal deste laboratório é escrita em português.

Código, nomes de arquivos, nomes de pastas, funções, variáveis e termos técnicos de implementação devem ser escritos em inglês sempre que fizer sentido.

Exemplos:

```text
Documentação: português
Código: inglês
Pastas: inglês
Funções: inglês
Commits: preferencialmente inglês ou português consistente
```

## Escopo inicial

Este laboratório deve favorecer:

* scripts locais;
* protótipos pequenos;
* linha de comando;
* arquivos de entrada e saída;
* fixtures sintéticas;
* testes simples;
* validação manual.

Não é objetivo inicial criar apps completos, dashboards, integrações frágeis ou automações com efeito real antes de validar o núcleo do comportamento.

## Status atual

Status: laboratório em fase inicial.

Projeto ativo:

```text
projects/nota-fiscal-insight
```

Foco atual:

```text
especificação, harness e fixtures sintéticas
```

## Próximos passos

1. Preencher `projects/nota-fiscal-insight/SPEC.md`.
2. Preencher `projects/nota-fiscal-insight/HARNESS.md`.
3. Criar fixtures sintéticas mínimas.
4. Definir a primeira saída esperada em JSON.
5. Criar o primeiro teste ou script de validação.
6. Só depois implementar o primeiro parser.
