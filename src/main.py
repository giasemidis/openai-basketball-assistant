import os
import streamlit as st
import openai


def main():
    openai.organization = os.getenv("OPENAI_API_ORG")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    st.title("GIASE: Your basketball specialist.")

    st.write("This is your basketball specialist. Ask me any basketball related question. Ah! I have no knowledge of 2022 onwards, because I am powered by ChatGPT. So, I don't do predictions.")

    st.write("**Example:** *'Who won the NBA finals in 2011 and who won the finals MVP?'*")
    st.write("I don't answer questions like *'Who was US president in 2010?'*")

    input_txt = st.text_area("Ask me your question. Answers will be limited to 30 tokens")

    prompt = "You are a basketball specialist. If a question is not related to basketball answer 'This is a non-basketball question'. Limit your answer to 30 tokens if possible"

    if input_txt != "":
        # st.write("You entered:", input_txt)
        prompt += input_txt

        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=30)
        # Print answer to the screen
        st.write(response["choices"][0]["text"])

    return

if __name__ == "__main__":
    main()
