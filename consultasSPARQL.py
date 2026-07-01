from owlready2 import *
from tabulate import tabulate
import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
gufo_path = os.path.join(base_dir, "gUFO-RDF.rdf").replace("\\", "/")
onto_path = os.path.join(base_dir, "ontoBNCC.rdf").replace("\\", "/")

PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo#/1.0.0"] = gufo_path
onto_gUFO = get_ontology(gufo_path).load()
ontoBNCC = get_ontology(onto_path).load()

print("\n" + "="*60)
print("Inserindo novas instâncias...")
print("="*60)

with ontoBNCC:
    transf_geom = ontoBNCC.ConceitoDisciplinar("Transformacoes_Geometricas")
    transf_geom.especificado_por.append(ontoBNCC.Ano_7)
    transf_geom.pertence_a_unidade.append(ontoBNCC.UT_Geometria)

    tales = ontoBNCC.ConceitoDisciplinar("Teorema_de_Tales")
    tales.especificado_por.append(ontoBNCC.Ano_9)
    tales.pertence_a_unidade.append(ontoBNCC.UT_Geometria)
    transf_geom.precede.append(tales) 

    eq_1_grau = ontoBNCC.ConceitoDisciplinar("Equacoes_de_1_Grau")
    eq_1_grau.especificado_por.append(ontoBNCC.Ano_7)
    eq_1_grau.pertence_a_unidade.append(ontoBNCC.UT_Algebra)
    ontoBNCC.Propriedades_da_Igualdade.precede.append(eq_1_grau) 

    fracoes = ontoBNCC.ConceitoDisciplinar("Fracoes_Equivalentes")
    fracoes.especificado_por.append(ontoBNCC.Ano_6)
    fracoes.pertence_a_unidade.append(ontoBNCC.UT_Numeros)

    dizimas = ontoBNCC.ConceitoDisciplinar("Dizimas_Periodicas")
    dizimas.especificado_por.append(ontoBNCC.Ano_8)
    dizimas.pertence_a_unidade.append(ontoBNCC.UT_Numeros)
    fracoes.precede.append(dizimas)

    graf_barras = ontoBNCC.ConceitoDisciplinar("Graficos_de_Barras")
    graf_barras.especificado_por.append(ontoBNCC.Ano_6)
    graf_barras.pertence_a_unidade.append(ontoBNCC.UT_ProbabilidadeE_Estatistica)

    unid_dados = ontoBNCC.ConceitoDisciplinar("Unidades_de_Armazenamento_Dados")
    unid_dados.especificado_por.append(ontoBNCC.Ano_9)
    unid_dados.pertence_a_unidade.append(ontoBNCC.UT_GrandezasEMedidas)

    nuvem = ontoBNCC.ConceitoDisciplinar("Armazenamento_em_Nuvem")
    nuvem.especificado_por.append(ontoBNCC.Ano_8)
    nuvem.pertence_a_unidade.append(ontoBNCC.UT_MundoDigital)
    
    unid_dados.relacionaSe_com.append(nuvem)

    sist_operacionais = ontoBNCC.ConceitoDisciplinar("Sistemas_Operacionais")
    sist_operacionais.especificado_por.append(ontoBNCC.Ano_6)
    sist_operacionais.pertence_a_unidade.append(ontoBNCC.UT_MundoDigital)

    cyber = ontoBNCC.ConceitoDisciplinar("Impacto_do_Cyberbullying")
    cyber.especificado_por.append(ontoBNCC.Ano_7)
    cyber.pertence_a_unidade.append(ontoBNCC.UT_CulturaDigital)

    est_repeticao = ontoBNCC.ConceitoDisciplinar("Estruturas_de_Repeticao")
    est_repeticao.especificado_por.append(ontoBNCC.Ano_8)
    est_repeticao.pertence_a_unidade.append(ontoBNCC.UT_PensamentoComputacional)
    ontoBNCC.Algoritmos_Sequenciais.precede.append(est_repeticao)

    variaveis = ontoBNCC.ConceitoDisciplinar("Variaveis_e_Constantes")
    variaveis.especificado_por.append(ontoBNCC.Ano_9)
    variaveis.pertence_a_unidade.append(ontoBNCC.UT_PensamentoComputacional)
    
    variaveis.relacionaSe_com.append(eq_1_grau)



print("\n" + "="*60)
print("A EXECUTAR CONSULTAS SPARQL")
print("="*60)

# Prefixos base para as consultas
PREFIXOS = """
    PREFIX : <http://example.com#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX gufo: <http://purl.org/nemo/gufo#>
"""

