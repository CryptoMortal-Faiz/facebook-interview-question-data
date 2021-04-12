# Get maximum value in a python list

def get_max_val_list(lst):
    
    if len(lst) == 0:
        return "Empty List"
    max_val = 0
    count = 0
    
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

print(get_max_val_list([0,1,2,3,4,5,6,7,8,8]))
