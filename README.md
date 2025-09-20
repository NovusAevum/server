# INTELSPHERE LangChain Agent Server

This FastAPI backend reads MCP rules, session notes, and current objectives to route tasks to intelligent agents: Strategist, Optimizer, Analyst.

## Endpoints
- POST `/route` → Route objective to correct agent
- GET `/memory/recent` → Retrieve recent session notes

## Run the Server
```bash
uvicorn main:app --reload
```
