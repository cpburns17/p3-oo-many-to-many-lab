class Author:
    def __init__(self, name) -> None:
        self.name = name
        self.contracts_list = []
        self.books_list = []

    def contracts(self):
        return self.contracts_list

    def books(self):
        temp_book_list =[]
        for contract in self.contracts_list:
            temp_book_list.append(contract.book)
        return temp_book_list
    
    def sign_contract(self, book, date, royalties):
        pass

    def total_royalties(self):
        pass



    

class Book:
    def __init__(self, title) -> None:
        self.title = title
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list


class Contract:
    def __init__(self, author, book, date, royalties) -> None:
        self.author = author
        author.contracts_list.append(self)
        self.book = book
        book.contracts_list.append(self)
        self.date = date
        self.royalties = royalties 

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception()
        
    @property
    def book(self):
        return self._book 
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception()
        
    @property
    def date(self):
        return self._date 
    
    @date.setter
    def date(self, date):
        if type(date) == str:
            self._date = date
        else: 
            raise Exception()
        
    @property
    def royalties(self):
        return self._royalties 
    
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) == int:
            self._royalties = royalties
        else:
            raise Exception()
        

