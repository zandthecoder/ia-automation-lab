# Decisions

Este arquivo registra decisões importantes do IA Automation Lab.

O objetivo não é documentar cada alteração feita no repositório, mas preservar o contexto das escolhas que afetam o modo de trabalho, o escopo dos projetos, a arquitetura, os testes, o uso de agentes e a segurança.

Cada decisão deve responder:

* qual era o contexto;
* o que foi decidido;
* quais alternativas foram consideradas;
* quais benefícios e custos foram aceitos;
* em que situação a decisão deve ser reconsiderada.

## Status

Os registros podem usar os seguintes status:

* `proposed`: decisão ainda em discussão;
* `accepted`: decisão vigente;
* `rejected`: alternativa considerada, mas não adotada;
* `superseded`: decisão substituída por uma decisão mais recente.

Quando uma decisão mudar, o registro original não deve ser apagado. Ele deve ser marcado como `superseded` e apontar para a decisão que o substituiu.

## Scope

O campo `Scope` indica onde a decisão se aplica.

Exemplos:

```text
lab
nota-fiscal-insight
salad-jar-generator
reading-companion
```

Decisões com escopo `lab` valem para todo o repositório, salvo quando uma decisão posterior e mais específica estabelecer uma exceção.

## Decision Log

## DEC-001 — Usar um único repositório para o laboratório

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

O laboratório terá vários projetos pequenos voltados ao aprendizado de Spec-Driven Development, harnesses, testes, agent coding e automação.

Era necessário decidir se cada ideia teria um repositório separado desde o início ou se todos os projetos ficariam organizados em um único repositório.

### Decision

Usar um único repositório para o IA Automation Lab.

Os projetos individuais ficam dentro da pasta:

```text
projects/
```

Documentos e templates compartilhados ficam na raiz e em:

```text
templates/
```

### Alternatives considered

1. Criar um repositório separado para cada projeto.
2. Manter apenas arquivos soltos, sem estrutura comum.
3. Usar uma ferramenta de notas como fonte principal do laboratório.

### Consequences

Benefícios:

* facilita reutilizar templates;
* mantém o roadmap e o backlog em um único lugar;
* permite comparar a evolução entre projetos;
* reduz a quantidade de configuração inicial;
* facilita fornecer contexto comum ao ChatGPT e ao Codex;
* mantém o histórico de aprendizado centralizado.

Custos e trade-offs:

* o repositório pode ficar grande com o tempo;
* decisões específicas podem se misturar com decisões globais;
* projetos maduros podem futuramente precisar de repositórios próprios.

### Revisit when

Reconsiderar esta decisão quando:

* um projeto precisar de ciclo de release independente;
* um projeto virar produto público;
* o repositório ficar difícil de navegar;
* as dependências dos projetos começarem a entrar em conflito;
* um projeto exigir controles de acesso diferentes.

---

## DEC-002 — Manter apenas um projeto ativo por vez

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

Existem várias ideias de projeto interessantes, mas o objetivo principal do laboratório é desenvolver um processo disciplinado de construção com IA.

Trabalhar em vários projetos ao mesmo tempo pode dificultar a conclusão de ciclos completos de especificação, implementação, validação e retrospectiva.

### Decision

Manter apenas um projeto com status `now`.

Novas ideias podem ser registradas em `PROJECT_IDEAS.md`, mas sua implementação deve aguardar até que o projeto ativo alcance o critério mínimo de conclusão definido no `ROADMAP.md`.

### Alternatives considered

1. Trabalhar em vários projetos em paralelo.
2. Alternar livremente entre projetos conforme a motivação.
3. Limitar o trabalho a dois projetos simultâneos.

### Consequences

Benefícios:

* reduz dispersão;
* aumenta a chance de concluir ciclos completos;
* facilita identificar o que foi realmente aprendido;
* melhora a qualidade das retrospectivas;
* evita acumular vários protótipos incompletos.

Custos e trade-offs:

