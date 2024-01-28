import streamlit as st

from text2code import Text2Code

# from getpass import getpass
# OPENAI_API_KEY = getpass()


st.set_page_config(layout="centered", page_icon=":shark:", page_title="Text2Code Demo")
st.title("Text2Code Demo")


# Description block
st.subheader("Description", divider="gray")
with st.expander("Click here for description"):
    description_text = """
    This is a demo for the Text2Code feature. It allows to generate code given users instructions.

    Current support: 
    - SDK feature: cleaning functions
    - language: React.

    Future support:
    - SDK feature: data handler functions
    - language: support other programming languages
    """
    st.markdown(description_text)


# Side bar block
with st.sidebar:
    OPENAI_API_KEY = st.text_input("Please provide your OpenAI api key", type="password")
    st.markdown("Get the api key [here](https://platform.openai.com/api-keys)")


# User input block
st.subheader("Your input", divider="gray")
with st.expander("explanation"):
    instruction_text = """
    Please provide below instructions and/or examples.

    Example:
    - instruction: Standardize phone numbers by removing leading double zeros.\\
    example: (001658345423, +491658345423), (001743456732, +491743456732)
    - instruction: Standardize the phone numbers. See examples below.\\
      example: (001658345423, +491658345423), (01743456732, +491743456732), (1845342361, +491845342361), (1743567891, +491743567891)
    - instruction: Standardize dates to dd.mm.yyyy format
    - instruction: Given a full address, keep only index
    """
    st.markdown(instruction_text)

col1, col2 = st.columns(2)

with col1:
    user_instruction = st.text_area("Instructions👇")
with col2:
    user_example = st.text_area("Examples👇")
user_input = {"user_instruction": user_instruction, "user_example": user_example}


# Get results block
if OPENAI_API_KEY:
    t2c = Text2Code(OPENAI_API_KEY)
    t2c.init_llm_chain()

if st.button("Generate code"):
    with st.spinner(text="Please wait...Generating the results."):
        try:
            result = t2c.generate_code(user_input)
        except Exception as e:
            error_message = str(e) + " -> OpenAI api key not found. Please enter your api key in the saide bar."
            print(error_message)
            raise type(e)(error_message).with_traceback(e.__traceback__)
        # result = """phoneNumber: (values) => {{ \n    values.map(([item, index]) => {{ \n        let phoneNumber = item; \n        if (/^[0]{{2}}/.test(phoneNumber)) {{ \n            phoneNumber = `+${{item.slice(2, item.length)}}`; \n        }} \n        return [ \n            {{ \n                value: phoneNumber, \n                info: [ \n                    {{ \n                        message: \'We have automatically transformed your input into the correct format by converting "00" to "+".\', \n                        level: "info", \n                    }}, \n                ], \n            }}, \n            index, \n        ]; \n    }}); \n}}"""

    tab1, tab2 = st.tabs(["React", "Angular"])

    with tab1:
        st.code(result, language="python")
