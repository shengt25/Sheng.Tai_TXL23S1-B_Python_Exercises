class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages_count):
        super().__init__(name)
        self.author = author
        self.pages = pages_count

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.publisher = chief_editor

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief editor: {self.publisher}")


# Creating a book and a magazine
magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

# Printing the information
print("Magazine:")
magazine1.print_information()
print("\n")
print("Book:")
book1.print_information()
