import re

def split_by_sentence(text: str) -> list:
    pattern = r"(?<=[.!?])\s+"
    sentences = re.split(pattern, text)
    return [sentence for sentence in sentences if sentence]

text = "Привет! Как дела? Все хорошо..."
print(split_by_sentence(text))