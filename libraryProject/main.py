from tkinter import *
import tkinter.font as font
import datetime as dt
import pypyodbc as pypyodbc



root = Tk()
root.geometry("1000x600")
root.title("Library Management System")
root['background']="#EFEDE1"

conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V06V6RC;'
                      'Database=libraryManagement;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


fontSize = font.Font(family='Helvetica', size=10, weight='bold')
fontIntro = font.Font(family='Helvetica', size=13, weight='bold')
fontBookView = font.Font(family='Helvetica', size=11, weight='bold')


def openWindowViewBooks():
    global row
    newWindow = Toplevel(root)
    newWindow.geometry("880x1000")
    newWindow['background'] = "#EFEDE1"
    newWindow.title("View Books")
    conn = pypyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-V06V6RC;'
                            'Database=libraryManagement;'
                            'Trusted_Connection=yes;')
    cursor = conn.cursor()
    viewBooksLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#775600',fg='#ffffff',
                             text = "View Books")
    viewBooksLabel.pack(fill="x")

    bookIdBlock = Label(newWindow,
                        height=100, width=22,
                        bg="#775600",fg='#ffffff')
    bookIdBlock.place(x=5,
                      y=70)
    bookIdText = Label(bookIdBlock,
                       text = "Book ID",
                       bg='#775600', fg='#EFEDE1')
    bookIdText['font'] = fontSize
    bookIdText.place(x=40,
                     y=6)
    cursor.execute("select * from BookList")
    list = []
    for row in cursor:
        list.append(row[0])
    y = 30
    for bookId in list:
        counterString = Label(bookIdBlock,
                            text=bookId,
                            bg='#775600', fg='#EFEDE1')
        counterString.place(x=-1,
                          y=y)
        y = y + 24

    bookTitleBlock = Label(newWindow,
                        height=100, width=22,
                        bg="#775600",fg='#ffffff')
    bookTitleBlock.place(x=180,
                      y=70)
    bookTitleText = Label(bookTitleBlock,
                       text = "Book Title",
                       bg='#775600', fg='#EFEDE1')
    bookTitleText['font'] = fontSize
    bookTitleText.place(x=40,
                     y=6)
    cursor.execute("select * from BookList")
    list = []
    for row in cursor:
        list.append(row[1])
    y = 30
    for bookTitle in list:
        counterString = Label(bookTitleBlock,
                            text=bookTitle,
                            bg='#775600', fg='#EFEDE1')
        counterString.place(x=-1,
                          y=y)
        y = y + 24

    authorBlock = Label(newWindow,
                        height=100, width=22,
                        bg="#775600",fg='#ffffff')
    authorBlock.place(x=355,
                      y=70)
    authorText = Label(authorBlock,
                       text = "Author",
                       bg='#775600', fg='#EFEDE1')
    authorText['font'] = fontSize
    authorText.place(x=46,
                     y=6)
    cursor.execute("select * from BookList")
    list = []
    for row in cursor:
        list.append(row[2])
    y = 30
    for author in list:
        counterString = Label(authorBlock,
                            text=author,
                            bg='#775600', fg='#EFEDE1')
        counterString.place(x=-1,
                          y=y)
        y = y + 24

    pageBlock = Label(newWindow,
                        height=100, width=22,
                        bg="#775600",fg='#ffffff')
    pageBlock.place(x=535,
                      y=70)
    pageText = Label(pageBlock,
                       text = "Page",
                       bg='#775600', fg='#EFEDE1')
    pageText['font'] = fontSize
    pageText.place(x=48,
                     y=6)
    cursor.execute("select * from BookList")
    list = []
    for row in cursor:
        list.append(row[3])
    y = 30
    for page in list:
        counterString = Label(pageBlock,
                            text= page,
                            bg='#775600', fg='#EFEDE1')
        counterString.place(x=-1,
                          y=y)
        y = y + 24

    availabilityBlock = Label(newWindow,
                        height=100, width=22,
                        bg="#775600",fg='#ffffff')
    availabilityBlock.place(x=715,
                      y=70)
    availabilityText = Label(availabilityBlock,
                       text = "Availability",
                       bg='#775600', fg='#EFEDE1')
    availabilityText['font'] = fontSize
    availabilityText.place(x=40,
                     y=6)
    cursor.execute("select * from BookList")
    list = []
    for row in cursor:
        list.append(row[4])
    y = 30
    for availability in list:
        counterString = Label(availabilityBlock,
                            text=availability,
                            bg='#775600', fg='#EFEDE1')
        counterString.place(x=-1,
                          y=y)
        y = y + 24
    conn.commit()
    conn.close()


