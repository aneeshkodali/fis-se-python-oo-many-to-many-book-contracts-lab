class Author:
    
    # store all authors
    all = []

    # initialize author
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # return author contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    # return author books (via contracts)
    def books(self):
        # get contracts
        contracts = self.contracts()
        # get unique authors from contracts
        books = {contract.book for contract in contracts}
        return books
    
    # create new contract record
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # get royalty amount for author contracts
    def total_royalties(self):
        # get contracts
        contracts = self.contracts()
        # get royalties from contracts
        royalties = [contract.royalties for contract in contracts]
        return sum(royalties)
    

class Book:
    
    # store books
    all = []

    # initialize book
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    # return book contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # return book authors (via contracts)
    def authors(self):
        # get contracts
        contracts = self.contracts()
        # get unique authors from contracts
        authors = {contract.author for contract in contracts}
        return authors


class Contract:
    
    # store contracts
    all = []

    # return Contract records for a given date
    @classmethod
    def contracts_by_date(cls, date):
        return [
                contract
                for contract in Contract.all
                if contract.date == date
            ]

    # initialize
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author property
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    # book property
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    # date property
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    # royalties property
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value