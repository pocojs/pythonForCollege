import re

from date import result

remove_duplicate_words = ("This is is a test test.")

result = re.sub(r'\b(\w+)( \1\b)+', r'\1', remove_duplicate_words)
print(result)