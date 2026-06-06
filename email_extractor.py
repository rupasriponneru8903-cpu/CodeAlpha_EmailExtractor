import re

text = """
Contact us:
abc@gmail.com
support@yahoo.com
hello123@gmail.com
"""

emails = re.findall(r'\S+@\S+', text)

print("Emails Found:")

for email in emails:
    print(email)