def openWindowBorrowBooks():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Borrow Books")

    borrowBooksLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#667700',fg='#ffffff',
                             text = "Borrow Books")
    borrowBooksLabel.pack(fill="x")
    global bookIdEntry
    global studentIdEntry

    # Book ID part
    bookIDLabel = Label(newWindow,
          height=4, width=40,
          bg='#667700',fg='#ffffff')
    bookIDLabel.place(x=50,
                      y=50)
    bookIdText = Label(bookIDLabel,
                       text = "Book ID",
                       bg='#667700', fg='#ffffff')
    bookIdText.place(x=10,
                     y=20)
    bookIdEntry = Entry(bookIDLabel,
                        width=30)
    bookIdEntry.place(x=80,
                      y=20)

    studentIDLabel = Label(newWindow,
          height=4, width=40,
          bg='#667700',fg='#ffffff')
    studentIDLabel.place(x=50,
                         y=130)
    studentIdText = Label(studentIDLabel,
                       text = "Student ID",
                       bg='#667700', fg='#ffffff')
    studentIdText.place(x=10,
                        y=20)
    studentIdEntry = Entry(studentIDLabel,
                        width=30)
    studentIdEntry.place(x=80,
                      y=20)


    def borrowBook():
        borrowingDate = dt.datetime.now()
        borrowDay = borrowingDate.day
        borrowMonth = borrowingDate.month
        borrowYear = borrowingDate.year
        borrowingDate = str(borrowDay) + ("/") + str(borrowMonth) + ("/") + str(borrowYear)
        returnMonth = borrowMonth + 1
        global returningDate
        returningDate = str(borrowDay) + ("/") + str(returnMonth) + ("/") + str(borrowYear)
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        bookIdList = []
        studentIdList = []
        cursor.execute("select * from BookList")
        for row in cursor:
            bookIdList.append(str(row[0]))
        cursor.execute("select * from StudentInfo")
        for row in cursor:
            studentIdList.append(str(row[0]))
        if studentIdEntry.get() not in studentIdList:
            newWindow = Toplevel(root)
            newWindow.geometry("300x300")
            newWindow['background'] = "#EFEDE1"
            newWindow.title("Error")
            errorLabel = Label(newWindow,
                               height=2, width=40,
                               bg='#667700', fg='#ffffff',
                               text="Student is not found")
            errorLabel.place(x=8,
                             y=130)
        if studentIdEntry.get() in studentIdList:
            cursor.execute("select * from StudentInfo where studentId = " + studentIdEntry.get())
            borrowedBooksNumberList = []
            for row in cursor:
                borrowedBooksNumberList.append(row[2])
            if borrowedBooksNumberList[0] == 3:
                newWindow = Toplevel(root)
                newWindow.geometry("300x300")
                newWindow['background'] = "#EFEDE1"
                newWindow.title("Error")
                errorLabel = Label(newWindow,
                                   height=2, width=40,
                                   bg='#667700', fg='#ffffff',
                                   text="The student cannot borrow any more book.")
                errorLabel.place(x=8,
                                 y=130)
        borrowedBooksList = []
        cursor.execute("select FirstBook, SecondBook, ThirdBook from StudentInfo")
        for rows in cursor:
            for row in rows:
                borrowedBooksList.append(str(row))
        if bookIdEntry.get() in borrowedBooksList:
            newWindow = Toplevel(root)
            newWindow.geometry("300x300")
            newWindow['background'] = "#EFEDE1"
            newWindow.title("Error")
            errorLabel = Label(newWindow,
                               height=2, width=40,
                               bg='#667700', fg='#ffffff',
                               text="The book has already been borrowed.")
            errorLabel.place(x=8,
                             y=130)
        if bookIdEntry.get() not in bookIdList:
            newWindow = Toplevel(root)
            newWindow.geometry("300x300")
            newWindow['background'] = "#EFEDE1"
            newWindow.title("Error")
            errorLabel = Label(newWindow,
                               height=2, width=40,
                               bg='#667700', fg='#ffffff',
                               text="Book is not found")
            errorLabel.place(x=8,
                             y=130)
        cursor.execute("select * from StudentInfo where studentId = " + studentIdEntry.get())
        borrowedBooksNumberList = []
        for row in cursor:
            borrowedBooksNumberList.append(row[2])
        if bookIdEntry.get() in bookIdList and studentIdEntry.get() in studentIdList and borrowedBooksNumberList[0] != 3 and bookIdEntry.get() not in borrowedBooksList:
            conn = pypyodbc.connect('Driver={SQL Server};'
                                    'Server=DESKTOP-V06V6RC;'
                                    'Database=libraryManagement;'
                                    'Trusted_Connection=yes;')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO BorrowedBooks (BookId, StudentId, BorrowDate, ReturnDate) VALUES (?,?,?,?)",
                           [(bookIdEntry.get()), (studentIdEntry.get()), (borrowingDate), (returningDate)])
            cursor.execute("update BookList set Availability = 'Borrowed' where BookId = " + bookIdEntry.get())
            cursor.execute("update StudentInfo set BorrowedBooks += 1 where StudentId = " + studentIdEntry.get())

            cursor.execute("select * from StudentInfo where studentId = " + studentIdEntry.get())
            firstBookList = []
            for row in cursor:
                firstBookList.append(str(row[5]))
            cursor.execute("select * from StudentInfo where studentId = " + studentIdEntry.get())
            secondBookList = []
            for row in cursor:
                secondBookList.append(str(row[6]))
            cursor.execute("select * from StudentInfo where studentId = " + studentIdEntry.get())
            thirdBookList = []
            for row in cursor:
                thirdBookList.append(str(row[7]))
            if firstBookList[0] == 'None':
                cursor.execute("update StudentInfo set FirstBook = (?) where StudentId = (?)",
                               (bookIdEntry.get(), studentIdEntry.get()))
            elif secondBookList[0] == 'None':
                cursor.execute("update StudentInfo set SecondBook = (?) where StudentId = (?)",
                               (bookIdEntry.get(), studentIdEntry.get()))
            elif thirdBookList[0] == 'None':
                cursor.execute("update StudentInfo set ThirdBook = (?) where StudentId = (?)",
                               (bookIdEntry.get(), studentIdEntry.get()))
        conn.commit()
        conn.close()

    borrowingDate = dt.datetime.now()
    borrowDay = borrowingDate.day
    borrowMonth = borrowingDate.month
    borrowYear = borrowingDate.year
    returnMonth = borrowMonth + 1
    global returningDate
    returningDate = str(borrowDay) + ("/") + str(returnMonth) + ("/") + str(borrowYear)
    returnDateLabel = Label(newWindow,
          height=4, width=40,
          bg='#667700',fg='#ffffff')
    returnDateLabel.place(x=50,
                      y=210)
    returnDateText = Label(returnDateLabel,
                       text = "Return Date",
                       bg='#667700', fg='#ffffff')
    returnDateText.place(x=10,
                     y=20)
    returningDateLabel = Label(returnDateLabel,
                               text = returningDate,
                               bg='#667700', fg='#ffffff',
                        width=16)
    returningDateLabel.place(x=80,
                      y=20)

    borrowBookButton = Button(newWindow,
                           height=2, width=16,
                           text="Borrow Book",
                           command=borrowBook,
                           bg='#667700', fg='#ffffff')
    borrowBookButton.place(x=130,
                        y=290)


