from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def planner_agent(user_message: str):

    planner_prompt = f"""
You are an AI planning agent.

Your job is to break the user request into subtasks.

Available agents:
- document_agent (handles document summarization and document Q&A)
- research_agent (performs web research)
- task_agent (creates task lists)

Return the result as JSON list.

User request:
{user_message}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": planner_prompt}
        ],
        temperature=0
    )

    plan = response.choices[0].message.content

    return plan