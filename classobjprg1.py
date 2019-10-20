class StackOverflowUser:
    def testcaseques(self):


       print("E->easy question"
         "M->medium question"
          "c->complex question"
          "1->test cases for easy questions"
          "2->test caes for medium questions"
          "3->test caes for complex questions"
         )
       in_ques = input("Enter input questions: ")
       testcase_in = input("Enter input testcase: ")
       if in_ques=="E":
           f=open(r"d:\easyques.txt","r")
           f1=f.read()
           print(f1)
       elif in_ques=="M":
           fi = open(r"d:\mediumques.txt", "r")
           f2 = fi.read()
           print(f2)
       elif in_ques=="c":
           fl = open(r"d:\complexques.txt", "r")
           f3 = fl.read()
           print(f3)
       elif in_ques=="2":
           fe = open(r"d:\mediumtestcase.txt", "r")
           f4 = fe.read()
           print(f4)
       elif in_ques=="3":
           fo = open(r"d:\complextestcase.txt", "r")
           f5 = fo.read()
           print(f5)
       elif in_ques=="1":
            fa = open(r"d:\easytestcase.txt", "r")
            f1 = fa.read()
            print(f1)

       print(in_ques)
       print(testcase_in)

prg= StackOverflowUser()
prg.testcaseques()
