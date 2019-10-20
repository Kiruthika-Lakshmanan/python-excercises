num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

a = num1
b = num2

if(num1 == 0):
    print( b)

while(num2 != 0):
    if(num1 > num2):
        num1 = num1 - num2
    else:
        num2 = num2 - num1

gcd = num1   
print(gcd)
