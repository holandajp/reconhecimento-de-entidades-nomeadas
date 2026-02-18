import streamlit as st
import spacy
from spacy import displacy
import streamlit.components.v1 as components

st.title('Reconhecimento de entidades nomeadas (NER)')

caminho_modelo = 'modelo'
modelo = spacy.load(caminho_modelo)

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
    html = displacy.render(doc, style="ent", page=True)
    components.html(html, height=600, scrolling=True)