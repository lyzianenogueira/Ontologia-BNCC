# Integração BNCC - ORSD

## Proposito
Apresentar um modelo ontologico para estruturar e integrar os conceitos da Base Nacional Comum Curricular (BNCC) de Computação aos conteudos da disciplina de Matemática do Ensino Fundamental II (6º ao 9º ano). Com a ontologia, deve ser possivel instanciar, consultar e recuperar informações sobre as relações conceituais entre computação e a matemática, de modo a auxiliar professores, coordenadores e elaboradores de currículo no planejamento pedagogico integrado.

## Escopo
A ontologia deve modelar o currículo de Computação do Ensino Fundamental II (6º ao 9º ano) conforme a BNCC, respondendo a questões sobre conexões interdisciplinares e progressão conceitual.

**Abrangerá:**
- Conceitos e habilidades de Computação por ano escolar;
- Conexões com a Matemática;
- Pré-requisitos e relações de progressão.

**Não abrangerá:**
- Conteúdos da Educação Infantil, do Ensino Fundamental I e do Ensino Médio.

## Linguagem de Implementação
A ontologia será especificada em OntoUML para a modelagem conceitual, depois será transformada em OWL (Web Ontology Language) para viabilizar a implementação computacional, e por fim será consultada por meio da linguagem SPARQL.

## Usuários-Finais Pretendidos
- **Usuário 1.** Professores (informática e demais disciplinas) para planejamento interdisciplinar;
- **Usuário 2.** Coordenadores e gestores para apoio à implementação da BNCC e formação docente;
- **Usuário 3.** Agentes governamentais que atuam na elaboração de políticas públicas voltadas à educação;
- **Usuário 4.** Pesquisadores em Informática na Educação;
- **Usuário 5.** Desenvolvedores de materiais e recursos educacionais.

## Usos Pretendidos
- **Uso 1.** Auxiliar no planejamento pedagógico integrado;
- **Uso 2.** Formalizar relações interdisciplinares entre a computação e os demais campos da BNCC;
- **Uso 3.** Promover o reuso de recursos computacionais;
- **Uso 4.** Identificar áreas em que o uso de recursos computacionais pode trazer prejuízos ao aprendizado;
- **Uso 5.** Documentar e disseminar conexões curriculares.

## Requisitos de Ontologia

### Requisitos Não-Funcionais
- **RNF 1. Usabilidade**  
  Deve apresentar facilidade de entendimento para usuários não-especialistas (professores e coordenadores), com visualização interativa e documentação acessível.
- **RNF 2. Alinhamento curricular**  
  Deve estar alinhada à BNCC de Computação e o que é previsto para Matemática, também pela BNCC.
- **RNF 3. Extensibilidade**  
  Deve ser projetada para permitir futuras expansões, incluindo a incorporação de novos conceitos e disciplinas, e a adaptação para outros níveis de ensino.
- **RNF 4. Encontrável**  
  Deve ser fácil de ser encontrada por qualquer pessoa ou sistema, para isso, deve ser publicada em repositórios conhecidos, receber um identificador e vir acompanhada de suas informações básicas.

### Requisitos Funcionais (Questões de Competência)
- **QC1.** Quais são os conceitos de computação previstos para cada ano do Ensino Fundamental II?
- **QC2.** Como um conceito de computação precede outro?
- **QC3.** Quais conceitos de computação se conectam com conceitos de Matemática?
- **QC4.** Quais conceitos computacionais pertencem a um determinado eixo/unidade temática da BNCC?
- **QC5.** Quais conceitos computacionais estão previstos para um determinado ano escolar?
- **QC6.** Quais conceitos matemáticos pertencem a uma determinada unidade temática da BNCC?
- **QC7.** Quais conceitos matemáticos estão previstos para um determinado ano escolar?
- **QC8.** Como um conceito de matemática precede outro?




# Implementação em OWL no Protégé

A ontologia foi implementada em OWL para garantir expressividade e capacidade de inferência computacional. A seguir, é detalhado como os requisitos técnicos foram cumpridos.

