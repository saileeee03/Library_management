import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Library data
books = {
    121: {"name": "Harry Potter", "status": "Available"},
    122: {"name": "The Alchemist", "status": "Issued"},
    123: {"name": "Wings of Fire", "status": "Available"},
    124: {"name": "Rich Dad Poor Dad", "status": "Issued"},
    125: {"name": "The Lord of the Rings", "status": "Issued"},
    126: {"name": "The Little Prince", "status": "Available"},
    127: {"name": "Paper Things", "status": "Available"}
}

def check_book(book_id):
    try:
        book_id = int(book_id)
        if book_id in books:
            book = books[book_id]
            return f"Book Name: {book['name']}, Status: {book['status']}"
        return "Book not available in library"
    except ValueError:
        return "Invalid book ID"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    book_id = request.form.get('book', '')
    result = check_book(book_id)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
