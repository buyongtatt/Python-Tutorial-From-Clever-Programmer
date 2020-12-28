problems = 'broke, pale, short, nerdy'
l = problems.split(', ')

for i in range(len(l)):
    print(l[i])

joined = ' and '.join(l)
print(joined)

csv = ', '.join(l)

print(csv)
