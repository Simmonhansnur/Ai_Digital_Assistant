import json
import re

def execute_plan(plan):

    results = []

    # extract JSON from LLM output
    json_match = re.search(r'\[.*\]', plan, re.DOTALL)

    if not json_match:
        return {"error": "No JSON plan found from planner"}

    json_string = json_match.group()

    try:
        tasks = json.loads(json_string)
    except:
        return {"error": "Planner returned invalid JSON"}

    for task in tasks:

        agent = task.get("agent")
        description = task.get("task")

        result = {
            "agent": agent,
            "task": description,
            "result": f"{agent} executed task: {description}"
        }

        results.append(result)

    return results