from datetime import datetime

class Book:
    def __init__(self, name, isbn, title, author, year_of_publication,publisher, image_url):
        self.name = name
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.image_url = image_url

class User:
    def __init__(self, serial_no, address, area_code):
        self.serial_no = serial_no
        self.address = address
        self.area_code = area_code
class BooksRatings:
    def __init__(self,serial_no,isbn, rating):
        self.serial_no = serial_no
        self.isbn = isbn
        self.rating = rating
class Library:
    def __init__(self):
        self.users = {}
        self.book_list = {}
        self.time_record_list = {}

    def add_book(self, book):
        self.book_list[book.isbn] = {'book_info': book, 'ratings': []}
        print("Book is successfully added to the library.\n")

    def del_book(self, isbn):
        self.book_list.pop(isbn)
        print("Book is successfully deleted from the library.\n")

    def update_book(self, isbn, name):
        self.book_list[isbn]['book_info'].name = name
        print("Book name is successfully updated in the library.")
        print(f"[Book name: {self.book_list[isbn]['book_info'].name}]\n")

    def check_title(self, title):
        for isbn_key, book_info in self.book_list.items():
            book = book_info['book_info']
            if book.title == title:
                print(f"'{title}' is present in the library.\n")
                return
        print(f"Sorry! '{title}' book is not present in the library.\n")

    def check_isbn(self, isbn):
        for key, value in self.book_list.items():
            book = value['book_info']
            if book.isbn == isbn:
                print(f"Book with ISBN '{isbn}' is present in the library.\n")
                return
        print(f"Sorry! Book with ISBN '{isbn}' is not present in the library.\n")

    def add_user(self, user):
        self.users[user.serial_no] = user
        print("book is added successfully to the library:")
        print("")

    def change_user(self, serial_no, new_address, new_area_code):
        for key, value in self.users.items():
            if serial_no == value.serial_no:
                value.address = new_address
                value.area_code = new_area_code
                print("User's details changed.\n")
                return
        print("There is no such user with this serial no.\n")

    def issue_book(self, isbn, issue_date):
        if isbn not in self.time_record_list:
            self.time_record_list[isbn] = []
        self.time_record_list[isbn].append({'action': 'issue', 'date': issue_date})
        print(f"Book '{self.book_list[isbn]['book_info'].title}' with ISBN {isbn} is issued on {issue_date}\n")

    def return_book(self, isbn, return_date):
        if isbn not in self.time_record_list:
            self.time_record_list[isbn] = []
        self.time_record_list[isbn].append({'action': 'return', 'date': return_date})
        print(f"Book '{self.book_list[isbn]['book_info'].title}' with ISBN {isbn} is returned on {return_date}\n")
        #calculating late fees along with returning book.
        if isbn in self.time_record_list:
            record_list = self.time_record_list[isbn]
            issue_date = None
            return_date = None

            for record in record_list:
                if record['action'] == 'issue':
                    issue_date = datetime.strptime(record['date'], "%Y-%m-%d")
                elif record['action'] == 'return':
                    return_date = datetime.strptime(record['date'], "%Y-%m-%d")

            if issue_date and return_date:
                delta = return_date - issue_date
                if delta.days > 7:
                    late_fee = delta.days * 10
                    print(f"Late fees for '{self.book_list[isbn]['book_info'].title}' is {late_fee} INR\n")
                else:
                    print("There is no late fee for this book.\n")
            else:
                print("Incomplete record for this book. Cannot calculate late fees.\n")
        else:
            print("No record found for this book. Cannot calculate late fees.\n")

    def calculate_late_fees(self, isbn):
        if isbn in self.time_record_list:
            record_list = self.time_record_list[isbn]
            issue_date = None
            return_date = None

            for record in record_list:
                if record['action'] == 'issue':
                    issue_date = datetime.strptime(record['date'], "%Y-%m-%d")
                elif record['action'] == 'return':
                    return_date = datetime.strptime(record['date'], "%Y-%m-%d")

            if issue_date and return_date:
                delta = return_date - issue_date
                if delta.days > 7:
                    late_fee = delta.days * 10
                    print(f"Late fees for '{self.book_list[isbn]['book_info'].title}' is {late_fee} INR\n")
                else:
                    print("There is no late fee for this book.\n")
            else:
                print("Incomplete record for this book. Cannot calculate late fees.\n")
        else:
            print("No record found for this book. Cannot calculate late fees.\n")
    
    def add_rating(self, user_rating):
        isbn = user_rating.isbn
        rating = user_rating.rating
        
        for key,value in self.book_list.items():
            book = value['book_info']
            if book.isbn == isbn:
                value['ratings'].append(rating)

    def display(self):
        if(len(self.book_list)==0):
            print("No books to display!")
        for key,value in self.book_list.items():
            book = value['book_info'] 
            print(f"Title: {book.title}, ISBN: {book.isbn}, Area Code: {book.publisher}, Rating1s by users: {value['ratings']}")
    def avg_rating(self, publisher):
        total_rating = 0
        count = 0

        for key, value in self.book_list.items():
            book = value['book_info']

            if book.publisher == publisher:
                ratings = value['ratings']  
                rating_l = [int(rating) for rating in ratings]
                total_rating += sum(rating_l)  # Sum of all ratings for books from the publisher
                count += len(rating_l)  # Total number of ratings for books from the publisher

        if count > 0:
            average_rating = total_rating / count
            print(f"Average rating for Publisher {publisher} is {average_rating:.2f}\n")
        else:
            print(f"No ratings found for books from Publisher {publisher}\n")


 
    def total_books_per_year(self):
        year_count = {}
        for key,value in self.book_list.items():
            book = value['book_info']
            if book.year_of_publication == year_count:
                year_count[book.year_of_publication]+=1
            else:
                year_count[book.year_of_publication] =1
        if(len(year_count) == 0):
            print("No books available")
            return
        print("Total books per year are following:")
        for key,value in year_count.items():
            print(f"Year: {key}, Books: {value}\n")
            
    def top_five_rated_books(self):
        rating_list = {}
        for isbn, book_info in self.book_list.items():
            ratings = book_info['ratings']
            if ratings:
                # Convert the ratings to integers
                ratings = [int(rating) for rating in ratings]
                average_rating = sum(ratings) / len(ratings)
                rating_list[isbn] = average_rating

        sorted_dict = dict(sorted(rating_list.items(), key=lambda item: item[1], reverse=True))
        top_5_items = list(sorted_dict.items())[:5]
        if(len(top_5_items) == 0):
            print("No books available")
            return
        print("Top 5 rated books:")
        for isbn, rating in top_5_items:
            book = self.book_list[isbn]['book_info']
            print(f"Title: {book.title}, ISBN: {isbn}, Rating: {rating:.2f}")




