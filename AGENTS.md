# AGENTS.md

## Repository Purpose

Este repositório é um laboratório de aprendizado para praticar:

* Spec-Driven Development;
* harnesses;
* fixtures;
* testes automatizados;
* agent coding;
* Git;
* automação incremental;
* validação humana de software produzido com auxílio de IA.

O objetivo principal não é maximizar a velocidade de implementação.

O objetivo é construir sistemas pequenos, compreensíveis, testáveis e verificáveis, enquanto desenvolvemos um processo disciplinado de trabalho com agentes.

## Instruction Priority

Ao trabalhar neste repositório, siga esta ordem de prioridade:

1. instruções explícitas da tarefa atual;
2. `AGENTS.md` mais próximo do arquivo sendo alterado;
3. este `AGENTS.md` da raiz;
4. `SPEC.md` do projeto;
5. `HARNESS.md` do projeto;
6. decisões vigentes em `DECISIONS.md`;
7. orientações gerais em `README.md` e `ROADMAP.md`.

Uma instrução específica pode complementar uma instrução geral.

Não ignore uma regra existente sem explicar claramente o conflito.

## Required Reading

Antes de iniciar uma tarefa, leia somente os documentos necessários para compreender corretamente o trabalho.

Para tarefas de implementação dentro de um projeto, leia obrigatoriamente:

* este `AGENTS.md`;
* o `README.md` do projeto;
* o `SPEC.md` aplicável;
* o `HARNESS.md` aplicável;
* os critérios de aceite fornecidos na tarefa;
* arquivos diretamente relacionados à alteração.

Consulte também:

* `DECISIONS.md`, quando a tarefa envolver arquitetura, escopo, dependências, segurança ou convenções;
* `ROADMAP.md`, quando a tarefa puder expandir o escopo da fase atual;
* `PROJECT_IDEAS.md`, apenas quando a tarefa envolver priorização ou comparação de projetos.

Não leia nem modifique arquivos sem relação com a tarefa apenas para ampliar contexto.

## Working Principles

Sempre priorize:

* clareza sobre esperteza;
* soluções pequenas sobre arquiteturas antecipadas;
* comportamento verificável sobre implementação impressionante;
* biblioteca padrão sobre dependências desnecessárias;
* dados sintéticos sobre dados reais;
* mudanças reversíveis sobre grandes reestruturações;
* validação explícita sobre suposições.

Evite:

* overengineering;
* abstrações prematuras;
* expansão silenciosa de escopo;
* refatorações não solicitadas;
* novas ferramentas sem necessidade demonstrada;
* implementação baseada em requisitos implícitos.

## Task Planning

Antes de mudanças substanciais, apresente um plano curto.

Uma mudança é considerada substancial quando envolve um ou mais destes casos:

* múltiplos arquivos;
* nova funcionalidade;
* alteração de comportamento existente;
* nova dependência;
* mudança estrutural;
* refatoração relevante;
* alteração de schema ou contrato de dados;
* mudança no harness;
* decisão arquitetural.

O plano deve informar:

1. o comportamento que será implementado ou alterado;
2. os arquivos que provavelmente serão modificados;
3. como o resultado será validado;
4. riscos ou ambiguidades identificadas.

Para alterações pequenas e mecânicas, como correção de texto ou ajuste isolado, o plano pode ser omitido.

Não use o plano para expandir o escopo solicitado.

## Specification Gate

Não implemente código de produção sem uma especificação mínima válida.

Antes de começar a implementação, confirme que a SPEC define, no mínimo:

* objetivo;
* entrada;
* saída;
* regras de negócio aplicáveis;
* casos inválidos relevantes;
* critérios de aceite;
* escopo negativo;
* comportamento esperado para a tarefa atual.

Escopo negativo descreve aquilo que o projeto deliberadamente não faz.

Se a SPEC estiver incompleta, contraditória ou quebrada:

1. não implemente o comportamento afetado;
2. identifique claramente a lacuna;
3. proponha uma correção na documentação;
4. limite as alterações a Markdown, salvo instrução explícita em contrário;
5. aguarde uma especificação válida antes de implementar.

A validação da SPEC deve acontecer antes do código.

Se uma inconsistência só for descoberta durante a implementação, interrompa a parte afetada. Não escolha silenciosamente uma interpretação e não invente requisitos.

## Harness and Testing Rules

Toda mudança de comportamento deve criar ou atualizar testes.

