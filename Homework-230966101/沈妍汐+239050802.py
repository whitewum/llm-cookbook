import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="your-api-key",  # Replace with your actual API key
    base_url="https://api.deepseek.com"  # Your API's base URL
)
deployment = "deepseek-chat"

def get_summary(text):
    """Summarize the given text."""
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
        print(f"Error occurred during API call: {e}")
        return None

def read_text_file(file_path):
    """Read text from a file and return its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def summarize_file(file_path):
    """Summarize the content of a given text file."""
    text = read_text_file(file_path)
    if text:
        return get_summary(text)
    return None

# Example usage
if __name__ == "__main__":
    # Replace with the path to your text file
    file_path = "path/to/your/textfile.txt"
    
    summary = summarize_file(file_path)
    if summary:
        print("Summary:", summary)
