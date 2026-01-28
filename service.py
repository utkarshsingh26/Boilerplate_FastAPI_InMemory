from models import Genre

class BookService:
    def __init__(self, repo: "BookRepository"):
        self.repo = repo
    
    def process_new_book(self, title, book):
        if not self.repo.exists(title):
            self.repo.save_book(title, book)
        else:
            raise ValueError("Book already exists")
    
    def purchase(self, title):
        if self.repo.exists(title):
            current_stock_count = self.repo.get_all_books()[title].stock_count

            if current_stock_count == 0:
                raise ValueError("Book out of stock")
            else:
                self.repo.get_all_books()[title].stock_count -= 1

        else:
            raise ValueError("Book does not exist")
    
    def catalog(self):
        all_books = self.repo.get_all_books().items()
        for title, book in all_books:
            print(book)
            if book.stock_count <= 3:
                book.price = 1.2 * book.price
                if book.genre == Genre.FANTASY:
                    book.price = 0.9 * book.price
        return all_books
