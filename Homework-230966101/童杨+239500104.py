#童杨 + 239500104

import os
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",  # 提交时删除你的key，避免泄露
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
        print(f"API 调用错误: {e}")
        return None

# 测试函数
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# TODO: 实现一个从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# TODO: 添加功能以总结多个文本
def summarize_multiple_texts(file_paths):
    summaries = {}
    for path in file_paths:
        text = read_text_from_file(path)
        if text:
            summary = get_summary(text)
            summaries[path] = summary
    return summaries

# 示例调用
file_list = ["text1.txt", "text2.txt"]  # 请替换为实际文件名
summaries = summarize_multiple_texts(file_list)
for file, summary in summaries.items():
    print(f"Summary for {file}:\n{summary}\n")
