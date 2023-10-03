import streamlit as st
import openai 


default_prompt = "Highlight any errors in the code and provide suggestions for improving the code. \
                  Also implement those suggestions and provide revised code."

default_prompt = '''
{
    "code": "<<YOUR CODE HERE>>",
    "critical_errors": [
        {
            "error_id": 1,
            "explanation": "Explanation for critical error 1"
        },
        {
            "error_id": 2,
            "explanation": "Explanation for critical error 2"
        }
    ]
}
'''

def generate_text(prompt, api_key):
    openai.api_key = api_key

    #full_prompt = default_prompt + "\n" + prompt
    full_prompt = default_prompt.replace("<<YOUR CODE HERE>>", prompt)

    try: 
        response = openai.Completion.create(
            engine = "gpt-3.5-turbo-instruct",
            prompt = full_prompt,
            max_tokens = 3700
        )
        return response.choices[0].text.strip()

    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API Error: {str(e)}")
        return None

st.title("Suggestions for Improving Your Code")

user_input = st.text_area("Enter your code:", height = 200)

api_key = st.session_state.get("api_key", "")

if not api_key:
    api_key = st.text_input("Enter your OpenAI API key", type = "password")
    st.session_state.api_key = api_key  # Cache the API key

if st.button("Generate Suggestions for Improvement") and api_key:
    with st.spinner("Generating..."):
        generated_text = generate_text(user_input, api_key)
    st.success("Suggested Improvements Have Been Generated!")
    st.write("Suggested Improvements:")
    st.write(generated_text)
