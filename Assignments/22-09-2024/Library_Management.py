#Store books Information
#search_term = input("Enter title, author, or genre to search: ")
books = [{'ID': 1, 'Title': 'Crash Book', 'Author': 'Eric', 'Genre': 'Programming', 'Availability': 'Available'},
         {'ID': 2, 'Title': 'Fundamentals of Database Systems', 'Author': 'Thomos Connely', 'Genre': 'Database', 'Availability': 'Available'},
         {'ID': 3, 'Title': 'Pride and Prejudice', 'Author': 'Jane Austen', 'Genre': 'Classic', 'Availability': 'Checkout'},
         {'ID': 4, 'Title': 'The Lord of the Rings', 'Author': 'J.R.R. Tolkien', 'Genre': 'Adventure', 'Availability': 'Available'},
         {'ID': 5, 'Title': 'Harry Potter and the Philosophers Stone', 'Author': 'J.K. Rowling', 'Genre': 'Fantasy', 'Availability': 'Checkout'}  
        ]
 

#Store users information
users = [{'userid': 1, 'name': 'Arham', 'borrowed_list': [] },
         {'userid': 2, 'name': 'Eshaal', 'borrowed_list': [] }]

#Show all books
def show_books():
    print("\nAll Books:")
    for book in books:
         print(f" {book['ID']} . \"{book['Title']}\" by {book['Author']} ({book['Availability']}) ")

# Function to search for a book by title, author, or genre
def search_books():
    search_term = input("Enter title, author, or genre to search: ").lower()
    found_books = [book for book in books if search_term in book['Title'].lower() or search_term in book['Author'].lower() or search_term in book['Genre'].lower()]
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']} ({book['Availability']})")
    else:
        print("No books found.")
    print("----------------------------------------") 

#Borrow a book
def borrow(userid, bookid):
    for user in users:
        if user['userid'] == userid:
            user['borrowed_list'].append(books[0])
            print(f"{user['name']} has borrowed {books[0]['Title']}.")
            break

#Return book
def return_books(bookid, userid):
    founduser = None
    for u in users:
     if u['userid'] == userid:
        founduser = u
        break
    foundbook = None
    for b in books:
        if b['ID'] == bookid:
            foundbook = b
            break
    print(f"The book: {foundbook['Title']} for the user {founduser['name']} has been returned sucessfully")
    

# Function to view available books
def view_available_books():
    print("\nAvailable Books:")
    for book in books:
        if book['Availability'] == 'Available':
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")
    print("----------------------------------------")

#show_all_users()
def show_users():
    print("\nAll Users:")
    for user in users:
        #borrowed_books = ', '.join([book['Title'] for book in user['borrowed_list']]) if user['borrowed_list'] else "No books borrowed"
        print(f" {user['userid']} . \"{user['name']}\"")

# Main program loop
while True:
    print("\nWelcome to the Community Library System!")
    print("----------------------------------------")
    print("Please choose an option:")
    print("1. View all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all users")
    print("6. Exit")

    option = int(input("\nEnter your choice (1-6): "))

    if option == 1:
        show_books()
    elif option == 2:
        search_books()
    elif option == 3:
        userid = int(input("Enter your User ID: "))
        bookid = int(input("Enter the Book ID you want to borrow: "))
        borrow(userid, bookid)
    elif option == 4:
        userid = int(input("Enter your User ID: "))
        bookid = int(input("Enter the Book ID you want to return: "))
        return_books(bookid, userid)
    elif option == 5:
        show_users()
    elif option == 6:
        print("Exiting the Community Library System. Goodbye!")
        break  # Exit the loop, ending the program
    else:
        print("Invalid option, please choose a number between 1 and 6.")


# Function to view checked-out books
def view_checked_out_books():
    print("\nChecked Out Books:")
    for book in books:
        if book['Availability'] == 'Checked Out':
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")
    print("----------------------------------------")

  