Antes de implementar, identifique:

* qual cenário comprova o comportamento;
* qual fixture será usada;
* qual saída é esperada;
* como uma falha será apresentada;
* quais casos extremos são relevantes.

O harness deve ser:

* reproduzível;
* fácil de executar;
* independente de dados pessoais reais;
* claro quando falha;
* proporcional ao tamanho do projeto.

Quando adequado, prefira:

* fixtures sintéticas;
* golden tests;
* testes parametrizados;
* contract tests;
* validação de schemas;
* comparação explícita entre saída produzida e saída esperada.

Um golden test compara a saída do sistema com um resultado de referência considerado correto.

Um contract test verifica se dados ou componentes respeitam um formato ou comportamento previamente definido.

Não ajuste um teste apenas para fazê-lo passar quando o comportamento esperado não mudou.

Quando um teste e a SPEC estiverem em conflito, trate isso como uma inconsistência e investigue antes de alterar qualquer um deles.

## Implementation Rules

Implemente somente o menor incremento necessário para atender à tarefa.

Prefira:

* funções pequenas;
* nomes claros;
* fluxo de dados explícito;
* poucas camadas;
* tratamento claro de erros;
* interfaces simples;
* código fácil de testar.

Não adicione funcionalidades futuras como parte da implementação atual.

Não implemente:

* dashboards;
* bancos de dados;
* APIs externas;
* autenticação;
* aplicações móveis;
* automações reais;
* IA generativa;
* infraestrutura de produção;

salvo quando a tarefa e a SPEC solicitarem explicitamente.

Não refatore código fora do escopo apenas porque outra organização parece melhor.

## Scope Boundaries

Modifique somente os arquivos necessários para concluir e validar a tarefa.

Alterações fora dos arquivos originalmente previstos são permitidas quando forem necessárias para:

* adicionar ou atualizar testes;
* criar fixtures;
* corrigir documentação afetada;
* permitir a execução do harness;
* manter contratos de dados consistentes.

Quando alterar arquivos adicionais:

1. explique por que a mudança foi necessária;
2. mantenha a alteração mínima;
3. inclua o arquivo no relatório final;
4. não use a necessidade de teste como justificativa para refatoração ampla.

Não registre automaticamente toda alteração auxiliar em `DECISIONS.md`.

Crie ou proponha um registro de decisão somente quando a mudança:

* altera a arquitetura;
* muda o escopo;
* estabelece uma convenção persistente;
* adiciona uma dependência relevante;
* afeta mais de um projeto;
* modifica um contrato importante;
* cria um trade-off que precisará ser lembrado.

## Dependencies

Evite novas dependências quando a biblioteca padrão ou o código existente resolverem o problema de forma simples.

Antes de adicionar uma dependência, avalie:

* qual problema ela resolve;
* por que a solução existente não é suficiente;
* impacto em instalação e manutenção;
* risco de segurança;
* estabilidade da biblioteca;
* facilidade de remoção futura;
* impacto no harness.

Toda nova dependência deve ser justificada no relatório final.

Dependências que alterem significativamente a arquitetura ou o processo devem ser registradas ou propostas em `DECISIONS.md`.

Não atualize dependências sem relação com a tarefa atual.

## External Integrations

O núcleo local deve existir antes de qualquer integração externa.

Não adicione automaticamente:

* chamadas de rede;
* APIs;
* scraping;
* autenticação;
* notificações;
* serviços de cloud;
* bancos de dados remotos;
* integrações com calendários, e-mails ou contatos.

Quando uma integração externa for explicitamente solicitada:

* mantenha a lógica central separada da integração;
* crie mocks ou fixtures;
* documente o contrato esperado;
* trate erros e indisponibilidade;
* não use a integração real como único método de teste.

Mock é uma substituição controlada de uma dependência externa usada para testar o sistema de forma previsível.

## Privacy and Security

Use dados sintéticos como padrão.

Não adicione ao repositório:

* CPF;
* endereço real;
* telefone real;
* e-mail pessoal;
* chave de acesso fiscal;
* notas fiscais reais;
* históricos financeiros reais;
* listas reais de contatos;
* aniversários reais;
* informações médicas reais;
* tokens;
* senhas;
* API keys;
* secrets;
* cookies ou sessões.

Não copie dados sensíveis para:

* fixtures;
* testes;
* exemplos;
* documentação;
* logs;
* prompts;
* mensagens de erro.