## Disjunção entre Classes
Foram estabelecidas disjunções para garantir que um indivíduo não possa pertencer a mais de uma classe em um conjunto específico. Por exemplo, `Matematica` e `Computacao` são disjuntos, assim como os conceitos derivados (`ConceitoMatematico` e `ConceitoComputacional`) e as séries da grade curricular (`6Ano`, `7Ano`, `8Ano`, `9Ano`).

## Condições Necessárias e Suficientes
- **Classes Primitivas**: A maioria das classes base (ex: `ConceitoDisciplinar`, `AnoEscolar`, `UnidadeTematica`) é definida com `SubClassOf`, estabelecendo as condições estruturais que seus membros devem cumprir.
- **Classes Definidas**: Classes como `ConceitoMatematico`, `ConceitoComputacional`, `ConceitoBase` e `ConceitoInterdisciplinar` são definidas com `EquivalentTo`. Isso permite que o inferenciador (reasoner) classifique automaticamente indivíduos nelas com base em suas propriedades.

## Axiomas de Fechamento
A propriedade `:pertence_a_unidade` na classe `ConceitoDisciplinar` utiliza restrições universais (`owl:allValuesFrom` / `only`) para garantir que um conceito só possa pertencer a instâncias exclusivas da classe `UnidadeTematica`, fechando o escopo da propriedade.

## Propriedades e Quantificadores
- **Object Properties**: Todas as propriedades têm domínios e imagens (ranges) bem definidos. Por exemplo, a propriedade `:especificado_por` liga a classe `ConceitoDisciplinar` à classe `AnoEscolar`.
- **Características de Propriedades**: Propriedades foram caracterizadas para refinar sua semântica computacional. Foram definidos axiomas como `Transitive` (para `:precede`, indicando que se A precede B, e B precede C, logo A precede C), `Symmetric` (para `:relacionaSe_com`) e o pareamento de propriedades inversas, como `:contem_conceito` (`owl:inverseOf` `:pertence_a_unidade`).
- **Quantificadores de Cardinalidade**: A ontologia usa quantificadores (`some`, `all`, `min`) para restringir as relações. Por exemplo, exige-se uma cardinalidade qualificada mínima (`min 1`) para os eventos interdisciplinares (`ConexaoCurricular`), garantindo que todo relator pedagógico deve mediar (`gufo:mediates`) ao menos um `ConceitoMatematico` e um `ConceitoComputacional`.

## Indivíduos
A ontologia é populada com indivíduos exemplos que ilustram a aplicação prática do modelo. Foram inseridos indivíduos estáticos para a grade (como `Ano_6`, `UT_Algebra`), conceitos das disciplinas (como `Propriedades_da_Igualdade` e `Algoritmos_Sequenciais`) e as instâncias das relações pedagógicas, como `Reforco_Logico` (Relator).

---

# Consultas SPARQL

O objetivo principal da utilização das consultas SPARQL foi garantir que o modelo respondia adequadamente às **Questões de Competência (QCs)** definidas no Documento de Especificação de Requisitos da Ontologia (ORSD).

Para atestar a capacidade de dedução lógica do modelo, a validação com SPARQL foi dividida em duas fases utilizando a API **Owlready2** em **Python**:

1. **Primeira fase (sem inferência)**: As consultas procuraram por instâncias específicas. Como as instâncias foram cadastradas na superclasse genérica `ConceitoDisciplinar`, o retorno inicial foi vazio, comprovando a ausência de uma inserção manual direta.
2. **Segunda fase (com inferência)**: Após a execução do raciocinador lógico HermiT, a ontologia aplicou as regras estruturadas e reclassificou os indivíduos de forma automática, permitindo que as consultas retornassem os conjuntos de dados completos.

Abaixo, detalham-se as principais consultas formuladas para verificar as Questões de Competência:

---

