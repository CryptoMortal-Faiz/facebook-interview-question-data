def replace_none(ls):
  t = 0
  rs = []
  for i in ls:
    if i is not None:
      rs.append(i)
      t = i
    else:
      rs.append(t)
 
  rs = [None if x == 0 else x for x in rs]
  return rs
    
a1 = [None,1,2,None,None,3,None]
a2 = [None]
a3 = [1,2,3,4,5]
a4 = [None,0,None]
a5 = [0,0,0,0,0]
a6 = [None, None, None]

print(replace_none(a1))
print(replace_none(a2))
print(replace_none(a3))
print(replace_none(a4))
print(replace_none(a5))
print(replace_none(a6))
