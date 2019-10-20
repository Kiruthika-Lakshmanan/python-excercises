a=int(input())
b=int(input())
evsum=0
odsum=0
for i in range(a,b+1):
    if(i%2==0):
        evsum=evsum*i
    else:
        odsum=odsum*i
print(odsum)
print(evsum)
    
