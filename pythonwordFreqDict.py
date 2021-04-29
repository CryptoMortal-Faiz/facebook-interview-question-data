words = "This is a senctence for a DE"

d = {}
count = 0 
for i in words.split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
