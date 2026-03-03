from Person import Person

class Author(Person):
    def __init__(self, name, address, email, phone, description):
        super().__init__(name, address, email, phone)
        self.description = description
