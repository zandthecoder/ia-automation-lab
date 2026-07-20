# Project Ideas

Este arquivo registra e compara ideias de projetos para o IA Automation Lab.

O objetivo não é apenas guardar uma lista de ideias, mas ajudar a decidir quais projetos fazem sentido para praticar Spec-Driven Development, harnesses, agent coding, automação e construção incremental de software.

## Objetivo deste arquivo

Este backlog serve para:

* registrar ideias de projetos;
* comparar valor didático e utilidade prática;
* escolher a próxima implementação;
* evitar começar projetos grandes demais;
* identificar riscos técnicos e de privacidade;
* definir o menor primeiro passo de cada ideia;
* manter uma sequência de aprendizado coerente.

A regra geral é: cada projeto deve começar como um protótipo local, pequeno, testável e com entradas e saídas claras.

## Critérios de avaliação

Cada ideia deve ser avaliada pelos critérios abaixo.

### Valor didático

Quanto o projeto ajuda a aprender conceitos importantes como especificação, fixtures, harnesses, testes, parsing, automação, agentes e validação.

Escala: `Baixo`, `Médio`, `Alto`.

### Utilidade pessoal

Quanto o projeto resolve um problema real do autor do laboratório.

Escala: `Baixo`, `Médio`, `Alto`.

### Clareza de entrada e saída

Quão fácil é definir o que entra no sistema e o que deve sair dele.

Escala: `Baixo`, `Médio`, `Alto`.

### Facilidade de criar harness

Quão fácil é criar um conjunto de exemplos, fixtures e validações automatizadas para confirmar que o sistema está funcionando.

Harness, neste contexto, significa um pequeno ambiente de teste que executa o sistema com entradas conhecidas e compara o resultado com saídas esperadas.

Escala: `Baixo`, `Médio`, `Alto`.

### Risco técnico

Quão complexo ou incerto é implementar o projeto.

Escala: `Baixo`, `Médio`, `Alto`.

### Risco de privacidade e segurança

Quanto o projeto envolve dados sensíveis, efeitos reais, informações pessoais ou decisões que exigem validação humana.

Escala: `Baixo`, `Médio`, `Alto`.

### Dependência de integrações externas

Quanto o projeto depende de APIs, serviços externos, autenticação, scraping, apps móveis ou dados difíceis de obter.

Escala: `Baixo`, `Médio`, `Alto`.

### Potencial de virar produto

Quanto o projeto poderia evoluir para algo utilizável por outras pessoas, desde que ainda seja viável para uma única pessoa desenvolver com auxílio de IA.

Escala: `Baixo`, `Médio`, `Alto`.

## Ranking atual

| Ordem | Projeto               | Status      | Motivo                                                                                         |
| ----: | --------------------- | ----------- | ---------------------------------------------------------------------------------------------- |
|     1 | `nota-fiscal-insight` | `active`    | Melhor combinação de utilidade pessoal, dados reais estruturáveis, parser, fixtures e harness. |
|     2 | `salad-jar-generator` | `candidate` | Bom para praticar regras de negócio, geração de combinações e validação simples.               |
|     3 | `reading-companion`   | `candidate` | Ótimo para trabalhar com CSV, catálogos locais, matching e relatórios úteis.                   |
|     4 | `birthday-aggregator` | `later`     | Interessante, mas envolve privacidade, deduplicação e integrações mais chatas.                 |
|     5 | `medication-manager`  | `later`     | Valioso, mas envolve saúde e exige cuidado extra com segurança e validação humana.             |

## Ideias em detalhe

## 1. `nota-fiscal-insight`

**Status:** `active`
**Prioridade:** 1

### Resumo

Extrair e estruturar dados de notas fiscais, começando com exemplos sintéticos de NFC-e/nota fiscal paulista, para futuramente analisar gastos por mercado, padaria, categoria de produto e recorrência de compra.

### Por que vale fazer