def openWindowBookReturn():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Book Return")
    bookReturnLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#007777',fg='#ffffff',
                             text = "Book Return")
    bookReturnLabel.pack(fill="x")

    #Book ID part
    bookIDLabel = Label(newWindow,
          height=4, width=40,
          bg='#007777',fg='#ffffff')
    bookIDLabel.place(x=50,
                      y=70)
    bookIdText = Label(bookIDLabel,
                       text = "Book ID",
                       bg='#007777', fg='#ffffff')
    bookIdText.place(x=10,
                     y=20)
    bookIdEntry = Entry(bookIDLabel,
                        width=30)
    bookIdEntry.place(x=80,
                      y=20)

    # Student ID part
    studentIDLabel = Label(newWindow,
          height=4, width=40,
          bg='#007777',fg='#ffffff')
    studentIDLabel.place(x=50,
                         y=150)
    studentIdText = Label(studentIDLabel,
                       text = "Student ID",
                       bg='#007777', fg='#ffffff')
    studentIdText.place(x=10,
                        y=20)
    studentIdEntry = Entry(studentIDLabel,
                        width=30)
    studentIdEntry.place(x=80,
                      y=20)

    def returned():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()

        cursor.execute("delete from BorrowedBooks where BookId = " + bookIdEntry.get())
        cursor.execute("update BookList set Availability = 'Available' where BookId = " + bookIdEntry.get())
        cursor.execute("update StudentInfo set BorrowedBooks -= 1 where StudentId = " + studentIdEntry.get())
        cursor.execute("select * from StudentInfo")
        firstBookList = []
        for row in cursor:
            firstBookList.append(str(row[5]))
        if bookIdEntry.get() in firstBookList:
            cursor.execute("update StudentInfo set FirstBook = NULL where StudentId = " + studentIdEntry.get())
        cursor.execute("select * from StudentInfo")
        secondBookList = []
        for row in cursor:
            secondBookList.append(str(row[6]))
        if bookIdEntry.get() in secondBookList:
            cursor.execute("update StudentInfo set SecondBook = NULL where StudentId = " + studentIdEntry.get())
        cursor.execute("select * from StudentInfo")
        thirdBookList = []
        for row in cursor:
            thirdBookList.append(str(row[7]))
        if bookIdEntry.get() in thirdBookList:
            cursor.execute("update StudentInfo set ThirdBook = NULL where StudentId = " + studentIdEntry.get())
        if len(firstBookList) == 0 and len(secondBookList) == 0 and len(thirdBookList) == 0:
            newWindow = Toplevel(root)
            newWindow.geometry("300x300")
            newWindow['background'] = "#EFEDE1"
            newWindow.title("Book Error")
            errorLabel = Label(newWindow,
                               height=2, width=40,
                               bg='#007777', fg='#ffffff',
                               text="There are no book registered to the student.")
            errorLabel.place(x=8,
                             y=130)

        conn.commit()
        conn.close()

    def returnBook():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from BorrowedBooks where BookId = " + bookIdEntry.get())
        x = dt.datetime.now()
        x = str(x)
        year = (x[0:4])
        month = (x[5:7])
        if month.startswith("0"):
            month = month[1:2]
        day = (x[8:10])
        if day.startswith("0"):
            day = day[1:2]
        nowYear = int(year)
        nowMonth = int(month)
        nowDay = int(day)
        nowDate = dt.date(nowYear, nowMonth, nowDay)
        cursor.execute("select * from BorrowedBooks where BookId = " + bookIdEntry.get())
        returnDateList = []
        for row in cursor:
            returnDateList.append(row[3])
        cursor.execute("select * from BorrowedBooks where BookId = " + bookIdEntry.get())
        bookIdList = []
        for row in cursor:
            bookIdList.append(str(row[0]))
        if bookIdEntry.get() not in bookIdList:
            bookReturnNoBook()
        else:
            returnDateFromList = returnDateList[0]
            returnDateFromList = returnDateFromList.split("/")
            returnDay = int(returnDateFromList[0])
            returnMonth = int(returnDateFromList[1])
            returnYear = int(returnDateFromList[2])
            returnDate = dt.date(returnYear, returnMonth, returnDay)
            dateDifferance = nowDate - returnDate
            dateDifferance = str(dateDifferance)
            dateDifferance = dateDifferance.split(" ")
            dayDifferance = dateDifferance[0]
            dayDifferance = str(dayDifferance)
            if not dayDifferance.startswith("-"):
                conn = pypyodbc.connect('Driver={SQL Server};'
                                        'Server=DESKTOP-V06V6RC;'
                                        'Database=libraryManagement;'
                                        'Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute("update StudentInfo set Penalty = (?) where StudentId = (?)",
                               (dayDifferance, studentIdEntry.get()))
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from BorrowedBooks")
        bookIdList = []
        studentIdList = []
        for row in cursor:
            bookIdList.append(str(row[0]))
            studentIdList.append(str(row[1]))
        if bookIdEntry.get() in bookIdList and studentIdEntry.get() in studentIdList:
            returned()
        if studentIdEntry.get() not in studentIdList:
            bookReturnNoStudent()
        conn.commit()
        conn.close()

    def bookReturnNoBook():
        newWindow = Toplevel(root)
        newWindow.geometry("300x300")
        newWindow['background'] = "#EFEDE1"
        newWindow.title("Book Error")
        errorLabel = Label(newWindow,
                           height=2, width=40,
                           bg='#007777', fg='#ffffff',
                           text="Book is not found")
        errorLabel.place(x=8,
                         y=130)

    def bookReturnNoStudent():
        newWindow = Toplevel(root)
        newWindow.geometry("300x300")
        newWindow['background'] = "#EFEDE1"
        newWindow.title("Student Error")
        errorLabel = Label(newWindow,
                           height=2, width=40,
                           bg='#007777', fg='#ffffff',
                           text="Student is not found")
        errorLabel.place(x=8,
                         y=130)

    bookReturnButton = Button(newWindow,
                              height=2, width=16,
                              text="Book Return",
                              command=returnBook,
                              bg='#007777', fg='#ffffff')
    bookReturnButton.place(x=130,
                           y=260)


