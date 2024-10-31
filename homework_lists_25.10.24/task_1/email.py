import re

true_email = "example@test.com"
false_email = "example@com"
cool = "telltaleacc@gmail.com"

emails = [true_email, false_email, cool]

pattern = r"^\w+\@\D+\.\D{2,6}$"

for email in emails:
    re.findall(pattern, email)

emails_true = list(filter(lambda email: re.match(pattern, email), emails))
print(emails_true)