
import sys

import database




class start():
    def __init__(self):
        print("LIBRARY MANAGEMENT SYSTEM")
        self.chosefunction()
    def chosefunction(self): 
        print("""
    1)Admin\n2)Customer\n3) Exit
            """)
        choice = input("Choose one option please: ")
        if choice == "1" :
            a=ADMINISTRATION() 
        elif choice == "2" :
            c=MEMBER_CLASS()        
        elif choice == "3" :
            sys.exit()
        else:
            print("Invalid optoion please try again")
            self.chosefunction()

class ADMINISTRATION():
    def __init__(self):
        self.admin()

    def admin(self):
        print("THE ADMIN BLOCK")
        while True:
            print("""
    1)Add book\n2)Remove book\n3)Show book\n4)Add member\n5)Remove member\n6)Show member\n7)Show data\n8)Go back
                """)
            choice = input("Choose option: ")
            if choice == "1" :
                database.add_book()
                print("Book added")  
            elif choice == "2" :
                database.remove_book()
                print("Book removed")  
            elif choice == "3" :
                book_list=[]
                record =database.showbook()
                for i in record:
                    i = list(i)
                    book_list.append(i)
                arr = []
                for i in book_list:
                    arr.append(i[1])
                    database.quicksort(arr) 
                for j in arr:
                    print(j)
            elif choice == "4" :
                database.add_member()
                print("Member added successfully into the system")  
            elif choice == "5" :
                database.remove_member()
                print("Member remove successfully from the system")  
            elif choice == "6" :
                member = database.showmember()
                member_list = []
                for i in member:
                    i = list(i)
                    print(i)
                    member_list.append(i)
            elif choice == "7":
                record = database.showdata()
                for i in record:
                    print(i)
            else:            
                print("Invalid option. Starting the appication again")
                s=start()
        




class MEMBER_CLASS():
    def __init__(self):
        self.customer()
    def customer(self):
        print("THE CUSTOMER BLOCK")
        record =database.showbook()
        for i in record:
            print(i)
        while True:
            print("""
    1)Borrow book\n2)Renew book\n3)Return book\nGo back
                """)
            choice = input("Choose one option lease: ")
            if choice == "1" :
                database.borrow_book()
            elif choice == "2" :
                database.renew_book()
            elif choice == "3" :
                database.return_book()
            else:
                print("Starting the appication again")
                s=start()




    
    

    





        
        
s=start()
