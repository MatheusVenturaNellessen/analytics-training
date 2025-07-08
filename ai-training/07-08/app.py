import streamlit as st
import requests

st.set_page_config(page_icon="🦙", page_title="Pergunte à llama", layout="wide")

st.title("Tem alguma dúvida? Pergunte à llama!")

# Modelos disponíveis
modelos_disponiveis = ["llama3:8b"]
st.sidebar.title("Configurações")
modelo_selecionado = st.sidebar.selectbox("Escolha o modelo:", modelos_disponiveis)

# Inicializa o histórico
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Botão para limpar histórico
if st.sidebar.button("Limpar histórico"):
    st.session_state.chat_history = []

# Área de entrada do usuário
user_input = st.text_area("Digite sua pergunta:", height=150)

# Enviar pergunta
if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Digite algo antes de enviar.")
    else:
        with st.spinner("Gerando resposta..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": modelo_selecionado,
                        "prompt": user_input,
                        "stream": False
                    }
                )
                data = response.json()
                resposta = data["response"]

                # Salva no histórico
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("llama", resposta))

            except Exception as e:
                st.error(f"Erro ao chamar o modelo: {e}")

# Exibir histórico
if st.session_state.chat_history:
    for remetente, mensagem in st.session_state.chat_history:
        with st.chat_message("user" if remetente == "user" else "assistant"):
            st.markdown(mensagem)
