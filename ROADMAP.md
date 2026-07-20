# Roadmap

Este arquivo define a sequência de evolução do IA Automation Lab.

O roadmap não usa datas fixas. A progressão acontece por fases e por evidências concretas de aprendizado, implementação e validação.

A terminologia usada é:

* `now`: foco ativo;
* `then`: próximo projeto planejado;
* `later`: projetos futuros, ainda sem compromisso de execução imediata.

## Objetivo

O objetivo deste roadmap é organizar uma sequência de projetos que permita praticar, de forma incremental:

* Spec-Driven Development;
* criação de harnesses;
* uso de fixtures;
* testes automatizados;
* agent coding;
* revisão humana;
* Git;
* automação;
* validação de sistemas com IA.

Cada fase deve introduzir novos desafios sem abandonar as práticas aprendidas anteriormente.

O laboratório não busca concluir o maior número possível de projetos. A prioridade é desenvolver um processo de construção confiável, repetível e compreensível.

## Princípios de progressão

### Um projeto ativo por vez

Apenas um projeto deve permanecer com status `now`.

Novas ideias podem ser registradas em `PROJECT_IDEAS.md`, mas não devem iniciar implementação enquanto o projeto atual não atingir seu marco mínimo de conclusão.

Essa regra existe para evitar dispersão e permitir uma retrospectiva real sobre cada ciclo.

### Avanço baseado em evidências

Um projeto não é considerado concluído apenas porque existe código funcionando.

Para avançar, deve haver evidência de que:

* o comportamento esperado foi especificado;
* entradas e saídas foram definidas;
* fixtures representam cenários relevantes;
* existe um harness ou conjunto de testes;
* os testes passam;
* as limitações estão documentadas;
* as alterações do agente foram revisadas;
* as decisões importantes foram registradas.

### Núcleo local antes de integrações

Cada projeto deve começar como um sistema local, pequeno e previsível.

Antes de adicionar APIs, notificações, dashboards, autenticação ou automações reais, o núcleo do comportamento deve funcionar com:

* dados sintéticos;
* arquivos locais;
* execução manual;
* saídas explícitas;
* testes reproduzíveis.

### IA como ferramenta, não como fonte de verdade

Agentes podem ajudar a:

* revisar especificações;
* criar estrutura;
* implementar tarefas pequenas;
* escrever testes;
* sugerir refatorações;
* documentar decisões.

Toda alteração relevante deve ser validada por uma pessoa.

O agente não decide sozinho se uma tarefa está pronta.

### Git como parte do aprendizado

Git deve ser usado desde o início para:

* registrar pequenas alterações;
* comparar versões;
* reverter mudanças;
* revisar o trabalho do agente;
* manter histórico de decisões;
* experimentar com segurança.

Os commits devem ser pequenos e representar uma mudança compreensível.

Exemplos:

```text
docs: define initial receipt parser scope
test: add synthetic receipt fixtures
feat: parse receipt total
fix: reject missing item prices
```

## Estado atual

| Stage   | Project               | Status        |
| ------- | --------------------- | ------------- |
| `now`   | `nota-fiscal-insight` | em preparação |
| `then`  | `salad-jar-generator` | planejado     |
| `later` | `reading-companion`   | candidato     |
| `later` | `birthday-aggregator` | futuro        |
| `later` | `medication-manager`  | futuro        |

## Phase 0 — Laboratory Setup

**Stage:** `completed`
**Status:** concluída

### Objetivo de aprendizado

Preparar um ambiente mínimo para executar os projetos com organização, versionamento e instruções claras para agentes.

### Escopo mínimo

* criar a estrutura de pastas;
* escrever os documentos principais;
* inicializar o repositório Git;
* definir regras para agentes;
* criar templates reutilizáveis;
* escolher o primeiro projeto ativo.

### Entregáveis

* `README.md`;
* `PROJECT_IDEAS.md`;
* `ROADMAP.md`;
* `DECISIONS.md`;
* `AGENTS.md`;
* templates de `SPEC`, `HARNESS` e agent prompt;
* pasta do primeiro projeto;
* primeiro commit no Git.

### Critério de conclusão

Esta fase foi concluída com:

* a estrutura inicial versionada;
* os arquivos principais com conteúdo mínimo;
* o projeto ativo definido;
* o repositório disponível no editor e no Codex;
* pelo menos um commit inicial.

