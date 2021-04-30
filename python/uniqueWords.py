def uncommon(a):
    unique = set(a.lower().split()) # For input as list unique = set(a) 
    return len(unique)
a1 = "First this is the first string"
print(uncommon(a1))

# To get all words with values in dict

words = "first this is the first string"
wordfreq = {}
for word in words.split():
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1
wordfreq = {key:val for key, val in wordfreq.items() if val == 1}
print(wordfreq)

