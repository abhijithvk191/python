list1 = [1,2,[3,4,[5,6,7]],8,[9,[10,[11,12]]]]
result=[]
def type_fun(x):
  for items in x:
    if isinstance(items,list):
      if type_fun(items):
        return True
      else:  
        result.append(items)
    else:
      result.append(items)
type_fun(list1)
