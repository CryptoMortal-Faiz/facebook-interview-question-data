# Delet duplicates from python list

def remove_duplicates_list(lst):
    if len(lst) == 0:
        return "Empty List"
    mlist = []
    for i in lst:
        if i not in mlist:
            mlist.append(i)
    return mlist
  
## Driver  
l1 = [10,10,10,20,30,40,40,50,60,70]
print(remove_duplicates_list(l1))
