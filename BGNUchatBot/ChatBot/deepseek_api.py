import requests
import json

OPENROUTER_API_KEY = "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"  # use your actual working key

def build_prompt(question, context):
    return f"""
You are a chatbot for Baba Guru Nanak University, Nankana Sahib. Use the following information to answer the user's query:

**Context**:
{context}

**User Query**:
{question}

**Instructions**:
- Answer clearly without adding commentary or reasoning.
- If it's a greeting like 'hi' or 'hello', reply: "Hello! Welcome to Baba Guru Nanak University, Nankana Sahib. How can I assist you today regarding admissions or university information?"
- If info isn't available, reply: "Sorry, I don’t have enough information to answer. Please contact the university for assistance.
- Do not include any introductory phrases like 'Based on the context' or 'Therefore'
- Provide a detailed answer hvaing sufficiant information to address the user's query.
- Do not mention any section number in the answer."
"""

def ask_deepseek(question, context):
    prompt = build_prompt(question, context)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