# Dicionário com todas as QCs
consultas = {
    "QC1 - Conceitos de Computação por Ano": """
        SELECT ?ano ?conceito WHERE {
            ?conceito rdf:type :ConceitoComputacional .
            ?conceito :especificado_por ?ano .
        } ORDER BY ?ano
    """,
    "QC2 - Precedência na Computação": """
        SELECT ?base ?avancado WHERE {
            ?base rdf:type :ConceitoComputacional .
            ?avancado rdf:type :ConceitoComputacional .
            ?base :precede ?avancado .
        }
    """,
   "QC3 (Parte 1) - Interdisciplinaridade via relaciona-se": """
        SELECT ?comp ?mat WHERE {
            ?comp rdf:type :ConceitoComputacional .
            ?mat rdf:type :ConceitoMatematico .
            { ?comp :relacionaSe_com ?mat . }
            UNION
            { ?mat :relacionaSe_com ?comp . }
        }
    """,
    
    "QC3 (Parte 2) - Interdisciplinaridade via relator": """
        SELECT ?comp ?tipoRelacao ?mat WHERE {
            ?comp rdf:type :ConceitoComputacional .
            ?mat rdf:type :ConceitoMatematico .
            ?relator gufo:mediates ?comp .
            ?relator gufo:mediates ?mat .
            ?relator rdf:type ?tipoRelacao .
            FILTER (?tipoRelacao IN (:Reforca, :Compartilha, :Requer))
        }
    """,
    "QC4 - Conceitos Computacionais por Unidade Temática": """
        SELECT ?unidade ?conceito WHERE {
            ?conceito rdf:type :ConceitoComputacional .
            ?conceito :pertence_a_unidade ?unidade .
        } ORDER BY ?unidade
    """,
    "QC5 - Conceitos de Computação no 6º Ano": """
        SELECT ?conceito WHERE {
            ?conceito rdf:type :ConceitoComputacional .
            ?conceito :especificado_por :Ano_6 .
        }
    """,
    "QC6 - Conceitos Matemáticos por Unidade Temática": """
        SELECT ?unidade ?conceito WHERE {
            ?conceito rdf:type :ConceitoMatematico .
            ?conceito :pertence_a_unidade ?unidade .
        } ORDER BY ?unidade
    """,
    "QC7 - Conceitos Matemáticos por Ano Escolar": """
        SELECT ?ano ?conceito WHERE {
            ?conceito rdf:type :ConceitoMatematico .
            ?conceito :especificado_por ?ano .
        } ORDER BY ?ano
    """,
    "QC8 - Precedência na Matemática": """
        SELECT ?base ?avancado WHERE {
            ?base rdf:type :ConceitoMatematico .
            ?avancado rdf:type :ConceitoMatematico .
            ?base :precede ?avancado .
        }
    """,
    "Consulta Extra - Todos os conceitos": """
        SELECT ?conceito ?ano WHERE {
            ?conceito rdf:type :ConceitoDisciplinar .
            ?conceito :especificado_por ?ano .
        } ORDER BY ?ano
    """,
    "Consulta Extra - Unidades temáticas": """
        SELECT ?unidade ?disciplina WHERE {
            ?unidade rdf:type :UnidadeTematica .
            ?unidade :pertence_a_disciplina ?disciplina .
        } ORDER BY ?disciplina
    """,
    "Consulta Extra - Precedência": """
        SELECT ?conceitoBase ?conceitoAvancado WHERE {
            ?conceitoBase :precede ?conceitoAvancado .
        }
    """
}


print("\n" + "="*60)
print("EXECUTANDO MODELO ASSERTED - SEM INFERÊNCIA")
print("="*60)

for nome_qc, query in consultas.items():
    print(f"\n[{nome_qc}]")
    resultados = list(default_world.sparql(PREFIXOS + query))
    if not resultados:
        print("   -> Resultado: 0 registros encontrados")
    else:
        # Extrair cabeçalhos do SELECT
        match = re.search(r'SELECT\s+(?:DISTINCT\s+)?(.*?)\s+WHERE', query, re.IGNORECASE)
        cabecalhos = [var.replace('?', '').strip().capitalize() for var in match.group(1).split()] if match else []

        # Limpar os dados e formatar a tabela
        dados_tabela = []
        for linha in resultados:
            linha_limpa = [item.name if hasattr(item, 'name') else str(item) for item in linha]
            dados_tabela.append(linha_limpa)
            
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="fancy_grid"))


print("\n" + "="*60)
print("LIGANDO O REASONER")
print("="*60)
with ontoBNCC:
    sync_reasoner()
print("Inferências geradas")


print("\n" + "="*60)
print("EXECUTANDO MODELO INFERRED - COM INFERÊNCIA")
print("="*60)

for nome_qc, query in consultas.items():
    print(f"\n[{nome_qc}]")
    resultados = list(default_world.sparql(PREFIXOS + query))
    if not resultados:
        print("   -> Nenhum resultado encontrado.")
    else:
        # Extrair cabeçalhos do SELECT
        match = re.search(r'SELECT\s+(?:DISTINCT\s+)?(.*?)\s+WHERE', query, re.IGNORECASE)
        cabecalhos = [var.replace('?', '').strip().capitalize() for var in match.group(1).split()] if match else []

        # Limpar os dados e formatar a tabela
        dados_tabela = []
        for linha in resultados:
            linha_limpa = [item.name if hasattr(item, 'name') else str(item) for item in linha]
            dados_tabela.append(linha_limpa)
            
        print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="fancy_grid"))

print("\n" + "="*60)
print("FIM DO PROCESSAMENTO")
print("="*60)