def openWindowAddBook():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Add Book")
    addBookLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#770064',fg='#ffffff',
                             text = "Add Book")
    addBookLabel.pack(fill="x")

    # Book ID part
    bookIDLabel = Label(newWindow,
          height=4, width=40,
          bg='#770064',fg='#ffffff')
    bookIDLabel.place(x=50,
                      y=50)
    bookIdText = Label(bookIDLabel,
                       text = "Book ID",
                       bg='#770064', fg='#ffffff')
    bookIdText.place(x=10,
                     y=20)
    bookIdEntry = Entry(bookIDLabel,
                        width=30)
    bookIdEntry.place(x=80,
                      y=20)

    # Book Title part
    bookTitleLabel = Label(newWindow,
          height=4, width=40,
          bg='#770064',fg='#ffffff')
    bookTitleLabel.place(x=50,
                         y=130)
    bookTitleText = Label(bookTitleLabel,
                       text = "Book Title",
                       bg='#770064', fg='#ffffff')
    bookTitleText.place(x=10,
                        y=20)
    bookTitleEntry = Entry(bookTitleLabel,
                        width=30)
    bookTitleEntry.place(x=80,
                      y=20)

    # Author part
    authorLabel = Label(newWindow,
          height=4, width=40,
          bg='#770064',fg='#ffffff')
    authorLabel.place(x=50,
                      y=210)
    authorText = Label(authorLabel,
                       text = "Author",
                       bg='#770064', fg='#ffffff')
    authorText.place(x=10,
                     y=20)
    authorEntry = Entry(authorLabel,
                        width=30)
    authorEntry.place(x=80,
                      y=20)

    # Page part
    pageLabel = Label(newWindow,
          height=4, width=40,
          bg='#770064',fg='#ffffff')
    pageLabel.place(x=50,
                      y=290)
    pageText = Label(pageLabel,
                       text = "Page",
                       bg='#770064', fg='#ffffff')
    pageText.place(x=10,
                     y=20)
    pageEntry = Entry(pageLabel,
                        width=30)
    pageEntry.place(x=80,
                      y=20)

    def addBook():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO BookList (BookId, BookTitle, Author, Page, Availability) VALUES (?,?,?,?,?)",
                           [(bookIdEntry.get()),(bookTitleEntry.get()),(authorEntry.get()),(pageEntry.get()),"Available"])
        conn.commit()
        conn.close()


    addBookButton = Button(newWindow,
                              height=2, width=16,
                              text="Add Book",
                              command=addBook,
                              bg='#770064', fg='#ffffff')
    addBookButton.place(x=130,
                           y=360)