* ideias novas podem precisar esperar;
* pode haver queda de motivação se o projeto ativo entrar em uma fase difícil;
* oportunidades de experimentar outro domínio ficam temporariamente limitadas.

Ideias novas ainda podem ser discutidas, avaliadas e documentadas, desde que isso não inicie uma segunda implementação ativa.

### Revisit when

Reconsiderar esta decisão quando:

* houver experiência suficiente para conduzir mais de um ciclo com disciplina;
* um projeto estiver bloqueado por uma dependência externa;
* existir uma distinção clara entre projeto ativo e pequena experiência isolada;
* o processo de acompanhamento estiver maduro o suficiente para evitar dispersão.

---

## DEC-003 — Usar um roadmap sem datas baseado em `now`, `then` e `later`

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

O laboratório é um ambiente de estudo e não um projeto comercial com prazo externo.

Um cronograma baseado em datas poderia incentivar avanço artificial, mesmo sem evidências de que os conceitos e práticas da fase foram compreendidos.

### Decision

Usar um roadmap organizado com a terminologia:

* `now`: foco ativo;
* `then`: próximo projeto planejado;
* `later`: projetos futuros.

A passagem entre fases depende de critérios de conclusão e evidências de aprendizado, não de datas predefinidas.

### Alternatives considered

1. Definir datas e prazos para cada projeto.
2. Usar sprints semanais ou quinzenais.
3. Manter apenas uma lista ordenada sem estados.
4. Usar `current`, `next` e `later`.

### Consequences

Benefícios:

* favorece aprendizado real em vez de cumprimento de calendário;
* permite ajustar o ritmo;
* mantém clara a prioridade atual;
* reduz pressão para implementar antes de especificar e testar.

Custos e trade-offs:

* pode haver tendência a prolongar uma fase excessivamente;
* não existe compromisso temporal explícito;
* será necessário revisar periodicamente se o escopo ainda está adequado.

### Revisit when

Reconsiderar esta decisão quando:

* o laboratório passar a ter compromissos externos;
* algum projeto precisar de uma data de entrega;
* a ausência de datas estiver causando falta de progresso;
* houver necessidade de combinar fases com uma rotina de estudos estruturada.

---

## DEC-004 — Construir o núcleo local antes de integrações externas

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

Vários projetos considerados dependem potencialmente de APIs, sites externos, notificações, aplicativos móveis, autenticação ou automações com efeitos reais.

Essas dependências aumentam a complexidade e podem esconder problemas no comportamento central do sistema.

### Decision

Todo projeto deve começar com um núcleo local, pequeno e testável.

A primeira versão deve priorizar:

* arquivos locais;
* dados sintéticos;
* execução manual;
* entrada e saída explícitas;
* testes reproduzíveis;
* poucas dependências.

Integrações externas só devem ser consideradas depois que o núcleo local tiver SPEC, harness, testes e limitações documentadas.

### Alternatives considered

1. Começar diretamente pela integração que motivou o projeto.
2. Construir primeiro uma interface visual.
3. Criar desde o início uma aplicação completa.
4. Usar serviços externos como parte obrigatória do harness.

### Consequences

Benefícios:

* reduz complexidade inicial;
* permite testar o comportamento sem depender da rede;
* facilita criar fixtures;
* torna falhas mais fáceis de reproduzir;
* reduz custos e riscos;
* permite substituir integrações externas futuramente.

Custos e trade-offs:

* a primeira versão pode parecer menos impressionante;
* certas suposições sobre integrações reais só serão descobertas depois;
* algum trabalho local poderá precisar ser adaptado ao formato real.

### Revisit when

Esta decisão não precisa ser removida quando uma integração for adicionada.

Deve ser reconsiderada para um projeto específico quando:

* a integração for parte inseparável do comportamento que está sendo estudado;
* não existir uma forma útil de simular a fonte externa;
* o núcleo local já estiver validado;
* houver um harness de contrato para a integração.

---