### O que não fazer ainda

* escolher stack definitiva;
* criar arquitetura complexa;
* adicionar banco de dados;
* configurar cloud;
* criar CI/CD;
* integrar APIs externas;
* implementar o parser antes da especificação.

---

## Phase 1 — Nota Fiscal Insight

**Stage:** `now`
**Status:** projeto ativo

### Objetivo de aprendizado

Praticar o primeiro ciclo completo de Spec-Driven Development com um problema real e um núcleo local testável.

Esta fase deve ensinar a transformar exemplos de entrada em uma especificação, fixtures, harness e implementação incremental.

### Conceitos principais

* especificação de comportamento;
* parsing;
* fixtures sintéticas;
* schema de saída;
* golden tests;
* testes de regressão;
* Git;
* delegação de tarefas pequenas ao Codex;
* revisão de código gerado por agente.

Um golden test compara a saída produzida pelo sistema com um arquivo de referência considerado correto.

### Escopo mínimo

Dada uma representação sintética de uma nota fiscal, gerar um JSON estruturado contendo:

* estabelecimento;
* data da compra;
* itens;
* quantidade;
* preço unitário;
* preço total de cada item;
* valor total da nota.

### Entregáveis

* `projects/nota-fiscal-insight/README.md`;
* `projects/nota-fiscal-insight/SPEC.md`;
* `projects/nota-fiscal-insight/HARNESS.md`;
* schema da saída;
* pelo menos três fixtures sintéticas;
* saídas esperadas;
* parser local;
* testes automatizados;
* instruções de execução;
* registro de decisões e limitações.

### Harness mínimo

O harness deve:

1. carregar uma fixture;
2. executar o parser;
3. produzir uma saída estruturada;
4. comparar a saída com o resultado esperado;
5. indicar diferenças de forma clara;
6. retornar erro quando a validação falhar.

Exemplo conceitual:

```text
fixture input
    ↓
parser
    ↓
generated JSON
    ↓
comparison with expected JSON
    ↓
pass or fail
```

### Cenários mínimos

As fixtures devem incluir pelo menos:

1. nota válida com um item;
2. nota válida com vários itens;
3. entrada incompleta ou inválida.

### Partes mockadas

* consulta via QR Code;
* download automático;
* páginas governamentais;
* categorização por IA;
* banco de dados;
* dashboard;
* dados reais;
* análise histórica de gastos.

Mock significa substituir temporariamente uma dependência real por uma versão controlada e previsível.

### Critério de conclusão

A primeira versão estará concluída quando:

* a SPEC estiver revisada;
* o HARNESS estiver documentado;
* existirem pelo menos três fixtures sintéticas;
* o schema de saída estiver definido;
* o parser funcionar para todos os cenários suportados;
* os testes automatizados estiverem passando;
* casos inválidos produzirem erros claros;
* limitações estiverem documentadas;
* alterações relevantes tiverem sido versionadas com Git;
* uma retrospectiva estiver registrada em `DECISIONS.md`.

### O que não fazer ainda

* suportar todos os formatos de nota;
* acessar QR Codes reais automaticamente;
* armazenar notas em banco de dados;
* usar dados fiscais reais no repositório;
* categorizar produtos com IA;
* criar interface gráfica;
* construir dashboard;
* criar app mobile.

### Próxima decisão

Ao concluir a fase, decidir entre:

* encerrar a primeira versão e avançar;
* executar uma validação opcional com uma nota real anonimizada;
* corrigir lacunas encontradas na retrospectiva.

A validação com dado real não é obrigatória para avançar.

---

## Phase 2 — Salad Jar Generator

**Stage:** `then`
**Status:** planejado

### Objetivo de aprendizado

Praticar modelagem de regras de negócio e construção de um motor determinístico.

Determinístico significa que a mesma entrada, combinada com a mesma configuração, produz um resultado reproduzível.

### Conceitos principais

* regras de negócio;
* validação de entrada;
* separação entre dados e lógica;
* testes parametrizados;
* restrições;
* casos sem solução;
* refatoração orientada por testes.

Testes parametrizados executam a mesma regra com diferentes conjuntos de entrada e saída esperada.

### Escopo mínimo