Este é o melhor primeiro projeto porque tem um domínio real, entrada relativamente concreta e potencial de gerar valor pessoal rapidamente.

O projeto pode começar pequeno, apenas transformando uma nota fiscal de exemplo em um JSON estruturado. Depois pode evoluir para categorização, análise de gastos, comparação entre estabelecimentos e relatórios.

### O que vou aprender

* Parsing de dados semi-estruturados.
* Modelagem de entrada e saída.
* Criação de fixtures sintéticas.
* Harnesses de validação.
* Testes de regressão.
* Normalização de nomes de produtos.
* Categorização incremental.
* Cuidados com dados sensíveis.

### Avaliação

| Critério                            | Avaliação       |
| ----------------------------------- | --------------- |
| Valor didático                      | Alto            |
| Utilidade pessoal                   | Alto            |
| Clareza de entrada e saída          | Alto            |
| Facilidade de criar harness         | Alto            |
| Risco técnico                       | Médio           |
| Risco de privacidade e segurança    | Médio           |
| Dependência de integrações externas | Baixo no início |
| Potencial de virar produto          | Médio           |

### Menor primeiro passo

Criar uma fixture sintética representando uma nota fiscal simples e gerar uma saída JSON com:

* estabelecimento;
* data da compra;
* lista de itens;
* quantidade;
* preço unitário;
* preço total;
* valor total da nota.

### Harness mínimo

Executar um comando local com uma fixture de entrada e comparar a saída gerada com um arquivo JSON esperado.

Exemplo conceitual:

```text
input: fixtures/sample_receipt_01.txt
output esperado: fixtures/expected/sample_receipt_01.json
```

O harness deve falhar se algum campo essencial estiver ausente ou incorreto.

### Partes mockadas

* Consulta real via QR Code.
* Download automático da nota.
* Integração com sites do governo.
* Categorização automática por IA.
* Dashboard.
* Banco de dados.
* Dados reais.

### Riscos

* Notas fiscais reais podem conter dados sensíveis.
* Diferentes estabelecimentos podem gerar formatos variados.
* QR Codes podem depender de páginas externas instáveis.
* Categorização de produtos pode ser ambígua.

### Critério de pronto da primeira versão

A primeira versão estará pronta quando:

* existir uma SPEC mínima;
* existir uma fixture sintética;
* existir uma saída JSON esperada;
* o harness conseguir validar a saída;
* o parser funcionar para pelo menos um exemplo sintético;
* nenhum dado pessoal real estiver versionado.

### Próximo passo

Preencher `projects/nota-fiscal-insight/SPEC.md` e `projects/nota-fiscal-insight/HARNESS.md`.

---

## 2. `salad-jar-generator`

**Status:** `candidate`
**Prioridade:** 2

### Resumo

Gerar combinações de saladas de pote a partir de ingredientes, preferências, restrições e regras simples de montagem, começando como um gerador local com entrada e saída explícitas.

### Por que vale fazer

Este projeto é bom para praticar regras de negócio sem depender de dados sensíveis ou integrações externas.

Ele permite trabalhar com restrições, combinações, preferências, validação e talvez geração assistida por IA em uma etapa posterior.

### O que vou aprender

* Modelagem de regras de negócio.
* Validação de combinações.
* Separação entre dados, regras e geração.
* Testes com casos extremos.
* Uso de fixtures para ingredientes e preferências.
* Evolução de script simples para produto mais útil.

### Avaliação

| Critério                            | Avaliação |
| ----------------------------------- | --------- |
| Valor didático                      | Alto      |
| Utilidade pessoal                   | Médio     |
| Clareza de entrada e saída          | Alto      |
| Facilidade de criar harness         | Alto      |
| Risco técnico                       | Baixo     |
| Risco de privacidade e segurança    | Baixo     |
| Dependência de integrações externas | Baixo     |
| Potencial de virar produto          | Médio     |

