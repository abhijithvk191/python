with open('data.txt', 'r') as encrypted:
    data=encrypted.read()
count = {}
for letter in data:
    if letter in count:
        count[letter] += 1
    else:
        count.setdefault(letter,1)
print (''.join(count))
