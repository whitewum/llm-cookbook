# yuwenjie + 229050632
import os
from openai import OpenAI

client = OpenAI(
  api_key="your-api-key", # 提交时删除你的key，避免泄露
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

# Test the function
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

# TODO: 实现多个文本的摘要功能
def summarize_multiple_texts(file_paths):
    summaries = []
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            if summary:
                summaries.append(summary)
    return summaries

# TODO: 读取文件并生成多个文本的摘要
file_paths = ["path_to_your_file1.txt", "path_to_your_file2.txt"]
summaries = summarize_multiple_texts(file_paths)
for i, summary in enumerate(summaries):
    print(f"Summary {i+1}:", summary)
