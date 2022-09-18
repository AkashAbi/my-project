from platform import platform

import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="your password",
database="hotel_db"
)
mycursor=mydb.cursor()
print("TAJ SK hotel online booking")
def registercust():
    name=input("enter name:")
    address=input("enter address:")
    indate=input("enter check in date:")
    outdate=input("enter check out date:")
    roomnumber=input("enter your room number:")
    calculatingroombill=input("enter your roomtype:")
    phonenumber=input("enter your phone number:")
    sql="insert into custdata(name,address,indate,outdate,roomnumber,calculatingroombill,phonenumber)values('{}','{}','{}','{}','{}','{}','{}')".format(name,address,indate,outdate,roomnumber,calculatingroombill,phonenumber)
    mycursor.execute(sql)
    mydb.commit()

    
def roomtypeview():
    print("Do yoy want to see room type available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def roomrent():
    print ("We have the following rooms for you:-")
    print ("1. type A---->rs 1000 PN\-")
    print ("2. type B---->rs 2000 PN\-")

    print ("3. type C---->rs 3000 PN\-")
    print ("4. type D---->rs 4000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    n=int(input("For How Many Nights Did You Stay:"))
    if(x==1):
        print ("you have opted room type A")
        s=1000*n
    elif (x==2):
        print ("you have opted room type B")
        s=2000*n
    elif (x==3):
        print ("you have opted room type C")
        s=3000*n
    elif (x==4):
        print ("you have opted room type D")
        s=4000*n
    else:
        print ("please choose a room")
    print ("your room rent is =",s,"\n")
def restaurentmenuview():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
       sql="select * from restaurent"
       mycursor.execute(sql)
       rows=mycursor.fetchall()
       for x in rows:
           print(x)
def orderitem():
    
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print("do you want to purchase from above list:enter your choice:")
    d=int(input("enter your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount fopr samosa is :",s,"\n")
    elif(d==5):
        print("you have ordered sandwich")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for sandwich is :",s,"\n")
    elif(d==6):
        print("you have ordered dhokla")
        a=int(input("enter quantity"))
        s=30*a
        print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        print("you have ordered kachori")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for kachori is :",s,"\n")
    elif(d==8):
        print("you have ordered milk")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for kachori is :",s,"\n")
    elif(d==9):
        print("you have ordered noodles")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for noodles is :",s,"\n")
    elif(d==10):
        print("you have ordered pasta")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for pasta is :",s,"\n")
    else:
        print("please enter your choice from the menu")
def laundarybill():
    global z
    print("Do yoy want to see rate for laundary : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
             print(x)
    y=int(input("Enter Your number of clothes->"))
    z=y*10
    print("your laundary bill:",z,"\n")
    return z

def Menuset():
    print("enter 1: To enter customer data")
    print("enter 2 : To view roomtype")
    print("enter 3 : for calculating room bill")
    print("enter 4 : for viewing restaurent menu")
    print("enter 5 : for restaurent bill")
    print("enter 6 :for laundary bill")
    print("enter 7 : for exit:")
    try:
        userinput=int(input("please select an above option:"))
    except ValueError:
        exit("\n hi thats not a number")

    
    if(userinput==1):
        registercust()
    elif(userinput==2):
        roomtypeview()
    elif(userinput==3):
        roomrent()
    elif(userinput==4):
        restaurentmenuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        laundarybill()
    elif(userinput==7):
        print('Thanks for visiting')
        quit()
    else:
        print("enter correct choice")
Menuset()
def runagain():
    runagn=input("\n want to run again y/n:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            p=0
            
        else:
            li=0
        Menuset()
        runagn=input("\n want to run again y/n:")
runagain()
