#吕政谕+239050625
import os
from openai import OpenAI

client = OpenAI(
  api_key="your-api-key", 
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
        print(f"错误：API 调用失败。详细信息：{e}")
        return None

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            if not text.strip():
                print(f"警告：文件 '{file_path}' 为空。")
                return None
            return text
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except IOError as e:
        print(f"错误：无法读取文件 '{file_path}'。详细信息：{e}")
    return None

def summarize_multiple_texts(file_paths):
    summaries = []
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            if summary:
                summaries.append(summary)
    return summaries


file_paths = ["file1.txt", "file2.txt", "file3.txt"]
summaries = summarize_multiple_texts(file_paths)
for i, summary in enumerate(summaries):
    print(f"文件 {file_paths[i]} 的摘要：\n{summary}\n")
