list1 = [1,1,1,2,3,2,2,4,5]
result = []
for i in range(0,len(list1)):
  if list1[i] != list1[i-1]:
    result.append(list1[i])
print (result)
  
