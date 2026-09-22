import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def generate_study_plan(user_request):

    api_key = st.secrets.get("OPENAI_API_KEY")

    if not api_key:
        return "OpenAI API key is not configured."

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=api_key
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an AI study planner. "
            "Create a simple and practical study plan for students."
        ),
        (
            "human",
            """Create a study plan for this student:

{request}

Include:
- Topics
- Time allocation
- Breaks
- Practice
- Revision
"""
        )
    ])

    chain = prompt | llm

    response = chain.invoke({
        "request": user_request
    })

    return response.content