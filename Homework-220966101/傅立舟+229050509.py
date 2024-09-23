# 傅立舟 + 229050509
import os
from openai import OpenAI

client = OpenAI(
  api_key="9", 
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
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API 调用失败: {e}")
        return None

# Test the function
sample_text = """
[一只山羊和一只狐狸住在山上。狐狸总想吃掉山羊，山羊整天担惊受怕。有一日，山羊去山下，一不小心掉进了一口井里。狐狸看见了，得意地说：“哈哈！山羊兄弟，你怎么在这里？
这井里的水是不是很甜呀？”山羊回答说：“你说的没错，这井里的水的确很甜。”]
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

def summarize_files(file_paths):
    summaries = []
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = get_summary(text)
            summaries.append(summary)
        else:
            summaries.append(f"错误：无法生成摘要")
    return summaries

# 示例用法
file_paths = ["file1.txt", "file2.txt"]
summaries = summarize_files(file_paths)
for i, summary in enumerate(summaries):
    print(f"{file_paths[i]} 的摘要：\n{summary}\n")
