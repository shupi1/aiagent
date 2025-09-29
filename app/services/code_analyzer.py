import ast
from typing import Dict, List, Tuple
import os


class CodeAnalyzer:
    @staticmethod
    def analyze_python_code(code: str) -> List[Tuple[str, int, int]]:
        """分析 Python 代码，提取函数和类及其位置"""
        tree = ast.parse(code)
        functions = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno
                end_line = node.end_lineno
                functions.append((node.name, start_line, end_line))
            elif isinstance(node, ast.ClassDef):
                start_line = node.lineno
                end_line = node.end_lineno
                functions.append((f"Class: {node.name}", start_line, end_line))

        return functions

    @staticmethod
    def analyze_javascript_code(code: str) -> List[Tuple[str, int, int]]:
        """简单分析 JavaScript/TypeScript 代码，提取函数和类及其位置（简化版）"""
        lines = code.split('\n')
        functions = []

        for i, line in enumerate(lines, 1):
            stripped_line = line.strip()
            if stripped_line.startswith('function ') and '(' in stripped_line:
                func_name = stripped_line.split('function ')[1].split('(')[0].strip()
                functions.append((f"function {func_name}", i, i))  # 简化处理，只记录起始行
            elif stripped_line.startswith('class ') and '{' in stripped_line:
                class_name = stripped_line.split('class ')[1].split('{')[0].strip()
                functions.append((f"class {class_name}", i, i))  # 简化处理

        return functions

    @staticmethod
    def analyze_code_file(file_path: str, code: str) -> List[Tuple[str, int, int]]:
        """根据文件扩展名选择合适的分析器"""
        ext = os.path.splitext(file_path)[1].lower()

        if ext == '.py':
            return CodeAnalyzer.analyze_python_code(code)
        elif ext in ('.js', '.ts'):
            return CodeAnalyzer.analyze_javascript_code(code)
        else:
            # 对于其他类型的文件，我们只做简单处理
            return [("代码内容", 1, len(code.split('\n')))]

    @staticmethod
    def generate_code_summary(code_files: Dict[str, str]) -> str:
        """生成代码摘要，包含文件结构和主要函数"""
        summary = "项目代码摘要：\n\n"

        for file_path, code in code_files.items():
            summary += f"文件: {file_path}\n"
            functions = CodeAnalyzer.analyze_code_file(file_path, code)

            if functions:
                summary += "  主要函数/类:\n"
                for func_name, start_line, end_line in functions:
                    summary += f"    - {func_name} (行: {start_line}-{end_line})\n"
            else:
                summary += "  未识别到明显的函数或类定义\n"

            summary += "\n"

        return summary