## QC1. Quais são os conceitos de computação previstos para cada ano do Ensino Fundamental II?

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?ano ?conceito WHERE {
  ?conceito rdf:type :ConceitoComputacional .
  ?conceito :especificado_por ?ano .
} ORDER BY ?ano
```
## QC2. Como um conceito de computação precede outro?

Valida os pré-requisitos internos da disciplina de Computação, garantindo que o encadeamento pedagógico seja respeitado via propriedade transitiva `:precede`.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?conceitoBase ?conceitoAvancado WHERE {
    ?conceitoBase rdf:type :ConceitoComputacional .
    ?conceitoAvancado rdf:type :ConceitoComputacional .
    ?conceitoBase :precede ?conceitoAvancado .
}
```
## QC3. Quais conceitos de computação se conectam com conceitos de Matemática?

Esta questão avalia a interdisciplinaridade do modelo. Ela explora a semântica da interdisciplinaridade utilizando o operador `UNION` para buscar duas abordagens distintas: as conexões diretas (através da propriedade simétrica `:relacionaSe_com`) e as conexões indiretas mediadas por classes relatoras (como `Reforca`, `Requer` e `Compartilha`, subclasses de `ConexaoCurricular`). Devido a limitações técnicas da API em lidar com inferências num único bloco `UNION`, a consulta foi dividida em duas partes no código final.

### Parte 1 – Interdisciplinaridade Direta

Investiga as conexões diretas entre as matérias. Utiliza o operador `UNION` para mapear a propriedade simétrica `:relacionaSe_com` em ambas as direções, desviando das restrições de orientação do SPARQL.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?comp ?mat WHERE {
    ?comp rdf:type :ConceitoComputacional .
    ?mat rdf:type :ConceitoMatematico .
    { ?comp :relacionaSe_com ?mat . }
    UNION
    { ?mat :relacionaSe_com ?comp . }
}
```
### Parte 2 – Interdisciplinaridade via Relatores

Extrai as conexões mediadas por eventos pedagógicos complexos baseados em gUFO (subclasses de `ConexaoCurricular`). Esta abordagem recupera os conceitos mediados pela propriedade `gufo:mediates`, aplicando um filtro (`FILTER IN`) para exibir textualmente a natureza semântica da relação (`Reforca`, `Compartilha` ou `Requer`).

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?comp ?tipoRelacao ?mat WHERE {
    ?comp rdf:type :ConceitoComputacional .
    ?mat rdf:type :ConceitoMatematico .
    ?relator gufo:mediates ?comp .
    ?relator gufo:mediates ?mat .
    ?relator rdf:type ?tipoRelacao .
    FILTER (?tipoRelacao IN (:Reforca, :Compartilha, :Requer))
}
```
## QC4. Quais conceitos computacionais pertencem a um determinado eixo/unidade temática da BNCC?

Filtra e organiza as competências digitais com base nos eixos da BNCC (como Cultura Digital ou Mundo Digital), utilizando a relação `:pertence_a_unidade`.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?unidadeTematica ?conceito WHERE {
    ?conceito rdf:type :ConceitoComputacional .
    ?conceito :pertence_a_unidade ?unidadeTematica .
} ORDER BY ?unidadeTematica
```
## QC5. Quais conceitos computacionais estão previstos para um determinado ano escolar?

Busca na ontologia para mostrar a distribuição cronológica dos conceitos de Computação em um ano especificado, no exemplo o 6º ano.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?conceito WHERE {
    ?conceito rdf:type :ConceitoComputacional .
    ?conceito :especificado_por :Ano_6 .
}
```
## QC6. Quais conceitos matemáticos pertencem a uma determinada unidade temática da BNCC?

Mapeia de forma análoga à QC4 as instâncias inferidas como pertencentes à disciplina de Matemática, agrupando-as pelas unidades temáticas estabelecidas no documento formal.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?unidadeTematica ?conceito WHERE {
    ?conceito rdf:type :ConceitoMatematico .
    ?conceito :pertence_a_unidade ?unidadeTematica .
} ORDER BY ?unidadeTematica
```
## QC7. Quais conceitos matemáticos estão previstos para um determinado ano escolar?

Busca na ontologia para mostrar a distribuição cronológica de todos os conceitos de Matemática ao longo das quatro séries finais do Ensino Fundamental.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?ano ?conceito WHERE {
    ?conceito rdf:type :ConceitoMatematico .
    ?conceito :especificado_por ?ano .
} ORDER BY ?ano
```
## QC8. Como um conceito de matemática precede outro?

