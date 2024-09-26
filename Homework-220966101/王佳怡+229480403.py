import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    

def write_text_to_file(file_path, text):
    """
    将文本写入文件
    :param file_path: 文件路径
    :param text: 要写入的文本
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # 测试 square_number 函数
    number = 7
    squared = square_number(number)
    print(f"The square of {number} is {squared}")
    
    # 测试 write_text_to_file 函数
    file_path = "example.txt"
    text_to_write = "This is an example text file."
    write_text_to_file(file_path, text_to_write)
    
    # 测试 read_text_from_file 函数
    file_content = read_text_from_file(file_path)
    if file_content:
        print(f"File Content: {file_content}")
    else:
        print("Failed to read file content.")
    
    # 测试 error_example 函数（注：此函数会引发错误）
    try:
        error_example()
    except Exception as e:
        print(f"Error Example: {e}")


#  实现错误示例
def error_example():
    """
    展示常见的代码错误
    """
    # 拼写错误：print 写成了 pritn
    pritn("This will cause a syntax error.")
    
    # 缩进错误：result 的缩进不正确
    result = square_number(5)
    
    # 未定义变量：使用了一个未定义的变量 undefined_var
    print(f"Result: {result}, Undefined Variable: {undefined_var}")

#  实现文本总结
def get_summary(text):
    """
    使用DeepSeek的API对文本进行总结
    :param text: 输入的文本
    :return: 文本的总结
    """
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
        print(f"Error during API call: {e}")
        return None



