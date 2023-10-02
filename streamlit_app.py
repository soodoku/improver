import streamlit as st
import openai 
import secrets


default_prompt = "Highlight any errors in the code and provide suggestions for improving the code. \
                  Also implement those suggestions and provide revised code."

def generate_text(prompt, api_key):
    openai.api_key = api_key
    full_prompt = default_prompt + user_input
    response = openai.Completion.create(
        engine="davinci",
        prompt=full_prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@st.cache_data
def get_set_api_key(api_key=None):
    session_state = Server.get_current()._session_state
    if api_key:
        session_state.api_key = api_key
    return session_state.api_key

st.title("Suggestions for Improving Your Code")

user_input = st.text_area("Enter your code:", height=200)
st.write("You entered:", user_input)

api_key = st.text_input("Enter your OpenAI API key", type="password")

if api_key:
    st.session_state.api_key = api_key
st.write("API Key entered:", api_key)

# Retrieve the API key from the session
api_key = st.session_state.api_key

if st.button("Generate Suggestions for Improvement") and api_key:
    with st.spinner("Generating..."):
        generated_text = generate_text(user_input, api_key)
    st.success("Text Generated!")
    st.write("Generated Text:")
    st.write(generated_text)
