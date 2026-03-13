from fastapi import FastAPI
from schemas.request_models import UserRequest
from agents.planner_agent import planner_agent

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Digital Assistant Backend Running"}


@app.post("/api/request")
async def handle_request(request: UserRequest):

    user_message = request.message

    plan = planner_agent(user_message)

    return {
        "user_request": user_message,
        "execution_plan": plan
    }