import streamlit as st
from openai.error import OpenAIError

def clear_submit():
    st.session_state["submit"] = False


st.set_page_config(page_title="CodeReviewerGPT", page_icon="🤖", layout="wide")
st.header("🤖 CodeReviewerGPT")

openai_api_key = st.text_input("Enter your OpenAI API key (We DO NOT store it or any other data)", type="password")
query = st.text_area("Enter a Pull Request, Commit or Branch Url", on_change=clear_submit)

button = st.button("Review Code")
if button or st.session_state.get("submit"):
    if not st.session_state.get("api_key_configured"):
        st.error("Please configure your OpenAI API key!")
    elif not query:
        st.error("Please enter a pull request, branch or git commit URL!")
    else:
        st.session_state["submit"] = True
        # Output Columns
        answer_col = st.columns(1)
        #sources = search_docs(index, query)

        try:
            answer = None #get_answer(sources, query)
            #if not show_all_chunks:
                # Get the sources for the answer
                #sources = get_sources(answer, sources)

            with answer_col:
                st.markdown("#### Answer")
                st.markdown("")
        except OpenAIError as e:
            st.error(e._message)