def openWindowDeleteBook():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Delete Book")
    deleteBookLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#3C0077',fg='#ffffff',
                             text = "Delete Book")
    deleteBookLabel.pack(fill="x")

    # Delete Book part
    deleteBookLabel = Label(newWindow,
          height=4, width=40,
          bg='#3C0077',fg='#ffffff')
    deleteBookLabel.place(x=50,
                      y=70)
    deleteBookText = Label(deleteBookLabel,
                       text = "Book ID",
                       bg='#3C0077', fg='#ffffff')
    deleteBookText.place(x=10,
                     y=20)
    deleteBookEntry = Entry(deleteBookLabel,
                        width=30)
    deleteBookEntry.place(x=80,
                      y=20)

    def deleteBookNoBook():
        newWindow = Toplevel(root)
        newWindow.geometry("300x300")
        newWindow['background'] = "#EFEDE1"
        newWindow.title("Student Error")
        errorLabel = Label(newWindow,
                           height=2, width=40,
                           bg='#3C0077', fg='#ffffff',
                           text="Book is not found")
        errorLabel.place(x=8,
                         y=130)

    def deleteBook():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from BookList")
        bookIdList = []
        for row in cursor:
            bookIdList.append(str(row[0]))
        if deleteBookEntry.get() not in bookIdList:
            deleteBookNoBook()
        cursor.execute("delete from BookList where BookId= " + deleteBookEntry.get())
        conn.commit()
        conn.close()

    deleteBookButton = Button(newWindow,
                              height=2, width=16,
                              text="Delete Book",
                              command=deleteBook,
                              bg='#3C0077',fg='#ffffff')
    deleteBookButton.place(x=130,
                      y=160)


def openWindowAdminLogin():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Admin Login")
    adminLoginLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#993636',fg='#ffffff',
                             text = "Admin Login")
    adminLoginLabel.pack(fill="x")

# Admin ID part
    adminUsernameLabel = Label(newWindow,
          height=4, width=40,
          bg='#993636',fg='#ffffff')
    adminUsernameLabel.place(x=50,
                      y=70)
    adminUsernameText = Label(adminUsernameLabel,
                       text = "Username",
                       bg='#993636', fg='#ffffff')
    adminUsernameText.place(x=10,
                     y=20)
    adminUsernameEntry = Entry(adminUsernameLabel,
                        width=30)
    adminUsernameEntry.place(x=80,
                      y=20)

    # Admin Password part
    adminPasswordLabel = Label(newWindow,
          height=4, width=40,
          bg='#993636',fg='#ffffff')
    adminPasswordLabel.place(x=50,
                         y=150)
    adminPasswordText = Label(adminPasswordLabel,
                       text = "Password",
                       bg='#993636', fg='#ffffff')
    adminPasswordText.place(x=10,
                        y=20)
    adminPasswordEntry = Entry(adminPasswordLabel,
                         show="*",
                        width=30)
    adminPasswordEntry.place(x=80,
                      y=20)

    def adminError():
        newWindow = Toplevel(root)
        newWindow.geometry("300x300")
        newWindow['background'] = "#EFEDE1"
        newWindow.title("Admin Error")
        errorLabel = Label(newWindow,
                           height=2, width=40,
                           bg='#993636', fg='#ffffff',
                           text="Admin is not found")
        errorLabel.place(x=8,
                         y=130)

    def adminLoginControl():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from adminInfo")
        adminUsernameList = []
        adminPasswordList = []
        global adminLoginControlFlag
        adminLoginControlFlag = 0
        for row in cursor:
            adminUsernameList.append(str(row[0]))
        cursor.execute("select * from adminInfo")
        for row in cursor:
            adminPasswordList.append(str(row[1]))
        if adminUsernameEntry.get() in adminUsernameList and adminPasswordEntry.get() in adminPasswordList:
            switchOn(addBookButton)
            switchOn(deleteBookButton)
            switchOff(studentLoginButton)
            switchOff(studentLogoutButton)
            switchOn(adminLogoutButton)
            switchOff(adminLoginButton)
        else:
            adminError()
            switchOff(adminLogoutButton)
            switchOn(adminLoginButton)
        conn.commit()
        conn.close()

    loginButton = Button(newWindow,
                              height=2, width=16,
                              text="Login",
                              command=adminLoginControl,
                              bg='#993636', fg='#ffffff')
    loginButton.place(x=130,
                           y=240)


