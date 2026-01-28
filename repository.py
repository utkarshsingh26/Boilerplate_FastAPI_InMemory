class BookRepository:
    def __init__(self):
        self.books: dict[str, "Book"] = {}
    
    def save_book(self, title: str, book: "Book"):
        self.books[title] = book
    
    def get_all_books(self):
        return self.books
    
    def exists(self, title: str):
        return title in self.books
