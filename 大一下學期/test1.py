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