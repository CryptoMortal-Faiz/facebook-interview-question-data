#Find average length of Words in a given sentence

def findAverage(a):
    if len(a) == 0 or a is None:
        return "Empty String"
    sum = 0
    for w in a.split():
        sum += len(w)
    if len(a.split()) <= 0:
        return "Empty String"
    return int(round((sum/len(a.split())),0))
  
  

print(findAverage("Please enter a sentence: "))
print(findAverage(""))
print(findAverage(" "))
print(findAverage("Hello"))
print(findAverage("Hi my name is Bob"))

'''
5
Empty String
Empty String
5
3
'''
