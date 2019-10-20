s=input()
a=list(s)
a[::2] ,a[1::2]=a[1::2],a[::2]
''.join(a)
print(a)
