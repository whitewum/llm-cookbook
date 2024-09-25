import os
from openai import OpenAI
import requests

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
def read_text_from_file(file_path):
    """
    Reads text from a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except IOError as e:
        print(f"Error: An I/O error occurred while reading the file: {e}")
        return None

# TODO: Implement error handling for API calls
def summarize_text_via_api(text, api_url, api_key):
    """
    Sends text to an API for summarization and returns the summarized text.
    
    :param text: The text to be summarized.
    :param api_url: The URL of the API endpoint.
    :param api_key: The API key for authentication.
    :return: The summarized text or None if an error occurs.
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text
    }
    
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json().get('summary', '')
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while making the API call: {e}")
        return None
# TODO: Add functionality to summarize multiple texts
def summarize_multiple_texts(file_paths, api_url, api_key):
    """
    Reads multiple texts from files, summarizes each using an API, and returns the summaries.
    
    :param file_paths: List of file paths to read texts from.
    :param api_url: The URL of the API endpoint.
    :param api_key: The API key for authentication.
    :return: A list of summarized texts.
    """
    summaries = []
    
    for file_path in file_paths:
        text = read_text_from_file(file_path)
        if text:
            summary = summarize_text_via_api(text, api_url, api_key)
            if summary:
                summaries.append(summary)
    
    return summaries