Dado um conjunto de ingredientes e restrições, gerar combinações válidas de saladas de pote.

A primeira versão deve trabalhar com regras explícitas, sem depender de IA generativa.

### Entregáveis

* SPEC;
* HARNESS;
* catálogo sintético de ingredientes;
* regras de composição;
* casos válidos e inválidos;
* motor local;
* testes parametrizados;
* documentação de decisões.

### Harness mínimo

Validar que:

* ingredientes proibidos não sejam usados;
* categorias obrigatórias estejam presentes;
* a ordem de montagem seja respeitada;
* entradas impossíveis produzam erro claro;
* resultados sejam reproduzíveis.

### Partes mockadas

* banco nutricional;
* calorias;
* recomendações médicas;
* preços;
* estoque real;
* integração com supermercados;
* geração por IA;
* interface visual.

### Critério de conclusão

A fase estará concluída quando:

* as regras estiverem documentadas;
* o motor gerar combinações válidas;
* casos impossíveis forem tratados;
* os testes cobrirem as regras principais;
* os dados estiverem separados da lógica;
* a retrospectiva estiver registrada.

### O que não fazer ainda

* personalização nutricional avançada;
* recomendação médica;
* integração com compras;
* app mobile;
* geração livre por LLM;
* planejamento semanal completo.

---

## Phase 3 — Reading Companion

**Stage:** `later`
**Status:** candidato

### Objetivo de aprendizado

Praticar importação, normalização, matching e geração de relatórios a partir de fontes de dados diferentes.

Matching significa encontrar correspondência entre registros que representam a mesma entidade, mesmo quando os textos não são exatamente iguais.

### Conceitos principais

* parsing de CSV;
* normalização;
* modelagem de domínio;
* matching;
* catálogos locais;
* tratamento de dados incompletos;
* relatórios derivados;
* contract tests.

Um contract test valida se componentes ou formatos de dados respeitam um contrato previamente definido.

### Escopo mínimo

Importar um CSV sintético compatível com o formato esperado, cruzar os livros com um catálogo local de séries e gerar um relatório de progresso.

O relatório deve mostrar:

* série;
* último livro lido;
* próximo livro;
* status da série;
* registros não reconhecidos.

### Entregáveis

* CSV sintético;
* catálogo local de séries;
* parser;
* normalizador;
* lógica de matching;
* relatório;
* testes;
* documentação de casos ambíguos.

### Harness mínimo

Usar duas ou três séries sintéticas e validar que:

* o último livro lido seja identificado;
* o próximo livro seja sugerido;
* séries completas sejam marcadas corretamente;
* livros desconhecidos sejam reportados;
* variações simples de título sejam normalizadas.

### Partes mockadas

* API do Goodreads;
* consulta de lançamentos;
* resumos por IA;
* scraping;
* notificações;
* integrações com leitores digitais.

### Critério de conclusão

A fase estará concluída quando:

* o CSV for importado corretamente;
* o catálogo for processado;
* o progresso das séries for calculado;
* casos desconhecidos forem reportados;
* as regras de matching estiverem testadas;
* uma retrospectiva estiver registrada.

### O que não fazer ainda

* sincronização automática;
* monitoramento de lançamentos;
* notificações;
* catálogo global;
* resumos extensos;
* integração com Goodreads, Kindle ou StoryGraph.

---

## Phase 4 — Birthday Aggregator

**Stage:** `later`
**Status:** futuro

### Objetivo preliminar

Praticar agregação de múltiplas fontes, deduplicação, revisão manual e manipulação segura de dados pessoais.

### Escopo preliminar

Importar fontes locais sintéticas, normalizar registros e gerar uma lista unificada de próximos aniversários.

### Possíveis aprendizados

* deduplicação;
* normalização de nomes;
* merge de registros;
* níveis de confiança;
* revisão humana;
* geração de arquivos `.ics`;
* privacidade.

### Riscos principais

* dados pessoais;
* falsos merges;
* APIs limitadas;
* integração com iOS;
* dependência de plataformas externas.

### Limite atual

Esta fase não deve ser detalhada nem iniciada antes da retrospectiva dos três primeiros projetos.

O primeiro protótipo deve ser um agregador local, não um widget.

---

## Phase 5 — Medication Manager

**Stage:** `later`
**Status:** futuro