def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Update Book")
        print("4. Check Book by Title")
        print("5. Check Book by ISBN")
        print("6. Add User")
        print("7. Update User")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Add Rating to book")
        print("11. Display Books")
        print("12. Calculate Average Rating")
        print("13. Calculate Total Books per Year")
        print("14. Display Top Five Books")
        print("15. Calculate late fees for a book")
        print("16. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter name: ")
            isbn = input("Enter isbn: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year_of_publication = input("Enter year_of_publication: ")
            publisher = input("Enter publisher: ")
            image_url = input("Enter image_url: ")
            book = Book(name, isbn, title, author, year_of_publication,publisher, image_url)
            print(library.add_book(book))
        elif choice == 2:
            isbn = input("Enter the ISBN of the book to be deleted:")
            print(library.del_book(isbn))
        elif choice == 3:
            isbn = input("Enter isbn: ")
            name = input("Enter name: ")
            library.update_book(isbn, name)
        elif choice == 4:
            title = input("Enter title: ")
            library.check_title(title)
        elif choice == 5:
            isbn = input("Enter isbn: ")
            library.check_isbn(isbn)
        elif choice == 6:
            serial_no = input("Enter serial no of the user: ")
            address = input("Enter address of the user: ")
            area_code = input("Enter area code of the user: ")
            user = User(serial_no, address, area_code)
            library.add_user(user)
        elif choice == 7:
            serial_no = input("Enter serial no of the user: ")
            new_address = input("Enter address of the user: ")
            new_area_code = input("Enter area code of the user: ")
            library.change_user(serial_no, new_address, new_area_code)
        elif choice == 8:
            isbn = input("Enter isbn: ")
            issue_date = input("Enter issue date: ")
            library.issue_book(isbn, issue_date)
        elif choice == 9:
            isbn = input("Enter isbn: ")
            return_date = input("Enter return date: ")
            library.return_book(isbn, return_date)
        elif choice == 10:
            srno = input("Enter serial no: ")
            isbn = input("Enter isbn: ")
            rating = input("Enter rating: ")
            user_rating = BooksRatings(srno,isbn,rating)
            library.add_rating(user_rating)
        elif choice == 11:
            library.display()
        elif choice == 12:
            publisher = input("Enter publisher: ")
            library.avg_rating(publisher)
        elif choice == 13:
            library.total_books_per_year()
        elif choice == 14:
            library.top_five_rated_books()
        elif choice == 15:
            isbn = input("Enter isbn of the book to calculate late fees: ")
            library.calculate_late_fees(isbn)
        elif choice == 16:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
