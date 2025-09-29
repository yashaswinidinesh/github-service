from fastapi import FastAPI
from routers.handle_routes import router as issues_router

app = FastAPI()
app.include_router(issues_router)
# --- Health check ---
@app.get("/healthz", tags=["system"])
async def healthz():
    return {"status": "ok"}

