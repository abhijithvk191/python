mystring = 'Earth, otherwise known as the world, is the third planet from the Sun and the only object in the Universe known to harbor life.'
mydict = {}
inner_list = []
words = mystring.replace(',','').replace('.','').lower().split()
for word in words:
    if word[0].upper() not in mydict.keys():
        inner_list = [word]
        mydict.setdefault(word[0].upper(),inner_list)
    elif word[0].upper() in mydict.keys():
        inner_list = mydict[word[0].upper()]
        inner_list.append(word)
        mydict[word[0].upper()] = inner_list
print (mydict)
