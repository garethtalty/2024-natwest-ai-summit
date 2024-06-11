import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
model = "gpt-3.5-turbo"

st.set_page_config(page_title="Open AI Chat", page_icon="💬")
st.title("OpenAI Chat 💬")
st.sidebar.header("OpenAI Chat 💬")


    
    
def get_openai_response():
    chat_completion = client.chat.completions.create(
    messages=st.session_state.messages,
    model=model,
    )
    return chat_completion.choices[0].message.content.strip()

def submit():
    st.session_state.input_text = st.session_state.input_widget
    st.session_state.input_widget = ""

if 'messages' not in st.session_state or st.button("Reset chat"):
    st.session_state.messages = []
    st.session_state.input_text = ""

# Chat input
st.text_input("You: ", key="input_widget", on_change=submit)

# Extract the selected page from the URL parameters
page = st.query_params.get("page", ["home"])[0]

# Sending Messages
if st.session_state.input_text != "":
    st.session_state.messages.append({"role": "user", "content": st.session_state.input_text})
    response = get_openai_response()
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Assistant: {message['content']}")

