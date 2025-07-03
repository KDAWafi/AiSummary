import re

def sent_tokenize(text):
    # Very basic sentence splitter
    return re.split(r'(?<=[.!?])\s+', text.strip())


text = "This is a test. This is only a test."
print(sent_tokenize(text))
