import os
from openai import OpenAI

client = OpenAI(
  api_key="", # 提交时删除你的key，避免泄露
  base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    print("我在思考...")
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
        # 处理API调用时可能会出现的异常
        print(f"调用API时发生错误，错误信息是: {e}")

# Test the function
sample_text = """
[其实你们可以搞个共享相册，然后把要的人拉进去]
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
    # 为每个文本都生成自己的摘要信息
    summaries = {}
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text is not None:
            summary = get_summary(text)
            if summary:
                summaries[file_path] = summary
            else:
                summaries[file_path] = "没有摘要！"
        else:
            summaries[file_path] = "文本读取失败！"
    return summaries

# 多个txt的路径列表
file_paths = ["1.txt", "2.txt"]
summaries = summarize_texts(file_paths)

# 输出每个txt的摘要
for file_path, summary in summaries.items():
    print(f"{file_path} 的摘要是: {summary}")