### Menor primeiro passo

Dado um arquivo com ingredientes disponíveis e regras simples, gerar três sugestões válidas de salada de pote.

A saída pode conter:

* nome da salada;
* lista de ingredientes;
* ordem de montagem;
* observações;
* motivo da combinação.

### Harness mínimo

Criar fixtures com ingredientes e regras.

Validar que:

* uma salada não contém ingredientes proibidos;
* uma salada respeita a ordem de montagem;
* uma salada tem pelo menos uma base, uma proteína, vegetais e molho;
* o sistema retorna erro claro quando não há combinação possível.

### Partes mockadas

* Banco de dados de alimentos.
* Informações nutricionais reais.
* Cálculo calórico.
* Integração com mercado.
* Planejamento semanal avançado.
* Interface visual.

### Riscos

* Projeto pode parecer simples demais se não houver boas regras.
* Pode crescer demais se tentar incluir nutrição completa no início.
* Preferências alimentares podem tornar a lógica mais complexa.

### Critério de pronto da primeira versão

A primeira versão estará pronta quando:

* uma lista pequena de ingredientes gerar combinações válidas;
* as regras principais forem testadas;
* os casos de erro forem claros;
* a saída for previsível o suficiente para ser validada por harness.

### Próximo passo

Só iniciar depois que `nota-fiscal-insight` tiver uma primeira versão local funcionando.

---

## 3. `reading-companion`

**Status:** `candidate`
**Prioridade:** 3

### Resumo

Analisar uma lista exportada do Goodreads para identificar séries de livros em andamento, último livro lido, próximo livro recomendado e possíveis lançamentos futuros, começando com CSV exportado manualmente e catálogo de séries local.

### Por que vale fazer

Este projeto tem alto valor didático porque combina dados pessoais exportados, normalização, catálogos, matching e geração de relatórios úteis.

A versão inicial pode funcionar totalmente local, sem depender de API do Goodreads ou notificações externas.

### O que vou aprender

* Parsing de CSV.
* Normalização de títulos e autores.
* Modelagem de séries de livros.
* Matching entre livros lidos e catálogo local.
* Relatórios derivados de dados.
* Separação entre dados importados e dados mantidos manualmente.
* Evolução futura para notificações ou atualizações externas.

### Avaliação

| Critério                            | Avaliação       |
| ----------------------------------- | --------------- |
| Valor didático                      | Alto            |
| Utilidade pessoal                   | Alto            |
| Clareza de entrada e saída          | Médio           |
| Facilidade de criar harness         | Alto            |
| Risco técnico                       | Médio           |
| Risco de privacidade e segurança    | Médio           |
| Dependência de integrações externas | Baixo no início |
| Potencial de virar produto          | Médio           |

### Menor primeiro passo

Dado um CSV exportado manualmente do Goodreads e um catálogo local de séries, gerar um relatório mostrando:

* séries identificadas;
* último livro lido em cada série;
* próximo livro da série;
* status da série: não iniciada, em andamento ou completa.

### Harness mínimo

Criar um CSV sintético com poucos livros e um catálogo local pequeno.

Validar que:

* o sistema identifica corretamente o último livro lido;
* o sistema sugere o próximo livro;
* séries completas são marcadas como completas;
* livros fora do catálogo são ignorados ou reportados claramente.

### Partes mockadas

* API do Goodreads.
* Consulta automática a lançamentos.
* Scraping de sites de livros.
* Notificações.
* Resumos gerados por IA.
* Integração com Kindle, StoryGraph ou outros serviços.

### Riscos

* Títulos de livros podem variar entre edições.
* Séries podem ter ordem de publicação, ordem cronológica ou sub-séries.
* Dados exportados podem estar incompletos.
* Resumos de livros podem envolver direitos autorais e devem ser tratados com cuidado.

### Critério de pronto da primeira versão

A primeira versão estará pronta quando:

