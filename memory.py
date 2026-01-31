import streamlit as st

def init_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_to_memory(user, bot):
    st.session_state.chat_history.append(
        {"user": user, "bot": bot}
    )

def get_context():
    context = ""
    for chat in st.session_state.chat_history[-3:]:
        context += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    return context
