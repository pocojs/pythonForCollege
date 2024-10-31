import re

extract_hashtags = ("Loving the weather! #sunny #beautifulDay #nature")

pattern = r"[#]\D+"

result = re.findall(pattern, extract_hashtags)

print(result)