### Objetivo preliminar

Praticar modelagem de agendas e validação de regras em um domínio sensível, mantendo o sistema estritamente como protótipo educacional.

### Escopo preliminar

Gerar uma agenda simulada a partir de medicamentos e horários sintéticos.

### Possíveis aprendizados

* agendamento;
* validação de inconsistências;
* dados sensíveis;
* segurança;
* limites de automação;
* validação humana.

### Riscos principais

* impacto na saúde;
* falsa confiança;
* privacidade;
* responsabilidade;
* falha em lembretes;
* uso incorreto como orientação médica.

### Limite atual

Este projeto não deve:

* fornecer orientação médica;
* sugerir alterações de dose;
* identificar interações medicamentosas;
* usar prescrições reais;
* ativar notificações reais;
* substituir médicos, farmacêuticos ou cuidadores.

A fase só deve ser reconsiderada quando o laboratório já tiver maturidade em specs, harnesses, testes e validação.

## Critérios para avançar de fase

Antes de mover um projeto de `now` para concluído e promover o próximo projeto, verificar:

### Especificação

* O problema está claro?
* A entrada está definida?
* A saída está definida?
* As regras estão documentadas?
* O escopo negativo está explícito?

Escopo negativo descreve aquilo que o projeto deliberadamente não faz.

### Harness

* Há fixtures suficientes?
* Existem resultados esperados?
* O comportamento pode ser reproduzido?
* Falhas são fáceis de entender?
* Casos inválidos foram testados?

### Implementação

* O núcleo mínimo funciona?
* As dependências são justificadas?
* O código está simples?
* Os testes passam?
* A implementação respeita a SPEC?

### Agent coding

* As tarefas dadas ao agente foram pequenas?
* O agente recebeu critérios de aceite?
* As mudanças foram revisadas?
* Houve alguma alteração inesperada?
* O agente executou os testes?

### Git

* As mudanças foram versionadas?
* Os commits são pequenos e compreensíveis?
* É possível reverter a implementação?
* Arquivos sensíveis estão ignorados?
* O histórico ajuda a entender a evolução?

### Documentação

* As limitações estão registradas?
* As decisões importantes estão em `DECISIONS.md`?
* As instruções de execução funcionam?
* O próximo passo está claro?

## Retrospectiva obrigatória

Ao final de cada fase, registrar em `DECISIONS.md`:

* o que funcionou;
* o que não funcionou;
* onde o agente ajudou;
* onde o agente errou;
* quais prompts foram eficazes;
* quais testes detectaram problemas;
* quais instruções estavam ambíguas;
* o que deve mudar nos templates;
* qual habilidade precisa ser reforçada;
* por que o projeto foi encerrado ou continuado.

A retrospectiva deve acontecer antes de iniciar a implementação do próximo projeto.

## Definições de conclusão

### Projeto concluído

Um projeto está concluído quando atingiu o objetivo didático definido para sua fase.

Isso não significa que o produto está completo ou pronto para uso público.

### Projeto evoluído

Um projeto concluído pode receber novas fases no futuro, desde que a nova evolução tenha:

* objetivo claro;
* nova SPEC;
* novo harness;
* critérios de aceite;
* justificativa de valor.

### Laboratório

O IA Automation Lab é um processo contínuo de estudo.

Não existe um estado final obrigatório para o laboratório inteiro.

## Regra para automações com efeito real

Nenhuma integração externa, notificação ou automação com efeito real deve ser adicionada antes que o núcleo local tenha:

* SPEC revisada;
* harness funcionando;
* testes automatizados;
* dados sintéticos;
* validação manual;
* riscos documentados;
* mecanismo seguro de interrupção ou reversão.

Quando houver dados sensíveis ou efeitos reais, a validação humana é obrigatória.

## Fora do escopo atual

Não fazem parte do roadmap inicial:

* apps completos;
* arquitetura distribuída;
* microservices;
* cloud complexa;
* autenticação de usuários;
* monetização;
* suporte a múltiplos usuários;
* infraestrutura de produção;
* CI/CD avançado;
* dashboards;
* automações sem supervisão;
* escolha prematura de stack definitiva.

Esses itens podem ser reconsiderados quando um projeto demonstrar valor, confiabilidade e maturidade suficientes.
