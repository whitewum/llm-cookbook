#赵柳雨+239050440

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
        print(f"Error during API call: {e}")
        return None

def read_text_from_file(file_path):
    """Read text from a specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def summarize_multiple_texts(texts):
    """Summarize a list of texts."""
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# Example usage
sample_text = """
[Your long text here]
"""

# Get summary for a single text
summary = get_summary(sample_text)
print("Summary:", summary)

# Read from a file and summarize
file_path = "path/to/your/file.txt"
file_text = read_text_from_file(file_path)
if file_text:
    summary_from_file = get_summary(file_text)
    print("File Summary:", summary_from_file)

# Summarize multiple texts
texts_to_summarize = [
    "Text one to summarize.",
    "Text two to summarize.",
    # Add more texts as needed
]

summaries = summarize_multiple_texts(texts_to_summarize)
for i, summary in enumerate(summaries):
    print(f"Summary of Text {i + 1}:", summary)
