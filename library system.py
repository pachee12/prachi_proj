class Library:
    def __init__(self,  list, name):
        self.name = name
        self.booklist = list
        self.bkDict = {}

    def display(self,):
        print(f"The available books are: {self.name}\n\n")
        for book in self.booklist:
            print(book,"\n")

    def donate(self, user, book):
        self.booklist.append(book)


    def lend(self, user, book):
        if book not in self.bkDict.items():
            self.bkDict.update({book:user})
            print("we have dis book")

        else:
            print(f"so srry!... the book is being used by: {self.bkDict[book]}")

    def ret(self, user, book):
        self.booklist.remove(book)

if __name__ == '__main__':
    obj = Library(['harry potter', 'flower', 'queens', 'thor', 'iron man', 'wolverine', 'python basics'], "$*$ GRANTHAM $*$ \n")
    print("*$*$*$ WELCOME TO 'GRANTHAM' $*$*$*\n")
    while True:
        print(
              "Pls select the valid option😊\n"
              "1. display books\n"
              "2.donate book\n"
              "3.lend book\n"
              "4. return book\n")
        ch = int(input())
        if ch == 1:
            obj.display()

        elif ch == 2:
            user = input("kindly register ur name\n")
            book = input("which book do uh wanna donate:\n")
            obj.donate(user, book)

        elif ch == 3:
            user = input("kindly register ur name\n")
            book = input("which book do uh wanna lend:\n")
            obj.lend(user, book)

        elif ch == 4:
            user = input("kindly register ur name\n")
            book = input("which book do uh wanna return:\n")
            obj.ret(user, book)

        else:
            print("please select a valid option")













