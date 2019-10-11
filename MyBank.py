import sqlite3,sys,os
def front():
    os.system('cls')
    A=0
    while A!=1:
        print('''
                                        WELCOME TO MY BANK

1. CREATE NEW ACCOUNT
2. LOGIN TO YOUR ACCOUNT
3. ABOUT BANK
4. EXIT''')
        X=int(input("ENTER YOUR CHOICE : "))
        if X==1:
            create_account()
            
        elif X==2:
            os.system('cls')
            open_account()
            
        elif X==4:
            print("THANK YOU")
            exit()
        else:
            print("INVALID ENTRY")

    
def create_table():
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    curbank.execute('''CREATE TABLE account_holder(
    Name STRING(50) NOT NULL,
    Age STRING(3) NOT NULL,
    Fathers_Name STRING(50) NOT NULL,
    Mothers_Name STRING(50) NOT NULL,
    Contact_Number STRING(10) NOT NULL,
    Address STRING(100) NOT NULL,
    Addhar_Card STRING(16) NOT NULL,
    Nominee STRING(50) NOT NULL,
    Username STRING(20) PRIMARY KEY NOT NULL UNIQUE,
    Password STRING(20) NOT NULL,
    Type_Of_Account STRING(10) NOT NULL)
    Balance STRING(20) DEFAULT(0)
    WITHOUT ROWID;
    ''')
    MyBank.close()

    
def create_account():
    y=0
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    os.system('cls')
    name=str(input("ENTER YOUR NAME : "))
    y=0
    while y!= 1:
        age=str(input("ENTER YOUR AGE : "))
        if age.isdigit():
            y=1
        else:
            print("PLEASE ENTER INTEGER ONLY . TRY AGAIN.....")
    fname=str(input("ENTER YOUR FATHER'S NAME : "))
    mname=str(input("ENTER YOUR MOTHER'S NAME : "))
    y=0
    while y!= 1:
        number=str(input("ENTER YOUR CONTACT NUMBER : "))
        if number.isdigit():
            if len(number)==10:
                y=1
            else :
                print("INVALID ENTRY. TRY AGAIN......")
        else:
            print("PLEASE ENTER INTEGER ONLY . TRY AGAIN.....")
    address=str(input("ENTER YOUR ADDRESS : "))
    y=0
    while y!= 1:
        addhar=str(input("ENTER YOUR ADDHAR CARD NUMBER : "))
        if addhar.isdigit():
            if len(addhar)==12:
                y=1
            else :
                print("INVALID ENTRY. TRY AGAIN......")
        else:
            print("PLEASE ENTER INTEGER ONLY . TRY AGAIN.....")
    nom=str(input("ENTER YOUR NOMINEE'S NAME : "))
    y=0
    while y != 1:
        uname=str(input("ENTER YOUR UNIQUE USERNAME : "))
        curbank.execute("SELECT Name FROM account_holder WHERE Username=?",(uname,))
        data=curbank.fetchall()
        if len(data)==0:
            y=1
        else:
            print("THIS USERNAME IS ALREADY IN USE . TRY AGAIN.....")
        
    passw=input("ENTER YOUR PASSWORD : ")
    y=0
    while y!= 1:
        toa=str(input("ENTER THE TYPE OF ACCOUNT (SAVING OR CURRENT): "))
        if toa=="SAVING" or toa=="CURRENT":
            y=1
        else:
            print("PLEASE ENTER IN BLOCK . TRY AGAIN.....")
    curbank.execute('''
    INSERT INTO account_holder (
    Name,Age,Fathers_Name,Mothers_Name,Contact_Number,Address,Addhar_Card,Nominee,Username,Password,Type_Of_Account)
    VALUES (?,?,?,?,?,?,?,?,?,?,?);''',(name,age,fname,mname,number,address,addhar,nom,uname,passw,toa))
    MyBank.commit()
    MyBank.close()

def open_account():
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    Y=0
    while Y != 1:
        os.system('cls')
        print('''
                                    WELCOME TO LOGIN YOUR ACCOUNT''')
        un=str(input("ENTER YOUR USERNAME : "))
        curbank.execute("SELECT Name FROM account_holder WHERE Username=?",(un,))
        data=curbank.fetchall()
        if len(data)==0:
            print("USERNAME NOT FOUND. TRY AGAIN......\n")
        else:
            ps=str(input("ENTER YOUR PASSWORD : "))
            #sql="SELECT * from account_holder WHERE Username=?",(un,)
            curbank.execute("SELECT * from account_holder WHERE Username=?",(un,))
            record=curbank.fetchall()
            for row in record:
                if ps==row[9]:
                    os.system('cls')
                    print('''
                                WELCOME TO YOUR ACCOUNT {}
1. SHOW DETAILS
2. UPDATE DETAILS
3. REMOVE ACCOUNT
4. ATM
5. RETURN TO FRONT PAGE\n'''.format(row[0]))
                    x=int(input("ENTER YOUR CHOICE : "))

                    if x==1:
                        show(record)
                        
                    elif x==2:
                        MyBank.close()
                        update(un)

                    elif x==3:
                        MyBank.close()
                        delete(un)

                    elif x==4:
                        MyBank.close()
                        atm(un)

                    elif x==5:
                        Y=0
                        front()
                
                elif ps !=row[9]:
                    print("YOU ENTERED WRONG PASSWORD")
                    Y=0
    MyBank.close()

