# 黄孜帅 + 239050413
import os
from openai import OpenAI

client = OpenAI(
  api_key="ni mei you ？",
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
        print(f"API调用时发生错误: {e}")
        return "摘要生成失败。"

# Test the function
sample_text = """
[hello，world]
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

# TODO: 实现 API 调用的错误处理
def safe_get_summary(text):
    try:
        return get_summary(text)
    except Exception as e:
        print(f"调用API时出现错误: {e}")
        return "无法生成摘要，请检查输入或稍后重试。"

# TODO: 增加对多个文本的摘要功能
def summarize_multiple_texts(file_paths):
    summaries = {}
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = safe_get_summary(text)
            summaries[file_path] = summary
        else:
            summaries[file_path] = "无法读取文本或文本为空。"
    return summaries

# 示例：测试多个文件的摘要功能
file_list = ["/workspaces/llm-cookbook/Homework-230966101/蒋永琪+236050814.py", "/workspaces/llm-cookbook/Homework-230966101/1111.txt", "/workspaces/llm-cookbook/Homework-230966101/3333.txt"]  # 替换为你的文件路径
multiple_summaries = summarize_multiple_texts(file_list)
for file, summary in multiple_summaries.items():
    print(f"文件 '{file}' 的摘要：\n{summary}\n")
