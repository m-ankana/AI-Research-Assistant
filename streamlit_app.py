import streamlit as st
import requests

st.title(" AI research assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.write("Processing ...")

    # send file to FastAPI
    files = {"file": uploaded_file.getvalue()} 
    response = requests.post("http://127.0.0.1:8000/summarise", files=files)


    if response.status_code == 200:
        summary = response.json().get("summary", "No summary available.")
        st.subheader("Summary :")
        st.write(summary)

    else:
        st.error("Error: Could not summarize PDF")