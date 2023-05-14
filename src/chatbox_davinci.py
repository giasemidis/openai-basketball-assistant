import os

import openai
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header

openai.organization = os.getenv("OPENAI_API_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_text():
    """Input text by the user"""
    input_text = st.text_input(
        "Ask me your question. Answers will be limited to 256 tokens",
        "",
        key="input"
    )
    return input_text


def generate_response_completion(prompt, input_text):
    """Generate Reponse using davinci API"""
    prompt += input_text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt, max_tokens=256,
        temperature=0
    )
    return response["choices"][0]["text"]

def chatbot_davinci():
    """Chatbox based on Completion API and davinci model"""
    st.title("GIASE: Your basketball expert chatbox.")

    greeting_bot_msg = (
        "Hi, I am Giase, you basketball expert. Ask me anything, basketball related.\n"
        "Ah! I have no knowledge of 2022 onwards, because I am powered by ChatGPT. "
        "So, I don't do predictions.\n"
        "*Example*: 'Who won the NBA finals in 2011 and who won the finals MVP?'\n"
        "I don't answer questions like 'Who was US president in 2010?'"
    )

    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = [greeting_bot_msg]

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    prompt = "You are a basketball expert. If a question is not related to basketball answer 'This is a non-basketball question'. Limit your answer to 256 tokens if possible"

    user_input = get_text()

    if user_input:
        response = generate_response_completion(prompt, user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            if i - 1 >= 0:
                message(st.session_state['past'][i - 1], is_user=True, key=str(i) + '_user')


if __name__ == "__main__":
    chatbot_davinci()
