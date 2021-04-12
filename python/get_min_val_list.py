# Get min value from python list

def get_min_val_list(lst):
    
    if len(lst) == 0:
        return "Empty List"

    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

print(get_min_val_list([89,1,2,3,4,5,6,7,8,8]))
