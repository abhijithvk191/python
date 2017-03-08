list1 = [1,2,[3,4,[5,6,7]],8,[9,[10,[11,12]]]]
result=[]
def type_fun(x):
  if isinstance(x,list):
    
    return True
for items in list1:
  if type_fun(items):
    for items1 in items:
      if type_fun(items1):
        for items2 in items1:
          if type_fun(items2):
            for item3 in items2:
              result.append(item3)
          else:
              result.append(items2)
      else:
        result.append(items1)
  else:
    result.append(items)
print(result)
