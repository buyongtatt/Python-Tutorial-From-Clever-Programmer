contacts = {
    'Joe': {'phone': '123-4567', 'email': 'ea@website.com'},
    'Jane': {'phone': '987-6543', 'email': 'tieowj@toiwh.com'},
}

print(contacts['Joe']['email'])


sentence = 'I like the name Aaron because the name Aaron is the best'

word_counts = {
    'I': 1,
    'like': 1,
    'the': 3,
}

# dict.items()
print(word_counts.items())
# dict.keys()
print(word_counts.keys())
# dict.values()
print(word_counts.values())
# dict.pop(key)
print(word_counts.pop('like'))
# dict.popitem()
print(word_counts.popitem())
word_counts['stupid'] = 5
print(word_counts)

# dict.clear()
word_counts.clear()
print(word_counts)
