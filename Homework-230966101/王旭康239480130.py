import os
from openai import OpenAI

api_key = ""
base_url = "https://api.deepseek.com/v1"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
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
        return f"Error: {e}"

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def summarize_multiple_texts(texts):
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# 指定文件路径
file_path = r"C:\Users\dell\Desktop\111.txt"

# 读取文件内容
file_content = read_text_from_file(file_path)
if isinstance(file_content, str) and not file_content.startswith("Error"):
    summary_from_file = get_summary(file_content)
    print("Summary from file:", summary_from_file)
else:
    print(file_content)
