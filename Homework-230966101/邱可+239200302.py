import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.deepseek.com"
)
deployment = "deepseek-chat"

def get_summary(text):
    """Summarize the given text using the OpenAI API."""
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
        return f"Error: {e}"

def read_text_from_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def summarize_multiple_texts(texts):
    """Summarize multiple texts."""
    summaries = []
    for text in texts:
        summary = get_summary(text)
        summaries.append(summary)
    return summaries

# Test the function
sample_text = """
[Your long text here]
"""

summary = get_summary(sample_text)
print("Summary:", summary)

# Read text from a file
file_path = "sample_text.txt"  # Replace with your file path
file_text = read_text_from_file(file_path)
if isinstance(file_text, str) and not file_text.startswith("Error"):
    file_summary = get_summary(file_text)
    print("File Summary:", file_summary)
else:
    print(file_text)

# Summarize multiple texts
texts = [
    "Text 1: [Your long text here]",
    "Text 2: [Your long text here]",
    "Text 3: [Your long text here]"
]

summaries = summarize_multiple_texts(texts)
for i, summary in enumerate(summaries):
    print(f"Summary {i+1}:", summary)
