file = open(r"E:\purchaselist.html", "r")
ch=file.read()
d={}

for x in file:
    if '<li>' in file:
        x=x.lstrip("<li>")
        x=x.rstrip("</li>\n")
        key,value=x.split(",")
file.close()
d.update({key:value})
print(d)
