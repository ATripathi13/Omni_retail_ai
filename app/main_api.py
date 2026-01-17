from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.orchestrator.orchestrator import Orchestrator
from app.core.logger import log
import uvicorn
import os
import time
import uuid

app = FastAPI(
    title="Omni-Retail AI Orchestrator",
    description="API Gateway for Multi-Agent Retail System",
    version="1.0.0"
)

# Initialize Orchestrator (Singleton-ish for this demo)
orchestrator = Orchestrator()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    plan: list
    results: list

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    with log.contextualize(request_id=request_id):
        log.info(f"Request started: {request.method} {request.url}")
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            response.headers["X-Process-Time"] = str(process_time)
            response.headers["X-Request-ID"] = request_id
            log.info(f"Request completed: {response.status_code} - Duration: {process_time:.4f}s")
            return response
        except Exception as e:
            log.error(f"Request failed: {str(e)}")
            raise e

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "omni-retail-ai"}

@app.post("/api/v1/chat") 
def chat(request: ChatRequest):
    try:
        log.info(f"Received query: {request.query}")
        plan = orchestrator.plan_task(request.query)
        if not plan:
            log.error("Failed to generate a plan")
            raise HTTPException(status_code=500, detail="Failed to generate a plan.")
        
        results = orchestrator.execute_plan(plan)
        return {
            "query": request.query,
            "plan": plan,
            "results": results
        }
    except Exception as e:
        log.error(f"Chat Endpoint Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
