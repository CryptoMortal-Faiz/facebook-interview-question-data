# Given a ´dictionary, print the key for nth highest value present in the dict

def get_dict_max_val(new_dict):
    if not new_dict:
        return("Empty Dict")
    val_list = list(new_dict.values())
    res = []
    for i in val_list:
        if i not in res:
            res.append(i)
    res.sort
    max_val = res[len(res)-1]
    return max_val

## Approach 2
def get_dict_max_val(new_dict):
    if not new_dict:
        return("Empty Dict")
    values = set(my_dict.values())
    res = sorted(values,reverse = True)
    return res[0]

# Driver
dict1 ={"google":12, "amazon":9, "flipkart":4, "fb":13}
print(get_dict_max_val(dict1))
