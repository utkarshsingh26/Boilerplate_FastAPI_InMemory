from fastapi import FastAPI, HTTPException
from models import Book
from repository import BookRepository
from service import BookService

repo = BookRepository()
service = BookService(repo)

app = FastAPI()

@app.post("/books/{title}")
def create_books(title, book: Book):
    try:
        service.process_new_book(title, book)
        return {"message": "Book added to catalog"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/purchase/{title}")
def create_books(title):
    try:
        service.purchase(title)
        return {"message": "Book purchased"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/catalog")
def get_catalog():
    try:
        result = service.catalog()
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
