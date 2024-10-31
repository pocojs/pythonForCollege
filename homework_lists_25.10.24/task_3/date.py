import re

replace_dates = "Today's date is 24/10/2024."

pattern = r"(\d{2})/(\d{2})/(\d{4})"
result = re.search(pattern, replace_dates)
print(result)
if result:
    yyyy = result.group(3)
    mm = result.group(2)
    dd = result.group(1)
    new_date = yyyy + '-' + mm + '-' + dd

print(new_date)