* um CSV sintético puder ser lido;
* um catálogo local puder ser comparado;
* o relatório indicar corretamente o progresso em pelo menos duas séries;
* o comportamento estiver coberto por fixtures e harness.

### Próximo passo

Criar uma SPEC específica depois da primeira rodada com `nota-fiscal-insight` ou `salad-jar-generator`.

---

## 4. `birthday-aggregator`

**Status:** `later`
**Prioridade:** 4

### Resumo

Agregar aniversários a partir de fontes locais como CSV, planilhas e contatos exportados, deduplicar pessoas, priorizar quais aniversários acompanhar e futuramente alimentar um widget ou calendário.

### Por que vale fazer

A ideia tem utilidade pessoal clara, mas é mais complexa do que parece.

O núcleo local é interessante para aprendizado: importar dados, normalizar nomes, deduplicar pessoas e gerar uma lista de próximos aniversários.

A parte de widget no iOS, integração com Facebook, Outlook ou calendário deve ficar para fases posteriores.

### O que vou aprender

* Normalização de nomes.
* Deduplicação de registros.
* Regras de merge manual.
* Priorização de fontes.
* Geração de listas ordenadas por data.
* Exportação para formatos como JSON ou `.ics`.
* Cuidados com dados pessoais.

### Avaliação

| Critério                            | Avaliação                |
| ----------------------------------- | ------------------------ |
| Valor didático                      | Médio                    |
| Utilidade pessoal                   | Alto                     |
| Clareza de entrada e saída          | Médio                    |
| Facilidade de criar harness         | Médio                    |
| Risco técnico                       | Médio                    |
| Risco de privacidade e segurança    | Alto                     |
| Dependência de integrações externas | Alto se começar por APIs |
| Potencial de virar produto          | Baixo a Médio            |

### Menor primeiro passo

Criar três arquivos locais sintéticos representando fontes diferentes de aniversários e gerar uma lista unificada.

A saída deve conter:

* nome normalizado;
* data de aniversário;
* fontes onde a pessoa apareceu;
* nível de confiança;
* indicação se deve aparecer na lista principal.

### Harness mínimo

Criar fixtures com duplicatas e variações de nome.

Validar que:

* duplicatas óbvias são unificadas;
* duplicatas incertas são marcadas para revisão manual;
* aniversários sem ano são aceitos;
* a lista da semana é calculada corretamente.

### Partes mockadas

* Facebook.
* Outlook/Hotmail.
* Skype.
* iCloud.
* Widget iOS.
* Notificações.
* Dashboard.
* Sincronização automática.

### Riscos

* Dados de aniversário são dados pessoais.
* Deduplicação automática pode juntar pessoas erradas.
* Integrações externas podem ser limitadas ou instáveis.
* Widget iOS adiciona complexidade de plataforma.

### Critério de pronto da primeira versão

A primeira versão estará pronta quando:

* arquivos locais sintéticos forem agregados;
* a lista de aniversários da semana for gerada;
* duplicatas óbvias forem tratadas;
* casos ambíguos forem sinalizados para revisão manual;
* nenhum dado real estiver versionado.

### Próximo passo

Manter como ideia futura. Quando for iniciado, começar pelo agregador local, não pelo widget.

---

## 5. `medication-manager`

**Status:** `later`
**Prioridade:** 5

### Resumo

Criar um sistema pessoal de apoio ao gerenciamento de medicamentos, começando como protótipo local sem automações reais, com foco em organização, lembretes simulados e validação humana.

### Por que vale fazer

Este projeto pode ter alta utilidade pessoal, mas também tem risco elevado porque envolve saúde.

Ele só deve ser atacado depois de alguma prática com projetos menores, harnesses e validação. O sistema não deve tomar decisões médicas, alterar prescrições ou automatizar ações sem revisão humana.

### O que vou aprender

