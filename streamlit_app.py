import streamlit as st
import openai 
import secrets


default_prompt = "Highlight any errors in the code and provide suggestions for improving the code. \
                  Also implement those suggestions and provide revised code."

def generate_text(prompt, api_key):
    openai.api_key = api_key
    full_prompt = default_prompt + user_input
    response = openai.Completion.create(
        engine = "davinci-codex",
        prompt = full_prompt,
        max_tokens = 4096
    )
    return response.choices[0].text.strip()

st.title("Suggestions for Improving Your Code")

user_input = st.text_area("Enter your code:", height = 200)

api_key = st.session_state.get("api_key", "")

if not api_key:
    api_key = st.text_input("Enter your OpenAI API key", type = "password")
    st.session_state.api_key = api_key  # Cache the API key

if st.button("Generate Suggestions for Improvement") and api_key:
    with st.spinner("Generating..."):
        generated_text = generate_text(user_input, api_key)
    st.success("Text Generated!")
    st.write("Generated Text:")
    st.write(generated_text)
