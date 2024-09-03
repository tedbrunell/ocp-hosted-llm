import streamlit as st
import os
from openai import OpenAI

os.environ["SSL_CERT_FILE"] = "/home/ted/.local/share/mkcert/rootCA.pem"


openai_api_key="EMPTY"
openai_api_base="https://gemma-2b-it-hosted-llm.apps.sno.brunell.lab/v1"
client = OpenAI(api_key=openai_api_key,base_url=openai_api_base)

with st.sidebar:
    st.title("Gemma-2b-it ChatBot")
    temp = st.slider("Temperature for LLM", 0.1, 1.0, (0.7),help="Controls the randomness and creativity of the output")
#    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    chat_response = client.chat.completions.create(
      model="gemma-2b-it",
      messages=[
        {"role": "user", "content": prompt},
    ],
    temperature=temp
)

    msg = chat_response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)