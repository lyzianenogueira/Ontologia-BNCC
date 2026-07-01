import streamlit as st
from owlready2 import *
import pandas as pd
import re
import os

st.set_page_config(page_title="Ontologia BNCC", layout="wide")

st.title("Visualizador da Ontologia BNCC - Computação e Matemática")

@st.cache_resource
def load_and_populate_ontology():
    my_world = World()
    
    # Obtendo o diretório atual onde o app.py está localizado
    base_dir = os.path.dirname(os.path.abspath(__file__))
    gufo_path = os.path.join(base_dir, "gUFO-RDF.rdf").replace("\\", "/")
    onto_path = os.path.join(base_dir, "ontoBNCC.rdf").replace("\\", "/")
    
    # Carregando as ontologias usando caminhos dinâmicos
    PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo#/1.0.0"] = gufo_path
    onto_gUFO = my_world.get_ontology(gufo_path).load()
    ontoBNCC = my_world.get_ontology(onto_path).load()
    
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
        
    my_world.is_inferred = False
    return my_world, ontoBNCC, onto_gUFO

try:
    with st.spinner("Carregando ontologia e povoando a A-BOX..."):
        my_world, ontoBNCC, onto_gUFO = load_and_populate_ontology()
    st.success("Ontologias carregadas e povoadas com sucesso!")
except Exception as e:
    st.error(f"Erro ao carregar ontologias: {e}")
    st.stop()

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

# Definindo as abas na nova ordem solicitada
tab1, tab2, tab3, tab4 = st.tabs([
    "Visões da Ontologia (Imagens)", 
    "Consultas SPARQL (Código)", 
    "Modelo Asserted (Sem Inferência)", 
    "Modelo Inferred (Com Inferência)"
])

def render_results(resultados, query):
    if not resultados:
        st.info("0 registros encontrados.")
    else:
        # Extract headers from SELECT
        match = re.search(r'SELECT\s+(?:DISTINCT\s+)?(.*?)\s+WHERE', query, re.IGNORECASE)
        cabecalhos = [var.replace('?', '').strip().capitalize() for var in match.group(1).split()] if match else []
        
        # Convert results to a list of lists of strings
        data = []
        for linha in resultados:
            data.append([item.name if hasattr(item, 'name') else str(item) for item in linha])
        
        if not cabecalhos or len(cabecalhos) != len(data[0]):
            cabecalhos = [f"Col {i+1}" for i in range(len(data[0]))]
                
        df = pd.DataFrame(data, columns=cabecalhos)
        st.dataframe(df, use_container_width=True)

with tab1:
    st.header("Visões da Ontologia")
    st.markdown("Abaixo estão as representações visuais da ontologia (Diagramas gerados).")
    
    # Exibir as imagens
    try:
        st.image("Visao principal.png", caption="Visão Principal", use_container_width=True)
        st.markdown("---")
        st.image("Visao 2.png", caption="Visão 2", use_container_width=True)
        st.markdown("---")
        st.image("Visao 3.png", caption="Visão 3", use_container_width=True)
    except Exception as e:
        st.error(f"Erro ao carregar as imagens: {e}")

with tab2:
    st.header("Código das Consultas SPARQL")
    st.markdown("Abaixo você encontra as consultas SPARQL puras que estão sendo executadas nesta aplicação.")
    
    # Mostrar o prefixo usado em todas as consultas
    st.subheader("Prefixos Utilizados")
    st.code(PREFIXOS, language="sparql")
    
    st.subheader("Consultas de Competência (QCs)")
    for nome_qc, query in consultas.items():
        st.markdown(f"**{nome_qc}**")
        st.code(query, language="sparql")

with tab3:
    st.header("Resultados do Modelo Asserted")
    st.markdown("Como os dados foram inseridos genericamente, muitas consultas devem retornar **vazias** pois dependem da classificação do raciocinador.")
    
    for nome_qc, query in consultas.items():
        with st.expander(nome_qc):
            resultados = list(my_world.sparql(PREFIXOS + query))
            render_results(resultados, query)

with tab4:
    st.header("Resultados do Modelo Inferred")
    
    # Run reasoner if a button is clicked or just run it
    if st.button("Executar Raciocinador (Sync Reasoner)", type="primary"):
        if getattr(my_world, "is_inferred", False):
            st.info("O raciocinador já foi executado nesta sessão! (Dados já classificados)")
        else:
            with st.spinner("Executando o raciocinador (Inferência Lógica)..."):
                with ontoBNCC:
                    sync_reasoner([ontoBNCC])
                my_world.is_inferred = True
            st.success("Inferências geradas com sucesso!")
        st.session_state['reasoner_run'] = True

    if st.session_state.get('reasoner_run', False) or getattr(my_world, "is_inferred", False):
        st.session_state['reasoner_run'] = True
        st.markdown("Agora as consultas encontrarão os dados classificados!")
        for nome_qc, query in consultas.items():
            with st.expander(nome_qc, expanded=True):
                resultados = list(my_world.sparql(PREFIXOS + query))
                render_results(resultados, query)
    else:
        st.warning("Clique no botão acima para executar o raciocinador e ver os resultados inferidos.")
