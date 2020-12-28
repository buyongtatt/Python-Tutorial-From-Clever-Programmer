import re

text = 'random string. MyName_-123@website.com . some more random text. YourName888@company.net'

pattern = re.compile('[a-zA-Z0-9\-\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+')

result = pattern.findall(text)
print(result)