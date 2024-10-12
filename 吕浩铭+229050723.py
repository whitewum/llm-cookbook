import os
from openai import OpenAI, AuthenticationError, APIError, PermissionDeniedError, RateLimitError

client = OpenAI(
    api_key="your api key",  # 提交时删除你的key，避免泄露
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    prompt = f"用三到五句话概括这段内容\n\n{text}"
    messages = [{"role": "user", "content": prompt}]
    response = None
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )

    except AuthenticationError:
        print("身份认证出错")
        return response
    except APIError:
        print("API错误")
        return response
    except PermissionDeniedError:
        print("权限错误")
        return response
    except Exception:
        print("非法请求错误")
        return response

    return response.choices[0].message.content


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


for p in ["./txt1.txt", "./txt2.txt", "./txt3.txt"]:
    text = read_text_from_file(p)
    summary = get_summary(text)
    print("这个文件的摘要是",summary)
