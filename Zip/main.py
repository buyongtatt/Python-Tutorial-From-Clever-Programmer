list1 = [1,2,3,4,5]
list2 = ['one','two','three','four','five']

zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

items = ['Apple', 'Banana', 'Orange'] 
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

sentences = []
for item, count, price in zip(items, counts, prices):
    count, price = str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' dollar each.'
    sentences.append(sentence)
print(sentences)
