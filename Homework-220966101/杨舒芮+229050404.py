# 杨舒芮+229050404
import os
from openai import OpenAI

client = OpenAI(
  api_key="your-api-key", # 提交时删除你的key，避免泄露
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    try:
        prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        # TODO Implement error handling for API calls
        print(f"发生了错误: {e}")

# Test the function
sample_text = """

"""

summary = get_summary(sample_text)
print("Summary:", summary)

# TODO 实现一个从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None



# TODO: Add functionality to summarize multiple texts
def summarize_texts(file_paths):
    summaries = {}
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            summary = get_summary(text) or "没有结果"
        summaries[file_path] = summary
    return summaries

file_paths = [
    "/a.txt",
    "/b.txt",
    "/c.txt"
]


summaries = summarize_texts(file_paths)


for file_path, summary in summaries.items():
    print(f"{file_path} 的结果是: {summary}")
