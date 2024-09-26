#王树婷+239200205
import os
from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI(
    api_key="",  # 提交时请确保安全使用您的API密钥
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API调用出错: {e}")
        return None

# 从文件中读取文本
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None


def summarize_multiple_texts(file_paths):
    summaries = {}
    for path in file_paths:
        text = read_text_from_file(path)
        if text:  # 如果成功读取文本
            summary = get_summary(text)
            summaries[path] = summary
    return summaries



    sample_text = """
    [我是一个计算机的大学生，我在学习大语言模型应用开发。]
    """

  
    summary = get_summary(sample_text)
    print("摘要:", summary)

    # 从多个文件总结文本
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]  # 在这里添加您的文件路径
    summaries = summarize_multiple_texts(file_paths)
    
    for file, summary in summaries.items():
        print(f"{file} 的摘要: {summary}")
