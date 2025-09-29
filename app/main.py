from fastapi import FastAPI
from app.api.endpoints import router as api_router
import uvicorn

app = FastAPI(
    title="代码分析 AI Agent",
    description="接收代码和需求描述，分析代码并生成结构化报告",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "代码分析 AI Agent 服务已启动", "docs": "/docs"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)