#source language to target language
#prompt
#translator function
#put a translate button ->download button
import streamlit as st
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()  # Load variables from .env

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))


st.title("AI Translator")
st.divider()

input_text = st.text_area("Enter the text you want to translate:")

source_language = st.selectbox("Select source language", ["English", "Odia", "Tamil", "Telugu", "Hindi", "French", "German"])
target_language = st.selectbox("Select target language", ["English", "Odia", "Tamil", "Telugu", "Hindi", "French", "German"])

def translate_text(input_text, source_language, target_language):
    prompt = f"Translate this from {source_language} to {target_language}: {input_text}"
    translation = llm(prompt)
    return translation

if st.button("Translate"):
    if input_text:
        if source_language == target_language:
            st.warning("Source and target languages are the same. Please choose different languages.")
        else:
            translation = translate_text(input_text, source_language, target_language)
            st.write("Translation:", translation)

            st.download_button(
                label="Download Translation as .txt file",
                data=translation,
                file_name="translation.txt",
                mime="text/plain"
            )
    else:
        st.write("Please enter some text to translate.")
