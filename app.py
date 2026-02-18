import streamlit as st
import spacy
from spacy import displacy
import streamlit.components.v1 as components

st.title('Reconhecimento de entidades nomeadas (NER)')

caminho_modelo = 'modelo'
modelo = spacy.load(caminho_modelo)

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

options = {
    "colors": cores
}

escolha = st.radio(label='Escolha uma opção:', options=['Texto', 'Arquivo'])

texto = ''

if escolha == 'Texto':
    texto = st.text_area('Insira o texto:')
elif escolha == 'Arquivo':
    arquivo = st.file_uploader('Faça o upload do arquivo (somente .txt)', type='txt')
    if arquivo is not None:
        texto = arquivo.read().decode('utf-8')
        
if texto:
    doc = modelo(texto)
    html = displacy.render(doc, style="ent", page=True, options=options)
    components.html(html, height=600, scrolling=True)