# find 's' in mississippi

def find_s(str):
  if len(str) == 0 or str is None:
    return "Empty String"
  count = 0
  for i in str.lower(): # Or upper depending on 'S' or 's'
    if i == 's':
      count += 1
  return count

print(find_s('mississippi'))
print(find_s('facebook'))
print(find_s('miSsisSippi'))
print(find_s(' '))
print(find_s(' s '))
print(find_s(''))
print(find_s('facebook interview for Data Engineer'))

''' results for each print
4
0
4
0
1
Empty String
0
'''

