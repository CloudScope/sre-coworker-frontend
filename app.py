import streamlit as st

st.set_page_config(page_title="SRE Coworker", page_icon="🤖")

# Custom CSS for better styling
st.markdown(f"<style>{open('assets/styles.css').read()}</style>", unsafe_allow_html=True)

st.title("SRE Coworker Chat Assistant")

st.markdown("Welcome to the SRE Coworker multi-agent chat interface. How can I assist you today?")

# Quick Actions
st.subheader("Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Application Health"):
        prompt = "Check the application health"
with col2:
    if st.button("GKP Status"):
        prompt = "Get Grafana, Kibana, Prometheus status"
with col3:
    if st.button("Incident Response"):
        prompt = "Assist with incident response"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type your message here..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process the prompt (placeholder for now)
    response = f"You said: {prompt}. This is a placeholder response from the multi-agent system."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})