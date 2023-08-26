class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.emails = []
    def add_book(self, book_title):
        self.books.append(book_title)
    def add_email(self, email_subject):
        self.emails.append(email_subject)
    def get_books(self):
        return self.books
    def get_emails(self):
        return self.emails
class Publication:
    def __init__(self, title):
        self.title = title
    def get_title(self):
        return self.title
class Book(Publication):
    def __init__(self, title, date):
        super().__init__(title)
        self.date = date
    def get_date(self):
        return self.date
class Email(Publication):
    def __init__(self, title, to):
        super().__init__(title)
        self.to = to
    def get_to(self):
        return self.to
