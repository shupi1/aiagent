import os
import json
from typing import Dict, List, Optional
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY 环境变量未设置")

    def analyze_code_for_features(self, problem_description: str, code_summary: str, project_structure: str) -> Dict:
        """
        使用 LLM 分析代码与需求的匹配度
        """
        prompt = f"""
        你是一位专业的代码分析专家。请分析以下代码是否实现了需求中描述的功能，并指出具体实现位置。

        需求描述:
        {problem_description}

        项目结构:
        {project_structure}

        代码摘要:
        {code_summary}

        请按照以下JSON格式输出分析结果，确保格式正确：
        {{
            "feature_analysis": [
                {{
                    "feature_description": "实现的功能描述",
                    "implementation_location": [
                        {{
                            "file": "文件路径",
                            "function": "函数或类名",
                            "lines": "行号范围，如 13-16"
                        }}
                    ]
                }}
            ],
            "execution_plan_suggestion": "执行项目的建议步骤"
        }}

        注意事项:
        1. 确保识别需求中提到的所有功能点
        2. 准确指出每个功能在代码中的实现位置
        3. 执行建议应包括必要的依赖安装和启动命令
        4. 只返回JSON，不要添加其他解释文字
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位专业的代码分析专家，擅长分析各种编程语言的代码结构和功能实现。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )

        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            raise ValueError("LLM 返回的结果不是有效的 JSON")

    def generate_test_code(self, problem_description: str, code_summary: str, analysis_result: Dict) -> Optional[str]:
        """
        为分析结果生成测试代码
        """
        prompt = f"""
        你是一位专业的测试工程师。请根据以下需求、代码摘要和分析结果，生成可执行的单元测试代码。

        需求描述:
        {problem_description}

        代码摘要:
        {code_summary}

        分析结果:
        {json.dumps(analysis_result, indent=2)}

        请生成能验证所有功能点的测试代码。测试代码应：
        1. 针对每个功能点创建测试用例
        2. 包含必要的依赖导入
        3. 可直接执行，不需要额外修改
        4. 输出清晰的测试结果

        根据项目类型选择合适的测试框架和语言。
        只返回测试代码，不要添加其他解释文字。
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位专业的测试工程师，擅长为各种项目编写单元测试。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content
# Large Language Model service