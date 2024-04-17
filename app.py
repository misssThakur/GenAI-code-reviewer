from openai import OpenAI
import streamlit as st

# Read the API Key and Setup an OpenAI Client
f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

#########################################################################################
st.snow()
st.title("👩‍💻Code Reviewer")
st.subheader("Finds bugs in your code and returns back the corrrected code for you.")
##########################################################################################

# Take User's Input
prompt = st.text_box("Enter your Code here!")

# If the button is clicked, generate responses
if st.button("Generate") == True:
    st.balloons()
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0613",
      messages=[
        {"role": "system", "content": "You are a code reviewer expertise . Thus, find bugs, errors in the given code and return back the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )

    # Print the response on Web App
    st.write(response.choices[0].message.content)