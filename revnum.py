a=86776587658
b=1
flag=0
while(a>0):
   num=a%10
   a=a//10

   if(num==b):
       flag=1
       break

   elif(flag==0):
       print("the digit not found")
