# find 's' in mississippi

def find_s(str):
  if len(str) == 0 or str is None:
    return "Empty String"
  count = 0
  for i in str:
    if i == 's':
      count += 1
  return count