def show(record):
    os.system('cls')
    for row in record:
        print("\nNAME : ",row[0],)
        print("AGE : ",row[1],)
        print("FATHER'S NAME : ",row[2],)
        print("MOTHER'S NAME : ",row[3],)
        print("CONTACT NUMBER : ",row[4],)
        print("ADDRESS : ",row[5],)
        print("ADDHAR CARD : ",row[6],)
        print("NOMINEE : ",row[7],)
        #print("USERNAME=",row[8],)
        #print("PASSWORD=",row[9],)
        print("TYPE OF ACCOUNT : ",row[10],)
        print("BALANCE : ",row[11],)

def update(un):
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    print('''
WHAT DO YOU WANT TO UPDATE?
1. NAME
2. AGE
3. CONTACT NUMBER
4. USERNAME
5. PASSWORD
6. TYPE OF ACCOUNT''')
    a=int(input("ENTER YOUR CHOICE : "))
    if a==1:
        name=str(input("ENTER YOUR NAME : "))
        try:
            curbank.execute("UPDATE account_holder SET Name =? WHERE Username=?",(name,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    elif a==2:
        y=0
        while y!= 1:
            age=str(input("ENTER YOUR AGE : "))
            if age.isdigit():
                y=1
            else:
                print("PLEASE ENTER INTEGER ONLY . TRY AGAIN.....")
        #sql="UPDATE account_holder SET Age = "+age+" WHERE Username="+un+";"
        try:
            curbank.execute("UPDATE account_holder SET Age =? WHERE Username=?",(age,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    elif a==3 :
        y=0
        while y!= 1:
            number=str(input("ENTER YOUR CONTACT NUMBER : "))
            if number.isdigit():
                if len(number)==10:
                    y=1
                else :
                    print("INVALID ENTRY. TRY AGAIN......")
            else:
                print("PLEASE ENTER INTEGER ONLY . TRY AGAIN.....")
        try:
            curbank.execute("UPDATE account_holder SET Contact_Number=? WHERE Username=?",(number,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    elif a==4:
        y=0
        while y != 1:
            uname=str(input("ENTER YOUR UNIQUE USERNAME : "))
            curbank.execute("SELECT Name FROM account_holder WHERE Username=?",(uname,))
            data=curbank.fetchall()
            if len(data)==0:
                y=1
            else:
                print("THIS USERNAME IS ALREADY IN USE . TRY AGAIN.....")
        try:
            curbank.execute("UPDATE account_holder SET Username=? WHERE Username=?",(uname,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    elif a==5:
        passw=input("ENTER YOUR PASSWORD : ")
        try:
            curbank.execute("UPDATE account_holder SET Password=? WHERE Username=?",(passw,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    elif a==6:
        y=0
        while y!= 1:
            toa=str(input("ENTER THE TYPE OF ACCOUNT (SAVING OR CURRENT): "))
            if toa=="SAVING" or toa=="CURRENT":
                y=1
            else:
                print("PLEASE ENTER IN BLOCK . TRY AGAIN.....")
        try:
            curbank.execute("UPDATE account_holder SET Type_Of_Account=? WHERE Username=?",(toa,un,))
            MyBank.commit()
            print("record updated successfully")
        except:
            print("error in update operation")
            MyBank.rollback()
    MyBank.close()

def delete(un):
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    curbank.execute("DELETE FROM account_holder WHERE Username=?",(un,))
    choice=input("ARE YOU SURE YOU WANT TO DELETE : ")
    if choice=='YES' or choice=='yes':
        print("YOUR ACCOUNT IS SUCCESSFULLY REMOVED")
        MyBank.commit()
    MyBank.close()

def atm(un):
    MyBank=sqlite3.connect('my_bank.db')
    curbank=MyBank.cursor()
    Y=0
    while Y != 1:
        os.system('cls')
        print('''                    WELCOME TO ATM SERVICES''') 
        #un=str(input("ENTER YOUR USERNAME : "))
        curbank.execute("SELECT Name FROM account_holder WHERE Username=?",(un,))
        data=curbank.fetchall()
        if len(data)==0:
            print("USERNAME NOT FOUND. TRY AGAIN......\n")
        else:
            ps=str(input("ENTER YOUR PASSWORD : "))
            #sql="SELECT * from account_holder WHERE Username=?",(un,)
            curbank.execute("SELECT * from account_holder WHERE Username=?",(un,))
            record=curbank.fetchall()
            for row in record:
                if ps==row[9]:
                    print('''
1. SHOW BALANCE
2. WITHDRAW
3. DEPOSIT
4. GO BACK''')
                    choice=int(input("ENTER YOUR CHOICE : "))
                    if choice==1:
                        bal=curbank.execute("SELECT Balance FROM account_holder WHERE Username=?",(un,))
                        for b in bal:
                            print("YOUR BALANCE IS ",b[0]," RUPPEES")
                            
                    elif choice==2:
                        wd=int(input("ENTER THE AMOUNT TO WITHDRAW : "))
                        bal=curbank.execute("SELECT Balance FROM account_holder WHERE Username=?",(un,))
                        for b in bal:
                            B=b[0]-wd
                            if B>=0:
                                print("YOUR BALANCE IS ",B," RUPPEES")
                                curbank.execute("UPDATE account_holder SET Balance=? WHERE Username=?",(B,un,))
                                MyBank.commit()
                            else:
                                print("INSUFFICIENT BALANCE!")

                    elif choice==3:
                        da=int(input("ENTER THE AMOUNT TO DEPOSIT : "))
                        bal=curbank.execute("SELECT Balance FROM account_holder WHERE Username=?",(un,))
                        for b in bal:
                            B=b[0]+da
                            if B>=0:
                                print("YOUR BALANCE IS ",B," RUPPEES")
                                curbank.execute("UPDATE account_holder SET Balance=? WHERE Username=?",(B,un,))
                                MyBank.commit()
                            else:
                                print("INSUFFICIENT BALANCE!")

                    elif choice==4:
                        open_account()
                        
front()
