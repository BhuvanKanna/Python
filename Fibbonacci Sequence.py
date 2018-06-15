def nFib(n): 
  if n<2:
    return n
  return nFib(n-2)+nFib(n-1)
for num in range(1, 9):
  
  print(nFib(num))
