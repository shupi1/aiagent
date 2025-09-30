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
   git clone https://github.com/shupi1/aiagent0.git
   cd aiagent0

2. 配置环境变量

```bash
cp .env.example .env
```

编辑 `.env` 文件，添加你的 OpenAI API 密钥。

3. 构建并启动 Docker 容器

```bash
docker build -t aiagent0 .
docker run -p 8000:8000 --env-file .env aiagent0
```

4. 访问服务

- API 文档: http://localhost:8000/docs
- 分析接口: http://localhost:8000/api/analyze

### 示例用法

```bash
curl -X POST "http://localhost:8000/api/analyze" ^
  -H "Content-Type: multipart/form-data" ^
  -F "problem_description=对文件进行切分" ^
  -F "code_zip=@./D:/prj/aiagent/test_code.zip"
```
