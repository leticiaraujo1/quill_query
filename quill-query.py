import requests
import random


def getBook(subject):
    if subject == "random":
        subject = ''
    
    x = 'https://www.googleapis.com/books/v1/volumes?q=subject:'
    url = requests.get(x + subject)
    books = url.json()
    bookData = books.get('items', [])

    randNum = random.randint(0, len(bookData)-1)

    bookTitle = bookData[randNum]["volumeInfo"]["title"]
    bookAuthor = bookData[randNum]["volumeInfo"]["authors"]

    return bookTitle, ", ".join(bookAuthor)
 
def main():
    print("---Find a perfect book for you!---")
    print("Pick a genre. It could be romance, terror, fiction, biography, fantasy, poetry or random")
    genre =  input('')
    
    try:
        bookTitle, bookAuthor = getBook(genre)
        print("You should read", bookTitle, "by", bookAuthor)
    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()

