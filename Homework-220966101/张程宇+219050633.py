import os
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    prompt = f"请总结以下文本，用3-5句话概括:\n\n{text}"
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
        print(f"API 调用时出错: {e}")
        return None

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
        return None

def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# 示例使用
file_path = "example.txt"
sample_text = read_text_from_file(file_path)
if sample_text:
    summary = get_summary(sample_text)
    print("总结:", summary)

texts = ["长文本 1...", "长文本 2...", "长文本 3..."]
summaries = summarize_multiple_texts(texts)
for idx, summary in enumerate(summaries, 1):
    print(f"总结 {idx}:", summary)
