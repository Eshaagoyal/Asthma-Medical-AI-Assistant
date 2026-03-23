import streamlit as st
from app import initialize_system
from safety.guardrails import Guardrails

st.title("🤖 Asthma Chat Assistant")

# Load AI system
@st.cache_resource
def load_rag():
    return initialize_system()

rag = load_rag()
guard = Guardrails()

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
prompt = st.chat_input("Ask something about asthma...")

if prompt:

    safe, response = guard.filter_query(prompt)

    if not safe:
        answer = response
    else:
        answer = rag.run(prompt)

    st.session_state.messages.append(("user", prompt))
    st.session_state.messages.append(("assistant", answer))

# Display chat
for role, msg in st.session_state.messages:

    if role == "user":
        st.chat_message("user").write(msg)

    else:
        st.chat_message("assistant").write(msg)

# Example questions
st.sidebar.header("Example Questions")

examples = [
    "What is asthma?",
    "What are asthma symptoms?",
    "What triggers asthma attacks?",
    "How does an inhaler work?",
]

for q in examples:
    if st.sidebar.button(q):
        st.session_state.messages.append(("user", q))
        st.session_state.messages.append(("assistant", rag.run(q)))