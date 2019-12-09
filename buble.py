lst=[9,1,5]
s=len(lst)
for i in range(s):
  for j in  range(i+1,s):
  if lst[i]>lst[j]:
        lst[i],lst[j]=lst[j],lst[i]
  
 
print(lst)
