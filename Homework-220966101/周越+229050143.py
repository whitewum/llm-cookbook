# 周越+229050143
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

# TODO: Implement error handling for API calls
def safe_get_summary(text):
    try:
        return get_summary(text)
    except Exception as e:
        print(f"错误：调用 API 时出现问题 - {e}")
        return None

# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = safe_get_summary(text)
        if summary:
            summaries.append(summary)
    return summaries

# 示例用法
sample_texts = [
    "这是第一段需要总结的文本。",
    "这是第二段需要总结的文本。",
]

summaries = summarize_multiple_texts(sample_texts)
for idx, summary in enumerate(summaries):
    print(f"总结 {idx + 1}: {summary}")