## DEC-005 — Usar dados sintéticos como padrão

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

Alguns projetos envolvem informações potencialmente sensíveis, incluindo:

* notas fiscais;
* gastos;
* contatos;
* aniversários;
* histórico de leitura;
* dados de saúde;
* e-mails e calendários.

O uso de dados reais em fixtures, commits ou prompts para agentes aumenta riscos de privacidade e exposição acidental.

### Decision

Usar dados sintéticos como padrão em:

* fixtures;
* testes;
* exemplos de documentação;
* prompts para agentes;
* arquivos versionados;
* demonstrações iniciais.

Dados reais só podem ser usados quando forem necessários para validação e depois de serem anonimizados.

Dados reais não devem ser commitados no repositório.

### Alternatives considered

1. Usar dados reais desde o início.
2. Armazenar dados reais em uma pasta privada do repositório.
3. Usar dados reais e depender apenas do `.gitignore`.
4. Criar fixtures copiando parcialmente documentos reais.

### Consequences

Benefícios:

* reduz risco de exposição;
* facilita compartilhar projetos futuramente;
* torna os testes mais controlados;
* permite representar casos extremos deliberadamente;
* evita que agentes recebam informações pessoais desnecessárias.

Custos e trade-offs:

* fixtures sintéticas podem não representar todas as irregularidades do mundo real;
* problemas de formato podem aparecer apenas na validação com exemplos reais;
* será necessário investir algum tempo criando dados sintéticos representativos.

### Revisit when

A decisão continua válida como padrão.

O uso controlado de dados reais pode ser considerado quando:

* o harness já estiver funcionando;
* a validação não puder ser feita adequadamente apenas com dados sintéticos;
* o dado tiver sido anonimizado;
* o arquivo estiver fora do versionamento;
* os riscos estiverem documentados;
* a análise puder ser feita localmente.

---

## DEC-006 — Escrever documentação em português e código em inglês

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

A documentação precisa ser confortável para estudo, reflexão e tomada de decisão.

Ao mesmo tempo, código e nomes técnicos em inglês facilitam o uso de bibliotecas, ferramentas, agentes de programação e convenções comuns da indústria.

### Decision

Usar:

* português na documentação explicativa;
* inglês no código;
* inglês em nomes de funções e variáveis;
* inglês em nomes técnicos de pastas e arquivos;
* inglês em schemas e campos de dados;
* termos técnicos em inglês quando forem o padrão do ecossistema.

Nomes ligados diretamente ao domínio brasileiro podem permanecer em português quando a tradução reduzir a clareza.

Exemplo:

```text
nota-fiscal-insight
```

### Alternatives considered

1. Usar português em todo o repositório.
2. Usar inglês em toda a documentação.
3. Misturar idiomas livremente sem uma convenção explícita.

### Consequences

Benefícios:

* torna a documentação mais acessível para o estudo;
* aproxima o código das convenções das ferramentas;
* facilita trabalhar com agentes;
* reduz traduções artificiais de termos técnicos;
* prepara os projetos para eventual compartilhamento.

Custos e trade-offs:

* alguns arquivos terão conteúdo em português e identificadores em inglês;
* será necessário manter consistência;
* certos termos podem exigir explicação na primeira vez em que forem usados.

### Revisit when

Reconsiderar esta decisão quando:

* um projeto passar a ter colaboradores internacionais;
* um projeto virar produto público com documentação em inglês;
* houver necessidade de internacionalizar a documentação;
* a mistura de idiomas estiver causando ambiguidade.

---

## DEC-007 — Usar agentes em tarefas pequenas, verificáveis e revisadas

**Date:** 2026-07-12
**Status:** accepted
**Scope:** lab

### Context

O laboratório existe para aprender agent coding, mas delegar tarefas amplas pode produzir alterações difíceis de entender, revisar e validar.

O objetivo não é apenas obter código funcionando. É aprender a orientar agentes e verificar o trabalho produzido.

