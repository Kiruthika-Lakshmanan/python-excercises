class userinterface:

 def student(self):
    a=input("NAME:")
    b=input("DOB:")
    d = {}
    f = open(r"E:studentnameanddob.txt", "r")
    for line in f:
        (key, val) = line.strip().split(",")
        d[key] = val


    if a in d:
        if b == d[a]:
            print("valid")

        else:
            print("incorrect")
            print("enter a valid user name and password")
    else:
        print("invalid")
        print("enter a valid user name and password")

 def staff():
    c=input("NAME:")
    d=input("DOB:")
    e = {}
    f1 = open(r"E:staffnameandid.txt", "r")
    for line in f1:
        (key, val) = line.strip().split(",")
        e[key] = val


    if c in e:
        if d == e[c]:
            print("valid")

        else:
            print("incorrect")
            print("enter a valid user name and date of birth")
    else:
        print("invalid")
        print("enter a valid user name and date of birth")
                                                         

print("1->click 1 for student panel")
print("2->click 2 for staff panel")
opt=int(input())
if opt==1:
    option1=userinterface()
    option1.student()
elif opt==2:
    option2=userinterface()
    option2.staff()
