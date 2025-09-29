class Bank:
    def __init__(self):
       self.database={}
    def createaccount(self,name,l):
       self.database[name]=l
class Account:
    def __init__(self,name,password,email):
        self.name=name
        self.password=password 
        self.email=email
        self.l=[self.name,self.password,self.email,0,[]]
        a.createaccount(self.name,self.l)
        print(a.database)
        print("successfully account created")
a=Bank()
while 1:
    print("Welcome to sns bank")
    print("_"*100)
    print("1.login.")
    print("2.signup.")
    print("3.exit.")
    i=int(input("enter your choice"))
    if i==1:
        n=input("Enter your name- ")
        if n in a.database:
            p=input("Enter your password")
            if a.database[n][1]==p:
              while 1:
                print()
                print("-"*100)
                print("welcome",n,"to sns bank")
                print("1.Check banlance")
                print("2.Withdraw")
                print("3.Deposit")
                print("4.Transaction")
                print("5.Send Money")
                print("6.Exit")
                c=int(input("Select one option-"))
                if c==6:
                    break
                elif c==1:
                    print(a.database[n][3])
                elif c==2:
                    amount=int(input("Enter the amount-"))
                    if amount<a.database[n][3]:
                        a.database[n][3]-=amount
                        s="I have withdrawn "+str(amount)
                        a.database[n][4].append(s)
                        print("successfully withdraw")
                        print("current amount is",a.database[n][3])
                    else:
                        print("Insufficient balance")
                elif c==3:
                    amount=int(input("Enter the amount :"))
                    if amount>0:
                        a.database[n][3]+=amount
                        s="I have deposited "+str(amount)
                        a.database[n][4].append(s)
                        print("successfully deposited")
                        print("current amount is",a.database[n][3])
                    else:
                        print("Invalid amount")
                elif c==5:
                    reciever=input("Enter reciever name:")
                    if reciever in a.database:
                        amount=int(input("Enter amount to send"))
                        if amount>0:
                          if amount<a.database[n][3]:
                            a.database[n][3]-=amount 
                            a.database[reciever][3]+=amount
                            s="I have send "+str(amount)+" rs to "+reciever
                            s1="I have recieved "+str(amount)+" rs from "+n
                            a.database[n][4].append(s)
                            a.database[reciever][4].append(s1)
                        else:
                            print("Invalid amount")
                    else:
                        print("Invalid User")
                elif c==4:
                    for i in a.database[n][4]:
                        print(i)
                    
                
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        
        
    elif i==2:
       name=input("Enter your name ")
       password=input("Enter your password ")
       email=input("Enter your name email ")
       name=Account(name,password,email)
    elif i==3:
        print("Thankyou for visiting sns bank")
        print("come back again")
        exit()
    else:
        print("Invalid option")