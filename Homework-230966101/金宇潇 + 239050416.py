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
        print(f"错误：API 调用失败 - {e}")
        return None

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# TODO: Implement a function to read text from a file
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

# TODO: Add functionality to summarize multiple texts
def summarize_texts_from_files(file_paths):
    summaries = {}
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            if summary:
                summaries[file_path] = summary
    return summaries

# 测试函数
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  # 文件路径列表
summaries = summarize_texts_from_files(file_paths)

for file_path, summary in summaries.items():
    print(f"文件 '{file_path}' 的摘要:")
    print(summary)
