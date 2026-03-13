from tools.web_search import search_web
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def research_agent(query):

    search_results = search_web(query)
    print("SEARCH RESULTS:", search_results)

    context = ""

    for r in search_results:
        context += f"{r['title']} - {r['snippet']}\n"

    prompt = f"""
Summarize the following research findings.

Research topic:
{query}

Sources:
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    summary = response.choices[0].message.content

    return {
        "query": query,
        "summary": summary,
        "sources": search_results
    }