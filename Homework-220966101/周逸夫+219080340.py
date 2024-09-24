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
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# TODO: Implement a function to read text from a file
def read_text(file_path):
    try:
         with open(file_path, 'r',encoding=utf-8) as file: 
             content=file.read() 
         return content 
    except FileNotFoundError:
        return f"未找到指定文件"
    
# TODO: Implement error handling for API calls
def error_handing(text):
    try:
        prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7,
        max_tokens=150)
        return response.choices[0].message.content

    except client.APIError as e:
        logging.error(f"API 错误: {e}")
        return f"API 错误: {e}"

    except client.Timeout as e:
        logging.error(f"请求超时: {e}")
        return f"请求超时: {e}"

    except client.APIConnectionError as e:
        logging.error(f"网络连接错误: {e}")
        return f"网络连接错误: {e}"

    except client.RateLimitError as e:
        logging.error(f"请求速率限制错误: {e}")
        return f"请求速率限制错误: {e}"

    except Exception as e:
        logging.error(f"发生未知错误: {e}")
        return f"发生未知错误: {e}"
    
# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(texts, deployment="deepseek-chat", temperature=0.7, max_tokens=150):
    summaries = {}
    for idx, text in enumerate(texts):
        prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
        try:
            response = client.chat.completions.create(
                model=deployment,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            summaries[idx] = response.choices[0].message.content
        
        except Exception as e:
            summaries[idx] = f"发生未知错误: {e}"
    
    return summaries
