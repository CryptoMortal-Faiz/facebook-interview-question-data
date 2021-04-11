# Find uncoomon words in two sentences

def uncommon(a,b):
    res = []
    if a is None and len(a) == 0 and b is None and len(b) == 0:
        return "Empty Strings"
    spl_a = a.lower().split()
    spl_b = b.lower().split()
    for w in spl_a:
        if w not in spl_b:
            res.append(w)
    for w1 in spl_b:
        if w1 not in spl_a:
            res.append(w1)
    return res

  
## Below are inputs to the function
a1 = "Firstly this is the first string"
b1 = "Next is the second string"

a2 = "Firstly this IS THE first string"
b2 = "Next is the second string"

a3 = "Firstly this is the first string"
b3 = "Next second"

a4 = ""
b4 = ""

a5 = ""
b5 = "Next second"

print(uncommon(a1,b1))
print(uncommon(a2,b2))
print(uncommon(a3,b3))
print(uncommon(a4,b4))
print(uncommon(a5,b5))

''' RESULTS
['firstly', 'this', 'first', 'next', 'second']
['firstly', 'this', 'first', 'next', 'second']
['firstly', 'this', 'is', 'the', 'first', 'string', 'next', 'second']
[]
['next', 'second']
'''
