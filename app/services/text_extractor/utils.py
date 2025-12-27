
import re


def clean_output_text(text):
    if not text:
        return ""
    
    text = re.sub(r'[\n\s\t]+', " ", text)
    text = re.sub(r'\s{2,}', " ", text)
    return text.strip()