* Modelagem de dados sensíveis.
* Regras de agendamento.
* Simulação de lembretes.
* Validação de conflitos.
* Testes de casos extremos.
* Segurança e privacidade.
* Limites de automação em contexto de saúde.

### Avaliação

| Critério                            | Avaliação                                                          |
| ----------------------------------- | ------------------------------------------------------------------ |
| Valor didático                      | Alto                                                               |
| Utilidade pessoal                   | Alto                                                               |
| Clareza de entrada e saída          | Médio                                                              |
| Facilidade de criar harness         | Médio                                                              |
| Risco técnico                       | Médio                                                              |
| Risco de privacidade e segurança    | Alto                                                               |
| Dependência de integrações externas | Baixo no início                                                    |
| Potencial de virar produto          | Baixo para uma pessoa só, por risco regulatório e responsabilidade |

### Menor primeiro passo

Criar um protótipo local que receba uma lista sintética de medicamentos e horários e gere uma agenda diária simulada.

A saída pode conter:

* medicamento;
* dose textual;
* horário;
* instruções;
* status simulado;
* alertas básicos de inconsistência.

### Harness mínimo

Criar fixtures sintéticas com horários e regras simples.

Validar que:

* lembretes são gerados na ordem correta;
* medicamentos pausados não aparecem;
* horários duplicados são agrupados;
* inconsistências são marcadas para revisão;
* nenhuma recomendação médica é criada automaticamente.

### Partes mockadas

* Notificações reais.
* Integração com calendário.
* Dados reais de medicamentos.
* Interações medicamentosas.
* Prescrições.
* Comunicação com médicos ou farmácias.

### Riscos

* Erros podem afetar saúde se o sistema for usado sem validação.
* Dados são altamente sensíveis.
* Pode haver falsa confiança em automações.
* Escopo pode crescer rápido demais.

### Critério de pronto da primeira versão

A primeira versão estará pronta quando:

* o sistema funcionar apenas com dados sintéticos;
* uma agenda simulada for gerada;
* regras simples forem testadas;
* o README deixar claro que não há recomendação médica;
* nenhuma automação real for ativada.

### Próximo passo

Deixar para depois. Só iniciar quando o laboratório já tiver maturidade em specs, harnesses e validação.

## Ideias pausadas ou descartadas

Nenhum projeto descartado ainda.

Esta seção deve ser usada para registrar ideias que foram abandonadas, pausadas ou reduzidas de escopo, junto com o motivo.

Exemplo de registro futuro:

```text
## nome-da-ideia

Status: paused

Motivo:
A ideia depende de integração externa instável e não oferece um bom harness inicial.

Possível retomada:
Reavaliar se surgir uma versão local menor.
```

## Como adicionar uma nova ideia

Ao adicionar uma nova ideia, preencher:

```text
## nome-do-projeto

Status:
Prioridade:

### Resumo

### Por que vale fazer

### O que vou aprender

### Avaliação

| Critério | Avaliação |
|---|---|
| Valor didático |  |
| Utilidade pessoal |  |
| Clareza de entrada e saída |  |
| Facilidade de criar harness |  |
| Risco técnico |  |
| Risco de privacidade e segurança |  |
| Dependência de integrações externas |  |
| Potencial de virar produto |  |

### Menor primeiro passo

### Harness mínimo

### Partes mockadas

### Riscos

### Critério de pronto da primeira versão

### Próximo passo
```

## Regra de privacidade

Projetos que envolvem dados pessoais, saúde, finanças, documentos fiscais, contatos, aniversários, e-mails ou calendários devem começar obrigatoriamente com dados sintéticos.

Dados reais só devem ser usados depois que:

* o escopo estiver claro;
* o harness estiver funcionando;
* houver anonimização;
* os riscos estiverem documentados;
* existir validação humana;
* o dado real não for commitado no repositório.

A regra padrão é: fixture boa representa formato e comportamento, não preserva dados reais.