def openWindowStudentLogin():
    newWindow = Toplevel(root)
    newWindow.geometry("400x400")
    newWindow['background']="#EFEDE1"
    newWindow.title("Student Login")
    studentLoginLabel = Label(newWindow,
                             height=2, width=40,
                             bg='#359034',fg='#ffffff',
                             text = "Student Login")
    studentLoginLabel.pack(fill="x")

# Student ID part
    studentIdLabel = Label(newWindow,
          height=4, width=40,
          bg='#359034',fg='#ffffff')
    studentIdLabel.place(x=50,
                      y=70)
    studentIdText = Label(studentIdLabel,
                       text = "Student ID",
                       bg='#359034', fg='#ffffff')
    studentIdText.place(x=10,
                     y=20)

    studentIdEntry = Entry(studentIdLabel,
                        width=30)
    studentIdEntry.place(x=80,
                      y=20)

    studentPasswordLabel = Label(newWindow,
          height=4, width=40,
          bg='#359034',fg='#ffffff')
    studentPasswordLabel.place(x=50,
                         y=150)
    studentPasswordText = Label(studentPasswordLabel,
                       text = "Password",
                       bg='#359034', fg='#ffffff')
    studentPasswordText.place(x=10,
                        y=20)
    studentPasswordEntry = Entry(studentPasswordLabel,
                            show = "*",
                        width=30)
    studentPasswordEntry.place(x=80,
                      y=20)

    def studentError():
        newWindow = Toplevel(root)
        newWindow.geometry("300x300")
        newWindow['background'] = "#EFEDE1"
        newWindow.title("Student Error")
        errorLabel = Label(newWindow,
                           height=2, width=40,
                           bg='#359034', fg='#ffffff',
                           text="Student is not found")
        errorLabel.place(x=8,
                         y=130)

    def studentLoginControl():
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from studentInfo")
        studentIdListLogin = []
        studentPasswordList = []
        global studentLoginControlFlag
        studentLoginControlFlag = 0
        for row in cursor:
            studentIdListLogin.append(str(row[0]))
        cursor.execute("select * from studentInfo")
        for row in cursor:
            studentPasswordList.append(str(row[4]))
        if studentIdEntry.get() in studentIdListLogin and studentPasswordEntry.get() in studentPasswordList:
            switchOn(borrowBooksButton)
            switchOn(bookReturnButton)
            switchOff(adminLoginButton)
            switchOff(adminLogoutButton)
            switchOn(studentLogoutButton)
            switchOff(studentLoginButton)
            switchOn(myProfileButton)
            conn = pypyodbc.connect('Driver={SQL Server};'
                                    'Server=DESKTOP-V06V6RC;'
                                    'Database=libraryManagement;'
                                    'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO LoginedStudent (StudentId, StudentPassword) VALUES (?,?)",
                           [(studentIdEntry.get()), (studentPasswordEntry.get())])

            conn.commit()
            conn.close()
        else:
            studentError()
            switchOff(studentLogoutButton)
            switchOn(studentLoginButton)

    loginButton = Button(newWindow,
                              height=2, width=16,
                              text="Login",
                              command=studentLoginControl,
                              bg='#359034', fg='#ffffff')
    loginButton.place(x=130,
                           y=240)


def adminLogout():
    global adminLoginControlFlag
    if adminLoginControlFlag == 0:
        switchOff(addBookButton)
        switchOff(deleteBookButton)
        switchOn(studentLoginButton)
        switchOn(adminLoginButton)
        switchOff(studentLogoutButton)
        switchOff(adminLogoutButton)


