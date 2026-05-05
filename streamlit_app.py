import streamlit as st
import os
from google.cloud import dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sid-helper-cnt9-4f9cc5855647.json"

PROJECT_ID = "sid-helper-cnt9"

def detect_intent(text, session_id="123456"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

st.title("💱 SID Helper - Currency Converter")
st.write("Ask me to convert any currency!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("e.g. Convert 100 USD to PKR"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    bot_reply = detect_intent(prompt)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)