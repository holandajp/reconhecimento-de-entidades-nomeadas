import streamlit as st
import spacy

st.title('Reconhecimento de entidades nomeadas (NER)')

caminho_modelo = 'modelo'
modelo = spacy.load(caminho_modelo)

texto = ''

arquivo = st.file_uploader('Faça o upload do arquivo (somente .txt)', type='txt')
if arquivo is not None:
    texto = arquivo.read().decode('utf-8')

if texto:
    doc = modelo(texto)
    st.subheader('Entidades reconhecidas')
    for entidade in doc.ents:
        st.text(f'{entidade.text} -> {entidade.label_}')