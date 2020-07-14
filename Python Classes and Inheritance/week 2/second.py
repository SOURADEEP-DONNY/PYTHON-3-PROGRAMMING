class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return '"{}" by {}'.format(self.title,self.author)

class PaperBook(Book):
    def __init__(self,title,author,numPages):
        Book.__init__(self,title,author)
        self.numPages=numPages

class Ebook(Book):
    def __init__(self,title,author,size):
        Book.__init__(self,title,author)
        self.size=size

donny=Ebook('Harry Potter','J.K Rowling','2 MB')
print(donny)
print(donny.size)
