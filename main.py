from fastapi import FastAPI, Request
from pydantic import BaseModel
from chains.agent_router import route_objective
from memory.session_log import recall_recent_sessions

app = FastAPI()

class ObjectiveRequest(BaseModel):
    content: str

@app.post("/route")
def route_agent(request: ObjectiveRequest):
    return route_objective(request.content)

@app.get("/memory/recent")
def get_memory():
    return recall_recent_sessions()
