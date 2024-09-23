# 董政儒 + 229100226
import os
from openai import OpenAI

client = OpenAI(
  api_key="sk-Guess-My-Api-Key", # 提交时删除你的key，避免泄露
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
杭州电子科技大学信息工程学院是经浙江省人民政府批准建立的民办全日制普通本科独立学院，是浙江省应用型建设试点本科院校。
杭州电子科技大学信息工程学院是1999年由杭州电子科技大学举办、经浙江省人民政府批准、2004年由教育部确认的第一批独立学院。2012年7月杭州电子科技大学与临安市政府签署合作协议，共建杭州电子科技大学信息工程学院。2019年学院正式通过独立学院规范设置省级验收。
据2024年5月学校官网数据，学校占地面积500亩，建筑面积17.48万平方米；设有教学院部8个，开办本科专业26个；有教职员工521人（不含外聘教师），在校全日制本科生10488人。
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
file_paths = ["/workspaces/llm-cookbook/Homework-220966101/text1.txt", "/workspaces/llm-cookbook/Homework-220966101/text2.txt", "/workspaces/llm-cookbook/Homework-220966101/text3.txt"]
summaries = summarize_texts(file_paths)

# 输出每个txt的摘要
for file_path, summary in summaries.items():
    print(f"{file_path} 的摘要是: {summary}")
