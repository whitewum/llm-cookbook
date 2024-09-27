import os
from openai import OpenAI

client = OpenAI(
  api_key="",
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
在遥远的星系边缘，有一个被遗忘的星球，名为“翠绿之境”。这个星球上生长着一种奇特的植物，它们的叶片在月光下会发出柔和的荧光。星球的居民是一群爱好和平的生物，他们拥有透明的翅膀和长长的触角，能够与自然和谐共存。他们的生活方式简单而快乐，每天的工作就是收集月光下的露珠，用来酿造一种名为“星露”的神奇饮料。这种饮料据说能够治愈心灵的创伤，让喝下它的人忘记所有的烦恼。然而，有一天，一个邪恶的星际海盗发现了这个星球，他被“星露”的传说所吸引，决定占领这个星球，掠夺所有的“星露”。星球的居民们为了保护他们的家园和“星露”，与海盗展开了一场激烈的战斗。在这场战斗中，他们展现出了前所未有的勇气和智慧。
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

def handle_api_error(e):
    if isinstance(e, openai.error.OpenAIError):
        print(f"OpenAI API error occurred: {str(e)}")
    elif isinstance(e, openai.error.AuthenticationError):
        print("Authentication failed: Check your API key and credentials.")
    elif isinstance(e, openai.error.RateLimitError):
        print("Rate limit exceeded: Too many requests made. Please try again later.")
    elif isinstance(e, openai.error.ServiceUnavailableError):
        print("Service is temporarily unavailable. Please try again later.")
    else:
        print(f"An unexpected error occurred: {str(e)}")

def get_summary(text):
    prompt = f"Summarize the following text in 3-5 sentences:\n\n{text}"
    client = initialize_client()

    try:
        response = client.ChatCompletion.create(
            model=deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        handle_api_error(e)
        return None
    
# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(texts):
    summaries = []
    for i, text in enumerate(texts):
        print(f"Summarizing text {i + 1} out of {len(texts)}...")
        summary = get_summary(text)
        if summary:
            summaries.append(summary)
        else:
            summaries.append(f"Summary for text {i + 1} could not be generated.")
    return summaries
