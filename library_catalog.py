"""Represents a single book with a title, author, year, and checkout status."""

# 1. Book Class
class Book:
    """Represents a physical book in the catelog."""
    def __init__(self, title, author, year):
        # Validate that year is a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")

        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False # Starts as false

    def check_out(self):
        """Mark the physical book as checked out"""
        self.checked_out = True

    def return_book(self):
        """Mark the physical book as returned/available."""
        self.checked_out = False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"[{status}] '{self.title}' by {self.author} ({self.year})"

# 2. EBook Class (Inherits from Book)
class EBook(Book):
    """Represents a digital ebook with multi-user checkout capability."""

    def __init__(self, title, author, year, file_size_mb):
        # Pass the common attributes to the parent Book Class
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.checkout_count = 0   # Using counter instead of boolean

    def check_out(self):
        """Override: EBooks can be checked out simultaneously by multiple people."""
        self.checkout_count += 1

    def __repr__(self):
        return f"[EBook ({self.file_size_mb} MB) - Downloads: {self.checkout_count}] '{self.title}' by {self.author} ({self.year})"

# 3. Catalog Class

class Catalog:
    """Manages a collection of physical books and ebooks."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book or Ebook instance to the catalog."""
        self.books.append(book)

    def search_by_author(self, author):
        """Returns all books written by a specific author (case insensitive)."""
        return [b for b in self.books if author.lower() in b.author.lower()]

    def search_by_title(self, keyword):
        """Return all books where the keyword appears in the title (case insensitive)"""
        return [b for b in self.books if keyword.lower() in b.title.lower()]

    def get_available(self):
        """Return all available books. EBooks are always available."""
        available_list = []
        for book in self.books:
            # EBooks are instances of EBook and are always available
            if isinstance(book, EBook):
                available_list.append(book)
            elif not book.checked_out:
                available_list.append(book)
        return available_list

    def summary(self):
        """Print a full summary of the catalog collection."""
        print("\n Catalog Summary")
        print(f"Total items: {len(self.books)}")
        for book in self.books:
            print(f"   {book}")

# Test execution

catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search results = catalog.search_by_title("python")
results = catalog.search_by_title("python")
print(results)

#Check Out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()