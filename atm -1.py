
from ast import While
from multiprocessing import connection
from sqlite3 import connect
from tkinter import Menu
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "1234",
    database="atm_db"

)
mycursor = mydb.cursor()
#mycursor.execute("create table customer_data1(name varchar(300),id varchar(16),deposit varchar(8),pin varchar(5))")


print("successfully")

print("\t\t\t\t\tWELCOME TO SNA BANK ATM !!!\t\t\t\t\t")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("press 1 for login")
print("press  0 for create new account")
n = int(input("Enter the number:\t"))

name = ""
id=""
deposit= ""
pin = ""

if n==0 :
    name = input("enter name:\t")
    id = int(input("enter account no:\t  "))
    deposit = int(input("enter starting account you want deposite:\t"))
    pin = int(input("enter your password:\t"))
"""
you_name=name
account = id
amount=deposit
password = pin
"""

sql= "insert into customer_data1(name,id,deposit,pin) values ('%s','%s','%s','%s')"
val=(name,id,deposit,pin)


mycursor = mydb.cursor()

mycursor.execute(sql,val)

mydb.commit()
print("successfully")





if n ==1:
    info = (input("enter your id:\t"))
    pin = int(input("enter pin:\t "))
    mycursor = mydb.cursor()
    mycursor.execute("select * from customer_data1 where id='%s'"%(info))
    row = mycursor.fetchone()
    
    if mycursor.rowcount == 1:
        mycursor.execute("select * from customer_data1 where pin='%s'"%(pin) )
        row = mycursor.fetchone()
        

        if mycursor.rowcount ==1:
            print("login successfully\t\n")
            print("PRESS  (1) for withdrawl")
            print("PRESS  (2) for deposit")
            print("PRESS  (3) for total balance")
            print("PRESS  (4) for exit")


            d = (input("enter the number for next move:\t"))
            if d == 1 :
                a = int(input("Enter the amount you withdrawl: RS.\t₹"))
                mycursor.execute("select deposit from customer_data1 where pin='%s'"%(pin))
                
                col = mycursor.fetchone()
                x= list(col)
                for i in x:
                    z = (int(i))
                    c = z-a

                mycursor.execute("update customer_data1 set deposit='%s' where pin='%s'"%(c,pin))


            if d == 2 :
                b= int(input("enter the amount you deposite:RS.\t₹"))
                mycursor.execute("select deposit from customer_data1 where pin='%s'" % (pin))  
                col = mycursor.fetchone()
                x = list(col)
                for i in x:
                    z = (int(i))
                    c = z +b
                mycursor.execute("update customer_data1 set deposit='%s' where pin='%s'"%(c,pin))


            if d == 3 :
                mycursor.execute("select deposite from customer_data1 where pin='%s"%(pin))
                col = mycursor.fetchone()
                c = z -a or z+b

                mycursor.execute("update customer_data1 set deposit='%s' where pin='%s'"%(c,pin) )    




            if d == 4 :
                user_exit=input("you want to exit ? yes/no:\t")
                if user_exit == "y":
                    print("Thank you for using SNA atm !!!")
                    exit(0)
                else :
                    exit(1)



            else:
                print("invalid password")        




        else:
            print("account doen't exit")
            mydb.commit()             




 