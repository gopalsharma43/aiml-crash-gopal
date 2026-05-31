# This program demonstrates inheritance using a library system.

class LibraryItem:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}"


class Book(LibraryItem):

    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def describe(self):
        return (
            f"Book -> Title: {self.title}, "
            f"Author: {self.author}, "
            f"Pages: {self.pages}"
        )


class EBook(LibraryItem):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def describe(self):
        return (
            f"EBook -> Title: {self.title}, "
            f"Author: {self.author}, "
            f"File Size: {self.file_size} MB"
        )


book1 = Book(
    "Python Programming",
    "John Smith",
    450
)

ebook1 = EBook(
    "Machine Learning Guide",
    "Alice Brown",
    12.5
)

print(book1.describe())
print(ebook1.describe())