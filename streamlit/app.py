import os

import streamlit as st

from embedchain import App


@st.cache_resource
def ec_app():
    return App.from_config(config_path="config.yaml")

st.title("💬 Chatbot")
st.caption("🚀 Powered by Embedchain + Mixtral!")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
        Hi! I'm a chatbot. I can answer questions and learn new things!\n
        Ask me anything and if you want me to learn something do `/add <source>`.\n
        I can learn mostly everything. :)
        """,
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    app = ec_app()

    if prompt.startswith("/add"):
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        prompt = prompt.replace("/add", "").strip()
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Adding to knowledge base...")
            app.add(prompt)
            message_placeholder.markdown(f"Added {prompt} to knowledge base!")
            st.session_state.messages.append({"role": "assistant", "content": f"Added {prompt} to knowledge base!"})
            st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("Thinking...")
        full_response = ""
        full_contexts: list[tuple[str, dict]] = []

        response, contexts = app.chat(prompt, citations=True)
        msg_placeholder.empty()
        full_response += response
        full_contexts.extend(contexts)

        msg_placeholder.markdown(full_response)
        st.code(full_contexts)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
