import re

text = "My numbers are (123)456-7890 and 123-456-7890."

pattern = r"[(]\d{3}[)]\d{3}-\d{4}|\d{3}-\d{3}-\d{4}"

result = re.findall(pattern, text)

print(result)




