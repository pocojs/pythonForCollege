import re

def extract_hashtags(text: str) -> list:
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

text = "Сегодня отличный день! #погода #солнце #радость"
print(extract_hashtags(text))