Mapeia de forma estrita as dependências e a progressão de conteúdos da própria Matemática, utilizando a propriedade transitiva `:precede`.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?conceitoBase ?conceitoAvancado WHERE {
    ?conceitoBase rdf:type :ConceitoMatematico .
    ?conceitoAvancado rdf:type :ConceitoMatematico .
    ?conceitoBase :precede ?conceitoAvancado .
}
```

# Consultas Extras

Foram elaboradas mais três consultas extras para demonstrar que o modelo com inferência gera resultados consistentes.

## 1. Inventário Geral de Conceitos

Esta consulta varre a ontologia em busca de todas as instâncias cadastradas na superclasse abstrata `ConceitoDisciplinar`, mapeando-as aos seus respectivos anos letivos.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?conceito ?ano WHERE {
    ?conceito rdf:type :ConceitoDisciplinar .
    ?conceito :especificado_por ?ano .
} ORDER BY ?ano
```
## 2. Mapeamento das Unidades Temáticas e Disciplinas

Consulta responsável por extrair a relação entre os eixos de ensino (Unidades Temáticas) e as disciplinas da Base Nacional Comum Curricular (BNCC).

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?unidade ?disciplina WHERE {
    ?unidade rdf:type :UnidadeTematica .
    ?unidade :pertence_a_disciplina ?disciplina .
} ORDER BY ?disciplina
```
## 3. Precedência (Geral)

Esta consulta omite as restrições de classes específicas e busca puramente pela existência da relação de dependência educacional entre quaisquer dois conceitos.

```sparql
PREFIX : <http://example.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gufo: <http://purl.org/nemo/gufo#>

SELECT ?conceitoBase ?conceitoAvancado WHERE {
    ?conceitoBase :precede ?conceitoAvancado .
}
```

## Erros encontrado no processo de importação de OntoUML para OWL

Passar o modelo desenhado (OntoUML) para o modelo funcional no Protégé (OWL) trouxe alguns desafios práticos bem interessantes. Lidar com as ferramentas de modelagem exigiu bastante paciência, testes e refações. Abaixo, estão listados os três principais problemas enfrentados e como foram resolvidos:

**Conexões antigas**: Para ganhar tempo, foi reaproveitado partes de um modelo OntoUML mais antigo para montar uma nova versão. O problema é que, mesmo quando era apagado algumas ligações na tela da ferramenta, ela não deletava isso de verdade no código. Quando o arquivo era exportado para o Protégé essas ligações fantasmas iam junto, o que gerava erros. A solução foi fazer um modelo totalmente novo, desenvolvendo com bastante cuidado para não haver nenhum erro.

**Direção das relações**: Na teoria usada (gUFO), as setas de uma relação de mediação precisam, obrigatoriamente, sair do Relator e apontar para os conceitos. No início, essas setas foram ligadas sem prestar muita atenção à direção. O Visual Paradigm até avisou que tinha invertido as setas automaticamente para corrigir, mas na hora de exportar para OWL, ele exportou exatamente como havia sido ligado, mesmo que visualmente estivesse correto. Isso quebrou o modelo no Protégé. Para consertar, as conexões tiveram que ser apagadas e refeitas na direção exata desde o começo.

**Complexidade**: Ao ligar o raciocinador lógico (Reasoner) no Protégé para testar o sistema, foi notado que quanto maior a ontologia ficava, mais impossível era achar a causa de um erro. Um pequeno erro em uma regra fazia a ferramenta apontar falhas em vários lugares ao mesmo tempo. A melhor estratégia encontrada para lidar com isso foi a simplificação, a ontologia foi reduzida a um modelo mais básico, o que facilitou muito na hora de isolar e consertar os problemas.








