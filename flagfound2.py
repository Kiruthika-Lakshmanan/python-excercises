flag=0
n=4
count=0
k=["hsf","ugwd","hd"]
for i in range(len(k)):
  if 'ad' in k:
      flag=1
      count=count+1

  elif(flag==0):
      print("-1")
      break
print(count)
