import json
import re

from agents.research_agent import research_agent


def execute_plan(plan):

    results = []

    json_match = re.search(r'\[.*\]', plan, re.DOTALL)

    if not json_match:
        return {"error": "No JSON plan found"}

    json_string = json_match.group()

    try:
        tasks = json.loads(json_string)
    except:
        return {"error": "Planner returned invalid JSON"}

    for task in tasks:

        agent = task.get("agent")
        description = task.get("task")

        if agent == "research_agent":

            agent_result = research_agent(description)

        else:

            agent_result = {
                "message": f"{agent} not implemented yet"
            }

        results.append({
            "agent": agent,
            "task": description,
            "result": agent_result
        })

    return results