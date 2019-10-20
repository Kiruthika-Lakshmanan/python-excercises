a=input()
b=input()
f = open(r"E:\htmltest.html",'r')
fa=open(r"E:\dynamic"+a+".html",'w+')
filedata = f.read()

#filedata = filedata.replace("gucug",a )

for i in f:

    if "<h1>" in i:
        #s=i[5:-5]
        s="<h1>Hello"+a+"</html>"
        fa.write(s)
    else:
        fa.write('%s'%i)
#
#fa.write(filedata)
#fa.close()
f.close()
print(filedata)
