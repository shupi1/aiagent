from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import router as api_router
import uvicorn

app = FastAPI(
    title="代码分析 AI Agent",
    description="接收代码和需求描述，分析代码并生成结构化报告",
    version="1.0.0"
)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(api_router, prefix="/api")

@app.get("/api")
async def root():
    return {"message": "代码分析 AI Agent 服务已启动", "docs": "/docs"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)