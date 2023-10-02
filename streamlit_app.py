import streamlit as st
import openai

def generate_text(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=100  # Adjust max tokens as needed
    )
    return response.choices[0].text.strip()

st.title("Suggestions for Improving Your Code")

default_prompt = "Highlight any errors in the code and provide suggestions for improving the code. Also implement those suggestions and provide revised code."
user_input = st.text_input("Enter your code", default_prompt)
st.write("You entered:", user_input)

api_key = st.text_input("Enter your OpenAI API key", type="password")
st.write("API Key entered:", api_key)

if st.button("Generate Text") and api_key:
    with st.spinner("Generating..."):
        generated_text = generate_text(user_input, api_key)
    st.success("Text Generated!")
    st.write("Generated Text:")
    st.write(generated_text)
