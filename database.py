import sqlite3
import sys
import datetime
def createtable():  
    conn = sqlite3.connect("Book.db") 
    c = conn.cursor()  
    c.execute('''CREATE TABLE Books( 
                bookname text,
                authorname text,
                genre text,
                year text)
                ''') 
    conn.commit()  
    conn.close() 
    

#createtable()
def addbook(bookname, authorname, genre, year): 
    conn = sqlite3.connect("Book.db")
    c = conn.cursor()
    c.execute("INSERT INTO Books VALUES (?,?,?,?)", (bookname,authorname ,genre ,year ))
    conn.commit() 
    conn.close()
def showbook():  
    conn = sqlite3.connect("Book.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Books")
    item = c.fetchall()
    return item
def removebook(bookname):
    conn = sqlite3.connect("Book.db")
    c = conn.cursor()
    c.execute("DELETE FROM Books WHERE bookname=(?)", (bookname,))
    conn.commit() 
    conn.close()
def createtable_2():
    conn = sqlite3.connect("Member.db")
    c = conn.cursor()  
    c.execute('''CREATE TABLE Members( 
                name text,
                contact text,
                date text,
                age text)
                ''') 
    conn.commit() 
    conn.close()

#createtable()
def addmember(name,contact,date,age): 
    conn = sqlite3.connect("Member.db")
    c = conn.cursor()
    c.execute("INSERT INTO Members VALUES (?,?,?,?)", (name,contact,date,age ))
    conn.commit() 
    conn.close()
def showmember():  
    conn = sqlite3.connect("Member.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Members")
    item = c.fetchall()
    return item
def removemember(name):  
    conn = sqlite3.connect("Member.db")
    c = conn.cursor()
    c.execute("DELETE FROM Members WHERE name=(?)", (name,))
    conn.commit() 
    conn.close()
def createtable_1(): 
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()  
    c.execute('''CREATE TABLE Datas( 
                name text,
                title text,
                date text)
                ''') 
    conn.commit() 
    conn.close()

#createtable()
def adddata(name,title,date): 
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO Datas VALUES (?,?,?)", (name,title,date ))
    conn.commit() 
    conn.close()
def showdata():  
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Datas")
    item = c.fetchall()
    return item
def removedata(book):  
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("DELETE FROM Datas WHERE title=(?)", (book,))
    conn.commit() 
    conn.close()
    
    
def remove_book():
    book_name = input("Enter the name of book")
    removebook(book_name)
def add_member():
    name = input("Enter the member name: ")
    contact = input("Enter contact number: ")
    age = input("Enter age: ")
    date = datetime.date.today()
    addmember(name,contact,date,age)    
def remove_member():
    name = input("Enter the name of member: ")
    removemember(name)


        
        
def searchbook(title = None, author = None , genre = None ):
    
    conn = sqlite3.connect("Book.db")
    c = conn.cursor()
    if title != None:
        c.execute("SELECT *FROM Books WHERE bookname=(?)", (title,))
    elif author != None:
        c.execute("SELECT *FROM Books WHERE authorname=(?)", (author,))
    else:
        c.execute("SELECT *FROM Books WHERE genre=(?)", (genre,))
    item = c.fetchall()
    if len(item) >= 1:
        return item
    else:
        return f"Book not found"
    
    
def renew_book():
    Name = input("Enter your name")
    
    Book = input("Enter book name: ")
    adddata(Name,Book,datetime.date.today()) 
       
def return_book():
    Name = input("Enter your name")
    
    Book = input("Enter book name: ")
    removedata(Book)    
    # main.append(reserve_list)
    
    
def add_book():
    book_name = input("Enter the book name: ")
    author_name = input("Enter the author name: ")
    year_name = input("Enter year of publication: ")
    genre_name = input("Enter the genre: ")
    addbook(book_name,author_name,genre_name,year_name)
    # global book_list
    record =showbook()
    book_list = []
    for i in record:
        i = list(i)
        book_list.append(i)
        
        
def search(title = None, author = None , genre = None ):
    if title != None :
        result = searchbook(title, author = None , genre = None )
        return result
    elif author != None :
        result = searchbook(None, author , genre = None )
    else:
        result = searchbook( None,  None ,genre )
    print(result)


def borrow_book():
    Name=input("ENTER YOUR NAME: ")
    while True:
        print("""
1)By title\n2)By author\n3)By genre\nEnter any other key to go back
        """)
        choice = input("How do you want to search it")
        y = ""
        if choice == "1":
            insert = input("Enter title of book: ")
            x = search(insert,None,None)
            y = str(x[0][0])            
        elif choice == "2":
            insert = input("Enter Author of book: ")
            x = search(None,insert,None)
        elif choice == "3":
            insert = input("Enter Genre of book: ")
            x = search(None,None,insert)
        else:
            return
        borrow = input("Do you wanna borrow it? Y/N: ")
        if borrow == "Y" or borrow == "y":
            adddata(Name,y,datetime.date.today())
        else:
            return
        
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))