Quando o formato real precisar ser representado, crie dados sintéticos estruturalmente equivalentes.

Não presuma que um arquivo é seguro apenas porque está listado no `.gitignore`.

Se dados sensíveis forem encontrados, não os reproduza. Informe o problema e limite qualquer exposição adicional.

## Language and Naming

Use português para:

* documentação explicativa;
* contexto;
* decisões;
* especificações;
* descrições de regras;
* relatórios de trabalho.

Use inglês para:

* código;
* variáveis;
* funções;
* classes;
* schemas;
* campos de dados;
* nomes técnicos de arquivos e pastas;
* mensagens internas de validação, quando apropriado.

Nomes de domínio brasileiros podem permanecer em português quando uma tradução reduzir a clareza.

Exemplo aceito:

```text
nota-fiscal-insight
```

Mantenha consistência dentro de cada arquivo e componente.

## Git and Change Management

Não crie commits, branches, tags ou pull requests sem instrução explícita.

O usuário é inicialmente responsável por revisar e commitar as alterações.

Antes de concluir uma tarefa:

* revise o diff;
* confirme que somente arquivos necessários foram alterados;
* remova mudanças acidentais;
* não inclua arquivos gerados desnecessários;
* verifique se dados sensíveis não foram adicionados;
* sugira uma mensagem de commit quando isso for útil.

Não use comandos destrutivos de Git.

Não execute:

```text
git reset --hard
git clean -fd
git push --force
```

salvo instrução explícita e contexto seguro.

Não reverta alterações existentes que não foram produzidas na tarefa atual.

## Validation

Antes de declarar uma tarefa concluída, execute os testes e comandos de validação relevantes.

Use, nesta ordem:

1. testes diretamente relacionados à mudança;
2. harness do projeto;
3. suíte completa, quando disponível e proporcional;
4. validações estáticas relevantes;
5. execução manual mínima, quando necessária.

Se algum comando falhar:

* investigue a causa;
* corrija problemas dentro do escopo;
* execute novamente;
* relate falhas restantes.

Se não for possível executar um teste ou validação:

* diga explicitamente que não foi executado;
* explique o motivo;
* forneça o comando que deveria ser usado;
* não afirme que o comportamento funciona;
* diferencie claramente “implementado” de “validado”.

Não esconda warnings, erros ou testes ignorados.

## Completion Criteria

Uma tarefa só pode ser considerada concluída quando:

* a SPEC aplicável foi respeitada;
* os critérios de aceite foram atendidos;
* os testes necessários foram criados ou atualizados;
* as validações disponíveis foram executadas;
* o escopo não foi ampliado silenciosamente;
* arquivos alterados foram revisados;
* limitações conhecidas foram documentadas;
* nenhum dado sensível foi introduzido.

Código compilando não é evidência suficiente de conclusão.

Um teste passando também não é suficiente quando o teste não representa o comportamento especificado.

## Completion Report

Ao finalizar uma tarefa, apresente um relatório curto contendo:

### Summary

O que foi implementado ou alterado.

### Files changed

Lista dos arquivos modificados e a finalidade de cada alteração.

### Validation

Comandos executados e seus resultados.

Exemplo:

```text
pytest tests/test_receipt_parser.py
Result: 8 passed
```

### Decisions and trade-offs

Decisões relevantes tomadas durante a tarefa.

Quando aplicável, indicar:

* registro adicionado em `DECISIONS.md`;
* registro recomendado, mas ainda não criado;
* nenhuma decisão persistente necessária.

### Limitations

Comportamentos ainda não suportados, riscos ou pontos que precisam de revisão.

### Suggested next step

No máximo um próximo incremento pequeno e verificável.

Não declare trabalho futuro como se já tivesse sido realizado.

## Prohibited Actions

Sem instrução explícita, não:

* implemente o projeto inteiro;
* altere o roadmap;
* mude prioridades;
* amplie o escopo da fase;
* use dados reais;
* adicione integrações externas;
* introduza IA generativa;
* escolha uma stack complexa;
* crie infraestrutura de produção;
* faça deploy;
* envie mensagens ou notificações;
* altere calendários, e-mails ou dados externos;
* crie commits;
* remova arquivos existentes;
* execute comandos destrutivos;
* substitua decisões humanas em domínios sensíveis.

Quando uma tarefa exigir uma dessas ações, explique o impacto e siga apenas o escopo explicitamente autorizado.
