# 吴康 + 219100330
import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-II",
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
        print(f"API调用错误: {e}")
        return None

# Test the function
sample_text = """
大宋回到i的滑坡的呼叫的设计哦怕大家里的卡洛夫斯卡fadjdalksjdlakdjad
"""

summary = get_summary(sample_text)
print("Summary:", summary)

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
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            summaries[file_path] = summary
    return summaries

# Example usage
file_paths = ["/workspaces/llm-cookbook/Homework-230966101/sample_text.txt", "text2.txt"]  # Replace with your file paths
summaries = summarize_multiple_texts(file_paths)
for path, summary in summaries.items():
    print(f"Summary for {path}:", summary)
