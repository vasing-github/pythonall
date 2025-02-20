import os
import subprocess
import sys
from pathlib import Path
import platform


def get_libreoffice_path():
    """跨平台获取LibreOffice路径（支持环境变量覆盖）"""
    # 优先级1：环境变量指定
    env_path = os.getenv("LIBREOFFICE_PATH")
    if env_path and Path(env_path).exists():
        return env_path

    # 优先级2：平台自动检测
    search_paths = []
    if platform.system() == 'Windows':
        search_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"E:\soft3\libreoffice\program\soffice.exe"
        ]
    else:  # Linux/Unix-like
        search_paths = [
            "/usr/bin/libreoffice",  # Debian/Ubuntu
            "/usr/bin/soffice",  # CentOS/Docker常见路径
            "/app/bin/libreoffice",  # 容器常见安装路径
            "/usr/local/bin/libreoffice"
        ]

    # 尝试通过which命令查找（仅Unix-like系统）
    if platform.system() != 'Windows':
        try:
            which_path = subprocess.check_output(["which", "libreoffice"]).decode().strip()
            if which_path:
                search_paths.insert(0, which_path)
        except Exception:
            pass

    for path in search_paths:
        if Path(path).exists():
            return path

    raise FileNotFoundError(
        f"未找到LibreOffice，请确认已安装并添加到系统路径\n"
        f"可尝试以下方法：\n"
        f"1. 设置环境变量 LIBREOFFICE_PATH\n"
        f"2. 检查安装路径是否在以下列表中：{search_paths}"
    )


def doc_to_docx(file_path):
    """改进后的转换函数"""
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        raise FileNotFoundError(f"输入文件不存在: {file_path}")

    output_dir = file_path.parent
    output_path = file_path.with_suffix('.docx')

    command = [
        get_libreoffice_path(),
        "--headless",
        "--convert-to", "docx:MS Word 2007 XML",
        "--outdir", str(output_dir),
        str(file_path)
    ]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
            check=True
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"文档转换超时：{file_path.name}（超过120秒）")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8', errors='ignore')
        raise RuntimeError(f"转换失败[{e.returncode}]: {error_msg}")

    if not output_path.exists():
        available_files = "\n".join([f.name for f in output_dir.iterdir()])
        raise FileNotFoundError(
            f"输出文件未生成，目录中存在：\n{available_files}"
        )
    print(f"[调试] 转换输出目录: {output_dir}")
    print(f"[调试] 预期输出路径: {output_path}")
    return str(output_path)


if __name__ == '__main__':
    # 示例用法
    current_dir = Path(__file__).parent
    test_file = current_dir / "test.doc"

    try:
        output = doc_to_docx(test_file)
        print(f"转换成功：{output}")
    except Exception as e:
        print(f"错误发生：{str(e)}")
        sys.exit(1)
