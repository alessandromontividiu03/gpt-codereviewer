import streamlit as st
from openai.error import OpenAIError
from reviewer.git_handler import get_code_changes
from reviewer.reviewer_llm import review

st.set_page_config(page_title="CodeReviewerGPT", page_icon="🤖", layout="wide")
st.header("🤖 CodeReviewerGPT")

openai_api_key = st.text_input("Enter your OpenAI API key (We DO NOT store it or any other data)", type="password")
query = st.text_area("Enter a Pull Request or Commit Url", value="https://github.com/codelittinc/tasketeer-nlp-processor/pull/32")

button = st.button("Review Code")
if button or st.session_state.get("submit"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key!")
    elif not query:
        st.error("Please enter a pull request, branch or git commit URL!")
    else:
        st.session_state["submit"] = True
        # Output Columns
        code_changes = get_code_changes(query)
        if not code_changes.startswith("diff"):
            st.error("Error! Please enter a valid pull request or git commit URL!")

        try:
            code_review_comments = review(code_changes, openai_api_key)
            st.markdown("#### Code Review Comments")
            st.markdown(code_review_comments)
        except OpenAIError as e:
            st.error(e._message)