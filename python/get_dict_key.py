'''
Given a ´dictionary, print the key for nth highest value present in the dict.
If there are more than 1 record present for nth highest value then sort the key and print the first one.
'''

def get_dict_key(my_dict):
# Base condition for empty dictionary    
    if not my_dict:
        return "Empty Dict"
  
# list out keys and values separately
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    mlist = []
    for i in val_list:
        if i not in mlist:
            mlist.append(i)
    mlist.sort(reverse = True)

## Condition for no second max    
    if len(mlist) <= 1:
        return "No second max"
    secondmax = mlist[1]
    
# get all keys with second max
    keys = [k for k,v in my_dict.items() if v == secondmax]
    if len(keys) > 1:
        keys.sort()
        print(keys)
        first_key = keys[0]
    else:
        first_key = keys[0]
    return first_key

# Driver  
print(get_dict_key({"java":100, "python":100, "c":10, "sql":109}))
print(get_dict_key({}))
