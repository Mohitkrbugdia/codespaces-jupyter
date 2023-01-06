a=[]
import pandas as pd
n=int(input("enter a no.:"))
for i in range(1,n):
    i=int(input("enter a no.:"))
    a.append(i)
aa1=pd.DataFrame(a)
a1=aa1.mean()
print(a1)
