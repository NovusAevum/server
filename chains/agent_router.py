def route_objective(content):
    if "optimize" in content.lower():
        return {"agent": "Optimizer", "action": "Optimize code base."}
    elif "analyze" in content.lower():
        return {"agent": "Analyst", "action": "Run analysis and report insights."}
    else:
        return {"agent": "Strategist", "action": "Define system-level strategy."}
