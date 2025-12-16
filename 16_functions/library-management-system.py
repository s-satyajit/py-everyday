library = {}

def add_books(bookId, title, author):
    library[bookId] = {"title":title, "author": author, "available": True}

def borrow_books(bookId):
    if library.get(bookId) and library[bookId]["available"]:
        library[bookId]["available"] = False

def return_books(bookId):
    if library.get(bookId):
        library[bookId]["available"] = True