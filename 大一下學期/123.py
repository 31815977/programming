def isPrime(x):
  if x==2:
    TF=True
  elif x>1:
    for y in range(2,x):
      if (x%y)==0:
        TF=False
        break
      else:
        TF=True        
  else:
    TF=False
  return(TF)

def allprimes(n):
  n = eval(input())
  prime = []
  for i in range(1, n + 1):
    if(isPrime(i) == True):
      prime.append(i)
  print(prime)
  return prime

def Sort(alist):
  blist = len(alist)
  for i in range(blist-2):
      for j in range(blist-i-1): 
          if alist[j] > alist[j+1]:
              alist[j], alist[j+1] = alist[j+1], alist[j]
  return(blist)

allprimes(15)