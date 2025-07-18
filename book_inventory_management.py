from datetime import timezone, timedelta, datetime
import json

class Book:
    def __init__(self, isbn, title, author, publisher, genre, price, stock):
        if price <= 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._genre = genre
        self._price = price
        self._stock = stock
        self._rating = 0.0
        self._ratings_count = 0
        self.ratings = []
        self.units_sold = 0
        self.revenue = 0

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def ratings_count(self):
        return self._ratings_count

    @property
    def rating(self):
        return self._rating

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value

    def add_rating(self,rating):
        if 0.0 <= rating <= 5.00:
            self.ratings.append(rating)
            self._ratings_count += 1
            self._rating = (sum(self.ratings) / self._ratings_count).__round__(3)
        else:
            print("Enter the rating between 0.00 and 5.0")

    def decrease_stock(self,amount):
        if amount <= 0:
            raise ValueError("It is not possible baka.")
        elif amount > self._stock:
            raise ValueError(f"{amount} is more than {self._stock}, so it is not possible")

        self._stock -= amount

class Book_Shop:
    def __init__(self):
        self.inventory = []
        self.transaction_history = []
        self.search_history = []
        self.successful_transactions = 0
        self.unsuccessful_transactions = 0

    def validate_price_and_stock(self, price, stock):
        if price < 0:
            print("Price cannot be negative.")
            return False
        if stock < 0:
            print("Stock cannot be negative.")
            return False
        return True

    def add_book(self, isbn, title, author, publisher, genre, price, stock):
        if not self.validate_price_and_stock(price, stock):
            return

        if any(b.isbn == isbn for b in self.inventory):
            print("Book is already there cannot be added.")
            self.unsuccessful_transactions += 1
            return
        newBook = Book(isbn, title, author, publisher, genre, price, stock)
        self.inventory.append(newBook)
        print(f"{newBook.title} added successfully")

    def find_book_by_isbn(self,isbn):
        return next((book for book in self.inventory if book.isbn == isbn), None)

    def delete_book(self,isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            print(f"Book found: {book.title}")
            self.inventory.remove(book)
            self.successful_transactions += 1
            print(f"{book.title} has successfully been removed.")
        else:
            self.unsuccessful_transactions += 1
            print("Book not found.")

    def update_book(self,isbn,title=None, author=None, publisher=None, genre=None, price=None, stock=None):
        if not self.validate_price_and_stock(price, stock):
            return
        book = self.find_book_by_isbn(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if publisher:
                book.publisher = publisher
            if genre:
                book.genre = genre
            if price:
                book.price = price
            if stock:
                book.stock = stock
            self.successful_transactions += 1
            print(f"{book.title} has been updated.")
        else:
            self.unsuccessful_transactions += 1
            print("Book not found")


    def display_books(self):
        print("Book Inventory")
        print("====================================================================================")
        print(f"{'Sr.No':<8} {'ISBN':<15} {'Title':<30} {'Author':<20} {'Publisher':<20} {'Genre':<10} {'Price':<10} {'Stock':<10} {'Rating':<10}")
        print("="*80)
        for index, book in enumerate(self.inventory, start=1):
            print(f"{index:<8} {book.isbn:<15} {book.title:<30} {book.author:<20} {book.publisher:<20} {book.genre:<10} {book.price:<10.2f} {book.stock:<10} {book.rating:<10}")
        print("="*80)

    def search_book(self,search_query):
        found_book = []
        for book in self.inventory:
            if book.isbn == search_query:
                found_book.append(book)
            elif search_query.lower() in book.title.lower():
                found_book.append(book)
            elif search_query.lower() in book.author.lower():
                found_book.append(book)

        if found_book:
            for book in found_book:
                print(f"Found: Title : {book.title}, Author : {book.author} and ISBN : {book.isbn}")
        else:
            print("Book not found try again.")

    def purchase_book(self,isbn,quantity):
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("Book not found, try again.")
            self.unsuccessful_transactions += 1
            return

        if book.stock >= quantity:
            book.units_sold += quantity
            book.decrease_stock(quantity)
            print(f"You have purchased {quantity} copies of the book : {book.title}")

            transaction_type = "Purchase"
            current_time = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
            transaction_code = f"{book.isbn}-{current_time}-{transaction_type}-{quantity}"

            transaction_details = {
                "Transaction type" : transaction_type,
                "Current Time" : current_time,
                "Confirmation Code: " : transaction_code,
                "Quantity" : quantity,
                "ISBN" : book.isbn
            }

            self.transaction_history.append(transaction_details)
            self.successful_transactions += 1
        else:
            print(f"Not enough stock for the requested quantity. Available stock: {book.stock}")
            self.unsuccessful_transactions += 1

    def book_rating(self,isbn,new_rating):
        if not(0.0 <= new_rating <= 5.0):
            raise ValueError("Invalid rating. Rating must be between 0.0 and 5.0.")

        book = next((b for b in self.inventory if b.isbn == isbn), None)

        if book:
            book.add_rating(new_rating)
        else:
            print("That book you are trying to add an rating for does not exist.")


    def generate_sales(self):
        print("Sales generation")
        print("="*80)
        print(f"{'ISBN': <8}{'Title':<20}{'UnitsSold':<10}{'TotalRevenue':<10}")
        print("="*80)
        total_units_sold = 0
        total_revenue = 0

        for book in self.inventory:
            if book.units_sold > 0:
                revenue = book.units_sold * book.price
                total_units_sold += book.units_sold
                total_revenue += revenue
                print(f"{book.isbn:<8}{book.title:<20}{book.units_sold:<20}{revenue:<20.2f}")

        print("=" * 70)
        print(f"Total: {total_units_sold:<10}{total_revenue:<15.2f}")
        print("=" * 70)

    def search_book_history(self,query):
        self.search_history.append(query)

        if len(self.search_history) > 10:
            self.search_history.pop(0)

    def display_history(self):
        print("Your search history:")
        for idx, query in enumerate(self.search_history):
            print(f"{idx+1} : {query}")

    def save_inventory_to_file(self,file_name="inventory.json"):
        with open(file_name,"w") as file:
            json.dump([book.__dict__ for book in self.inventory], file)
        print("Inventory saved successfully")

    def load_inventory(self,file_name="inventory.json"):
        try:
            with open(file_name,"r") as file:
                data = json.load(file)
                for book_data in data:
                    book = Book(book_data["_isbn"], book_data["_title"],book_data["_author"],book_data["_publisher"],book_data["_genre"],book_data["_price"], book_data["_stock"])
                    self.inventory.append(book)
                print("Inventory load successfully")
        except FileNotFoundError:
            print("File not found.")

    
    def display_successful_transaction(self):
        print(self.successful_transactions)

    def display_unsuccessful_transaction(self):
        print(self.unsuccessful_transactions)



book = Book_Shop()
book.add_book("12345","Harry potter", "Vihaan K","XYZ","Rap", 22.99, 10)
book.add_book("83145","Built To Last","Sudha Murthy","Penguin","Children",7.99, 10)
book.add_book("12456","History of India","Subhashree","Random","History",24.99, 100)
book.book_rating("12345", 5)
book.book_rating("12345",4.5)
book.purchase_book("12456",1)
book.delete_book("12345")
book.update_book("12456","History of Pakistan","Subhashree", "Random","History",24.99, 100)
book.generate_sales()
book.search_book("Sudha Murthy")
book.search_book_history("The informant")
book.search_book_history("Minutes of magic")
book.search_book_history("The twelfth hour")
book.search_book_history("Blink")
book.display_history()
book.save_inventory_to_file()
book.display_books()
book.load_inventory()
book.purchase_book("83145",11)
book.display_successful_transaction()
book.display_unsuccessful_transaction()










