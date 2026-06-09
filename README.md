# Integração BNCC - ORSD

## Proposito
Apresentar um modelo ontologico para estruturar e integrar os conceitos da Base Nacional Comum Curricular (BNCC) de Computacao aos conteudos da disciplina de Matematica do Ensino Fundamental II (6º ao 9º ano). Com a ontologia, deve ser possivel instanciar, consultar e recuperar informacoes sobre as relacoes conceituais entre computacao e a matematica, de modo a auxiliar professores, coordenadores e elaboradores de curriculo no planejamento pedagogico integrado.

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
