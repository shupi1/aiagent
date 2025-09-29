import zipfile
import os
import tempfile
from typing import Dict, List


class FileProcessor:
    @staticmethod
    def extract_zip(zip_file_path: str) -> str:
        """解压 ZIP 文件到临时目录并返回目录路径"""
        temp_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        return temp_dir

    @staticmethod
    def read_code_files(directory: str) -> Dict[str, str]:
        """读取目录中的代码文件内容"""
        code_files = {}
        code_extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.cs', '.go', '.rb', '.php'}

        for root, _, files in os.walk(directory):
            for file in files:
                file_ext = os.path.splitext(file)[1]
                if file_ext in code_extensions:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory)

                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            code_files[relative_path] = f.read()
                    except UnicodeDecodeError:
                        # 处理二进制文件或无法解码的文件
                        continue

        return code_files

    @staticmethod
    def get_project_structure(directory: str) -> List[str]:
        """获取项目结构"""
        structure = []
        for root, dirs, files in os.walk(directory):
            relative_root = os.path.relpath(root, directory)
            if relative_root == '.':
                relative_root = ''

            for dir in dirs:
                structure.append(f"dir: {os.path.join(relative_root, dir)}")

            for file in files:
                structure.append(f"file: {os.path.join(relative_root, file)}")

        return structure