### Decision

Agentes, incluindo Codex, devem receber tarefas pequenas e delimitadas.

Cada tarefa deve incluir, sempre que aplicável:

* contexto;
* objetivo;
* arquivos relevantes;
* restrições;
* critérios de aceite;
* testes ou forma de validação;
* ações que não devem ser executadas.

Toda alteração relevante deve passar por revisão humana.

O agente não deve ser instruído a “criar o app inteiro” ou tomar decisões de produto sem orientação.

### Alternatives considered

1. Permitir que o agente defina arquitetura e implementação livremente.
2. Pedir projetos completos em um único prompt.
3. Usar o agente apenas para gerar exemplos, sem alterar arquivos.
4. Usar agentes somente depois que toda a arquitetura estiver definida manualmente.

### Consequences

Benefícios:

* mudanças ficam mais fáceis de revisar;
* erros são mais fáceis de localizar;
* testes podem validar cada incremento;
* prompts podem ser avaliados e melhorados;
* reduz o risco de o agente expandir o escopo;
* aumenta o aprendizado sobre delegação técnica.

Custos e trade-offs:

* exige mais preparação antes de pedir implementação;
* o processo pode parecer mais lento;
* tarefas grandes precisam ser divididas;
* a pessoa precisa entender o suficiente para revisar o resultado.

### Revisit when

Reconsiderar o nível de autonomia quando:

* o projeto tiver harnesses maduros;
* a suíte de testes oferecer boa proteção;
* as tarefas forem repetitivas e bem compreendidas;
* o agente demonstrar comportamento confiável naquele repositório;
* existir um processo seguro para revisar e reverter alterações.

Mesmo com maior autonomia, a validação humana continua obrigatória para dados sensíveis e automações com efeitos reais.

## Project Retrospectives

Esta seção registra retrospectivas de fases e projetos.

Uma retrospectiva não precisa representar uma única decisão. Ela serve para analisar o ciclo de trabalho e identificar melhorias para os próximos projetos.

## Retrospective Template

```markdown
## RETRO-XXX — Project or phase name

**Date:** YYYY-MM-DD
**Scope:** project-name
**Outcome:** completed | continued | paused

### Goal

Qual era o objetivo didático e técnico desta fase?

### What worked

- O que funcionou bem?
- Quais práticas ajudaram?
- Quais testes foram úteis?
- Onde o agente agregou valor?

### What did not work

- Onde houve dificuldade?
- Quais instruções estavam vagas?
- Onde o agente errou?
- Quais mudanças geraram retrabalho?

### Harness findings

- O harness detectou problemas reais?
- Quais cenários estavam faltando?
- As falhas eram fáceis de entender?
- Os testes estavam acoplados demais à implementação?

### Agent coding findings

- As tarefas estavam pequenas o suficiente?
- Os critérios de aceite estavam claros?
- O agente alterou algo fora do escopo?
- Quais prompts funcionaram melhor?

### Git findings

- Os commits estavam pequenos?
- Foi fácil revisar as diferenças?
- Alguma mudança precisou ser revertida?
- O histórico explica a evolução?

### Decisions

Quais decisões foram tomadas como resultado desta retrospectiva?

Referenciar novos registros quando necessário:

- DEC-XXX
- DEC-YYY

### Template changes

Quais templates ou instruções devem ser atualizados?

### Skills to reinforce

Quais conceitos ou habilidades precisam de mais prática?

### Next step

Qual é a próxima ação recomendada?
```

## Primeira retrospectiva planejada

A primeira retrospectiva será registrada depois da conclusão da primeira versão de:

```text
projects/nota-fiscal-insight
```

Ela deve avaliar, no mínimo:

* qualidade da SPEC;
* utilidade do HARNESS;
* representatividade das fixtures;
* experiência com Git;
* qualidade das tarefas dadas ao Codex;
* facilidade de revisar código gerado;
* limitações encontradas no parser;
* mudanças necessárias nos templates.
