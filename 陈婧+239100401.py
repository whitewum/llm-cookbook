#陈婧 239100401
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
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

# 实现一个从文件读取文本的函数
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError:
        print(f"错误：无法读取文件 '{file_path}'。")
    return None

# Implement error handling for API calls
def handle_api_call_error(response):
    if response.status_code != 200:
        print(f"API调用错误: {response.status_code} - {response.reason}")
        return None
    return response.json()

# Add functionality to summarize multiple texts
def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# Test reading text from a file
file_text = read_text_from_file('sample.txt')
if file_text:
    print("从文件读取的文本：", file_text)

# Test summarizing multiple texts
multiple_texts = ["Text 1", "Text 2", "Text 3"]
multiple_summaries = summarize_multiple_texts(multiple_texts)
print("Multiple Summaries:", multiple_summaries)
