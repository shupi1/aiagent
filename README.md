# AI Code Analysis Agent

这是一个AI驱动的代码分析Agent，能够接收代码和需求描述，分析代码并输出结构化的分析报告。

## 功能特点

- 接收多部分表单数据（multipart/form-data）请求
- 分析上传的代码文件，提取函数和类定义
- 将需求描述中的功能与代码实现进行匹配
- 生成结构化的JSON格式分析报告
- 提供执行计划建议
- 可选功能：生成功能验证测试代码

## 技术栈

- Python 3.9
- FastAPI
- NLTK (自然语言处理)
- Docker (容器化)

## 使用方法

### 方法一：使用Docker（推荐）

1. 构建Docker镜像：
   ```bash
   docker build -t ai-code-agent .
   ```

2. 运行Docker容器：
   ```bash
   docker run -p 8000:8000 ai-code-agent
   ```

### 方法二：直接运行

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 下载NLTK资源：
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

3. 启动应用：
   ```bash
   python main.py
   ```

## API使用

应用启动后，可以通过以下方式访问API：

- API文档：http://localhost:8000/docs
- ReDoc文档：http://localhost:8000/redoc

### 分析代码API

**URL**: `/analyze`
**方法**: `POST`
**内容类型**: `multipart/form-data`

**参数**:
- `problem_description` (form field): 项目功能的自然语言描述
- `code_zip` (file): 包含项目完整源代码的zip压缩文件

**响应示例**:
```json
{
  "feature_analysis": [
    {
      "feature_description": "实现用户注册功能",
      "implementation_location": [
        {
          "file": "src/users/register.py",
          "function": "register_user",
          "lines": "10-35"
        }
      ]
    }
  ],
  "execution_plan_suggestion": "要执行此项目，应首先执行 `pip install -r requirements.txt` 安装依赖，然后执行 `python main.py` 来启动服务。"
}
```

## 项目结构

- `main.py`: FastAPI应用主入口
- `code_analyzer.py`: 代码分析核心模块
- `requirements.txt`: Python依赖列表
- `Dockerfile`: Docker构建文件
- `README.md`: 项目说明文档

## 注意事项

1. 目前的代码分析基于关键词匹配，可能需要根据实际项目调整匹配算法
2. 对于复杂的代码库，分析准确性可能会受到限制
3. 功能验证部分当前只是生成测试模板，需要根据实际项目进行完善

## 扩展建议

1. 集成更高级的代码分析工具，如AST解析器针对不同语言
2. 使用机器学习模型提高功能与代码的匹配准确性
3. 实现自动化测试执行功能
4. 添加代码质量分析和安全漏洞检测功能