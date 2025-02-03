import streamlit as st
import openai

# 🔹 Configurer l’API OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🔹 Interface du chatbot
st.title("🤖 Chatbot Innov'BOULON")
st.subheader("💡 Posez vos questions sur l’IA et la Blockchain")

# 🔹 Historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Afficher les messages précédents
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 🔹 Saisie utilisateur
user_input = st.chat_input("Posez une question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 🔹 Envoyer la requête à OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Tu es un expert en IA et Blockchain, réponds en français."}] +
                  st.session_state.messages,
        temperature=0.7
    )
    bot_response = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # 🔹 Afficher la réponse
    with st.chat_message("assistant"):
        st.write(bot_response)
