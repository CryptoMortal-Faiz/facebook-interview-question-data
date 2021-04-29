def friends(rels):
    fs = dict()
    for r in rels:
        if len(r) == 1:
            if r[0] not in fs:
                fs[r[0]] = 0
        else:
            if r[0] in fs:
                fs[r[0]] += 1
            else:
                fs[r[0]] = 1
        if r[1] in fs:
            fs[r[1]] += 1
        else:
            fs[r[1]] = 1
    return fs

  
# Find friends Driver
l = [[100, 2], [43, 2, 3], [2, 1], [5, 7]]
print(friends(l))
