# 鲍鼎丞+229050209
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
        print(f"API调用错误: {e}")
        return None

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
    for path in file_paths:
        text = read_text_from_file(path)
        if text:
            summary = get_summary(text)
            summaries[path] = summary
    return summaries

# Test the function
sample_text = """
在当今快速发展的科技时代，人工智能（AI）正在逐渐改变我们的生活方式。无论是在医疗、教育还是交通领域，AI的应用都显得尤为重要。在医疗方面，AI可以帮助医生进行疾病的早期诊断，提高治疗效果。在教育领域，个性化学习平台利用AI来为学生提供量身定制的学习方案。而在交通领域，自动驾驶技术正在逐步成熟，有望提高道路安全性并减少交通拥堵。然而，随着AI的普及，伦理和隐私问题也愈发引起人们的关注。我们需要在推动技术发展的同时，确保人类的基本权益得到保护。
"""
summary = get_summary(sample_text)
print("Summary:", summary)

# Example of summarizing multiple files
file_paths = ['text1.txt', 'text2.txt']
summaries = summarize_multiple_texts(file_paths)
for path, summary in summaries.items():
    print(f"Summary for {path}: {summary}")
