# 朱世耀 + 229490340
import os
from openai import OpenAI

client = OpenAI(
  api_key="sk-", # 提交时删除你的key，避免泄露
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
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        # TODO Implement error handling for API calls
        # 处理API调用时可能会出现的异常
        print(f"调用API时发生错误，错误信息是: {e}")

# Test the function
sample_text = """
[在过去的一学年中，我始终保持着对知识的渴望和对学术的严谨态度，勤奋学习，刻苦钻研。通过不懈努力，我的学习成绩始终名列前茅，多次获得课程高分，并在XX学科竞赛中荣获一等奖，这些成绩不仅是对我学习成果的肯定，更是激励我不断前进的动力。我深知，学习是一场没有终点的马拉松，我将继续以优异的成绩和不懈的努力，追求卓越，攀登学术高峰。
除了专业学习外，我还积极参与各类课外活动和社会实践，努力提升自己的综合素质。作为学生会XX部部长，我成功策划并组织了多场校园活动，不仅锻炼了我的组织协调能力，还培养了我的团队合作精神和领导力。同时，我还积极参加志愿服务活动，用实际行动践行社会责任，传递正能量。这些经历让我更加自信、成熟，也为我未来的发展奠定了坚实的基础。
在学术研究中，我勇于探索未知领域，敢于提出新观点、新方法。在导师的指导下，我参与了一项关于XX领域的研究项目，通过查阅大量文献、设计实验方案、收集并分析数据，最终撰写了一篇高质量的学术论文并成功发表。这一过程中，我不仅学到了许多专业知识，更培养了我的创新思维和科研能力。我相信，这些宝贵的经验将对我未来的学术生涯产生深远的影响。
]
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
file_paths = ["text1.txt", "text2.txt", "text3.txt"]
summaries = summarize_texts(file_paths)

# 输出每个txt的摘要
for file_path, summary in summaries.items():
    print(f"{file_path} 的摘要是: {summary}")
