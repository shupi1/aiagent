# 代码分析 AI Agent

这是一个能够接收代码和需求描述，分析代码并输出结构化报告的 AI Agent。

## 功能

- 接收包含源代码的 ZIP 文件和功能需求描述
- 分析代码结构和功能实现
- 生成包含功能分析和执行建议的 JSON 报告
- 生成验证功能的测试代码（加分项）

## 快速开始

### 前提条件

- Docker
- OpenAI API 密钥（用于代码分析）

### 使用 Docker 运行

1. 克隆仓库
   ```bash
   git clone https://github.com/shupi1/aiagent.git
   cd aiagent# AI Agent Project
2. 配置环境变量
bash
cp .env.example .env
### 编辑 .env 文件，添加你的 OpenAI API 密钥
3. 构建并启动 Docker 容器
bash
docker build -t aiagent .
docker run -p 8000:8000 --env-file .env aiagent
4. 访问服务
API 文档: http://localhost:8000/docs
分析接口: http://localhost:8000/api/analyze
This is the README file for the AI Agent project.
###Example usage:
```bash
    curl -X POST "http://localhost:8000/api/analyze" \
      -H "Content-Type: multipart/form-data" \
      -F "problem_description=实现一个简单的加法函数" \
      -F "code_zip=@./test_code.zip"