def studentLogout():
    global studentLoginControlFlag
    if studentLoginControlFlag == 0:
        switchOff(borrowBooksButton)
        switchOff(bookReturnButton)
        switchOn(adminLoginButton)
        switchOn(studentLoginButton)
        switchOff(adminLogoutButton)
        switchOff(studentLogoutButton)
        switchOff(myProfileButton)
        conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-V06V6RC;'
                                'Database=libraryManagement;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()

        cursor.execute("delete LoginedStudent")
        conn.commit()
        conn.close()

def openWindowMyProfile():
    newWindow = Toplevel(root)
    newWindow.geometry("400x500")
    newWindow['background'] = "#EFEDE1"
    newWindow.title("My Profile")

    conn = pypyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-V06V6RC;'
                            'Database=libraryManagement;'
                            'Trusted_Connection=yes;')
    cursor = conn.cursor()
    loginedStudentIdList = []
    cursor.execute("select * from LoginedStudent")
    for row in cursor:
        loginedStudentIdList.append(str(row[0]))


    cursor = conn.cursor()
    loginedStudentPasswordList = []
    cursor.execute("select * from LoginedStudent")
    for row in cursor:
        loginedStudentPasswordList.append(str(row[1]))


    cursor = conn.cursor()
    #loginedStudentId = (loginedStudentIdList[0])
    nameSurnameList = []
    firstBookList = []
    secondBookList = []
    thirdBookList = []
    penaltyList = []
    cursor.execute("select * from StudentInfo where StudentId = " + loginedStudentIdList[0])
    for row in cursor:
        nameSurnameList.append(str(row[1]))
        firstBookList.append(str(row[5]))
        secondBookList.append(str(row[6]))
        thirdBookList.append(str(row[7]))
        penaltyList.append(str(row[3]))
    global loginedStudentNameSurname
    global loginedStudentFirstBook
    global loginedStudentSecondBook
    global loginedStudentThirdBook
    global loginedStudentPenalty
    loginedStudentNameSurname = nameSurnameList[0]
    loginedStudentFirstBook = firstBookList[0]
    loginedStudentSecondBook = secondBookList[0]
    loginedStudentThirdBook = thirdBookList[0]
    loginedStudentPenalty = penaltyList[0]
    cursor.execute("select * from LoginedStudent")
    loginedStudent = []
    for row in cursor:
        loginedStudent.append(str(row[0]))
    cursor.execute("select FirstBook from StudentInfo where StudentId = " + loginedStudent[0])
    firstBookTitleList = []
    for row in cursor:
        firstBookTitleList.append(str(row[0]))
    firstBookTitle = firstBookTitleList[0]
    cursor.execute("select * from LoginedStudent")
    loginedStudent = []
    for row in cursor:
        loginedStudent.append(str(row[0]))
    cursor.execute("select SecondBook from StudentInfo where StudentId = " + loginedStudent[0])
    secondBookTitleList = []
    for row in cursor:
        secondBookTitleList.append(str(row[0]))
    secondBookTitle = secondBookTitleList[0]
    cursor.execute("select * from LoginedStudent")
    loginedStudent = []
    for row in cursor:
        loginedStudent.append(str(row[0]))
    cursor.execute("select ThirdBook from StudentInfo where StudentId = " + loginedStudent[0])
    thirdBookTitleList = []
    for row in cursor:
        thirdBookTitleList.append(str(row[0]))
    thirdBookTitle = thirdBookTitleList[0]

    myProfileLabel = Label(newWindow,
                         height=2, width=40,
                         bg='#359034', fg='#ffffff',
                         text="My Profile")
    myProfileLabel.pack(fill="x")

    # Name part
    nameSurnameLabel = Label(newWindow,
                        height=4, width=40,
                        bg='#359034', fg='#ffffff')
    nameSurnameLabel.place(x=50,
                      y=50)
    nameText = Label(nameSurnameLabel,
                       text="Name",
                       bg='#359034', fg='#ffffff')
    nameText.place(x=10,
                     y=10)
    nameSurnameDataLabel = Label(nameSurnameLabel,
                        text = loginedStudentNameSurname,
                        width=20)
    nameSurnameDataLabel.place(x=80,
                      y=20)


    # Surname part
    surnameText = Label(nameSurnameLabel,
                     text="Surname",
                     bg='#359034', fg='#ffffff')
    surnameText.place(x=10,
                   y=30)

    # Book 1 part
    book1Label = Label(newWindow,
                           height=4, width=40,
                           bg='#359034', fg='#ffffff')
    book1Label.place(x=50,
                         y=130)
    book1Text = Label(book1Label,
                          text="Book 1",
                          bg='#359034', fg='#ffffff')
    book1Text.place(x=10,
                        y=20)
    bookTitleDataLabel = Label(book1Label,
                        text = firstBookTitle,
                           width=20)
    bookTitleDataLabel.place(x=80,
                         y=20)

    # Book 2 part
    book2Label = Label(newWindow,
                        height=4, width=40,
                        bg='#359034', fg='#ffffff')
    book2Label.place(x=50,
                      y=210)
    book2Text = Label(book2Label,
                       text="Book 2",
                       bg='#359034', fg='#ffffff')
    book2Text.place(x=10,
                     y=20)
    book2DataLabel = Label(book2Label,
                        text = secondBookTitle,
                        width=20)
    book2DataLabel.place(x=80,
                      y=20)

    # Book 3 part
    book3Label = Label(newWindow,
                      height=4, width=40,
                      bg='#359034', fg='#ffffff')
    book3Label.place(x=50,
                    y=290)
    book3Text = Label(book3Label,
                     text="Book 3",
                     bg='#359034', fg='#ffffff')
    book3Text.place(x=10,
                   y=20)
    book3DataLabel = Label(book3Label,
                        text = thirdBookTitle,
                      width=20)
    book3DataLabel.place(x=80,
                    y=20)


    # Penalty part
    penaltyLabel = Label(newWindow,
                      height=4, width=40,
                      bg='#359034', fg='#ffffff')
    penaltyLabel.place(x=50,
                    y=370)
    penaltyText = Label(penaltyLabel,
                     text="Penalty",
                     bg='#359034', fg='#ffffff')
    penaltyText.place(x=10,
                   y=20)
    penaltyDataLabel = Label(penaltyLabel,
                        text = loginedStudentPenalty,
                      width=20)
    penaltyDataLabel.place(x=80,
                    y=20)


