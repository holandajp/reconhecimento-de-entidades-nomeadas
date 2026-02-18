import streamlit as st
import spacy
from spacy import displacy
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NER Jurídico",
    page_icon="⚖️",
    layout="wide"
)

st.title("Reconhecimento de Entidades Nomeadas")
st.caption("Modelo treinado com spaCy para análise de textos jurídicos")

st.divider()

@st.cache_resource
def carregar_modelo():
    return spacy.load("modelo")

modelo = carregar_modelo()

with st.sidebar:
    st.header("Configurações")
    escolha = st.radio(
        "Entrada de dados:",
        ["Texto", "Arquivo"]
    )

texto = ""

if escolha == "Texto":
    texto = st.text_area(
        "Insira o texto jurídico:",
        height=200,
        placeholder="Digite ou cole o texto aqui..."
    )

elif escolha == "Arquivo":
    arquivo = st.file_uploader(
        "Upload de arquivo .txt",
        type="txt"
    )
    if arquivo is not None:
        texto = arquivo.read().decode("utf-8")

cores = {
    'B-JURISPRUDENCIA': '#F0F8FF',
    'B-LEGISLACAO': '#FA8072',
    'B-LOCAL': '#98FB98',
    'B-ORGANIZACAO': '#DDA0DD',
    'B-PESSOA': '#F0E68C',
    'B-TEMPO': '#FFB6C1',
    'I-JURISPRUDENCIA': '#F0F8FF',
    'I-LEGISLACAO': '#FA8072',
    'I-LOCAL': '#98FB98',
    'I-ORGANIZACAO': '#DDA0DD',
    'I-PESSOA': '#F0E68C',
    'I-TEMPO': '#FFB6C1',
    'LOC': '#D3D3D3',
    'MISC': '#D3D3D3',
    'ORG': '#D3D3D3',
    'PER': '#D3D3D3'
}

options = {"colors": cores}

if texto:
    st.subheader("Entidades Reconhecidas")

    doc = modelo(texto)

    html = displacy.render(
        doc,
        style="ent",
        page=False,
        options=options
    )

    html_wrapper = f"""
    <div style="padding: 20px; border-radius: 10px;">
        {html}
    </div>
    """

    components.html(html_wrapper, height=600, scrolling=True)