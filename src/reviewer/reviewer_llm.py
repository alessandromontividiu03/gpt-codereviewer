from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

PROMPT = """
Your job is to review the git code changes and come up with suggestions of improvements and fixes.
You must take into accout best practices, security, performance, and readability.

Provide the code review response in MARKDOWN format, in the following format:
```format
    filename: 'src/reviewer/reviewer_llm.py',
    line: 1,
    message: 'This is a code review message',
``` 

GIT CODE CHANGES: {code_changes}

YOUR CODE REVIEW HERE:

"""

def review(input, api_key):

    # read the prompt template and set the input variables
    prompt = PromptTemplate(template=PROMPT, input_variables=["code_changes"])
    llm = OpenAI(
        model_name='gpt-3.5-turbo',
        temperature=.7,
        max_tokens=3000,
        openai_api_key=api_key,
    )
    
    # split the input text into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap  = 100,
    )
    texts = text_splitter.create_documents([input])
    
    # run the chain on each chunk
    response = []
    for text in texts:
        final_prompt = prompt.format(code_changes=text)
        code_review = llm(final_prompt)
        response.append(code_review)
    
    return " ".join(response)