welcomeLabel = Label(root,
                         text="Welcome to Library System",
                         height = 4, width = 10,
                         bg='#775600', fg='#ffffff')
welcomeLabel ['font'] = fontIntro
welcomeLabel.pack(fill="x")

adminLoginButton = Button(root,
                         text="Admin",
                         height = 5, width = 30,
                         bg='#993636', fg='#ffffff',command=openWindowAdminLogin)
adminLoginButton.place(x=100,
                    y=200)
adminLoginButton ['font'] = fontSize

adminLogoutButton = Button(root,
                         text="Admin Logout",
                         height = 2, width = 12,
                           command=adminLogout,
                         bg='#993636', fg='#ffffff')
adminLogoutButton.place(x=160,
                    y=300)
adminLogoutButton ['font'] = fontSize

myProfileButton = Button(root,
                              text="My Profile",
                              height=5, width=30,
                              bg='#359034', fg='#ffffff',command=openWindowMyProfile)
myProfileButton.place(x=700,
                           y=350)
myProfileButton['font'] = fontSize

studentLoginButton = Button(root,
                         text="Student",
                         height = 5, width = 30,
                         bg='#359034', fg='#ffffff',command=openWindowStudentLogin)
studentLoginButton.place(x=700,
                    y=200)
studentLoginButton ['font'] = fontSize

studentLogoutButton = Button(root,
                         text="Student Logout",
                         height = 2, width = 12,
                             command=studentLogout,
                         bg='#359034', fg='#ffffff')
studentLogoutButton.place(x=760,
                    y=300)
studentLogoutButton ['font'] = fontSize

viewBooksButton = Button(root,
                         text="View Books",
                         height = 5, width = 30,
                         bg='#005677', fg='#ffffff',command=openWindowViewBooks)
viewBooksButton.place(x=400,
                    y=100)
viewBooksButton ['font'] = fontSize

borrowBooksButton = Button(root,
                         text="Borrow Books",
                         height = 5, width = 30,
                         bg='#667700', fg='#ffffff',command=openWindowBorrowBooks)
borrowBooksButton.place(x=400,
                    y=200)
borrowBooksButton ['font'] = fontSize

bookReturnButton = Button(root,
                         text="Book Return",
                         height = 5, width = 30,
                         bg='#007777', fg='#ffffff',command=openWindowBookReturn)
bookReturnButton.place(x=400,
                    y=300)
bookReturnButton ['font'] = fontSize

addBookButton = Button(root,
                         text="Add Book",
                         height = 5, width = 30,
                         bg='#770064', fg='#ffffff',command=openWindowAddBook)
addBookButton.place(x=400,
                    y=400)
addBookButton ['font'] = fontSize

deleteBookButton = Button(root,
                         text="Delete Book",
                         height = 5, width = 30,
                         bg='#3C0077', fg='#ffffff',command=openWindowDeleteBook)
deleteBookButton.place(x=400,
                    y=500)
deleteBookButton ['font'] = fontSize

def switchOff(x):
    x["state"] = DISABLED
def switchOn(x):
    x["state"] = NORMAL

switchOff(borrowBooksButton)
switchOff(bookReturnButton)
switchOff(addBookButton)
switchOff(deleteBookButton)
switchOff(adminLogoutButton)
switchOff(studentLogoutButton)
switchOff(myProfileButton)
conn.commit()
conn.close()
root.mainloop()
