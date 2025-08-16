import streamlit as st 
from io import StringIO
import pandas as pd 
from langchain_community.document_loaders import PyMuPDFLoader
import os



st.title("Chatbot")

st.write("Hoşgeldiniz.. Sizi burada görmek çok güzel. Size nasıl yardımcı olmamı istersiniz?")
yazi= st.text_input("Bugün ne hakkında bilgi almak istersin: ")



yüklenen_dosya = st.file_uploader("Dosya seçin", type=["pdf"])
if yüklenen_dosya is not None:
    with st.spinner("PDF işleniyor..."):
    
        with open("temp.pdf", "wb") as f:
            f.write(yüklenen_dosya.read())

    st.success("Pdf başarlı bir şekilde okundu.")

    loader = PyMuPDFLoader("temp.pdf")
    data = loader.load()

    st.write("ilk sayfa örneği:")
    st.write(data[0].page_content)
elif yüklenen_dosya is None:
    st.warning("Lütfen dosya ekleyiniz.")


    





