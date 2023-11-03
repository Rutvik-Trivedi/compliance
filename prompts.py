from langchain.prompts import ChatPromptTemplate

template = """The context provided is from a compliance policy. Given the Input, Return the non-compliant results from the input as your response:
Context: {context}

Input: {question}
"""
prompt = ChatPromptTemplate.from_template(template)