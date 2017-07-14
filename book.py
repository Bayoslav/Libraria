import datetime
from peewee import *
db = SqliteDatabase('books.db')
class Book(Model):
    name = CharField()
    writer = CharField()
    isbn = CharField()
    date = DateField()
    is_taken = BooleanField()

    class Meta:
        database = db


    def newbook(self):
        self.name = input("Name of the book:")
        self.writer = input("Writer of the booK:")
        self.isbn = (int(input("ISBN: ")))
        dudud = Book(name=self.name,writer=self.writer, isbn=self.isbn, date=datetime.date.today(),is_taken=False)
        dudud.save()
    def ispis(self):
        bood = Book.select()
        for boom in bood:
            print("Name: ", boom.name, " ","Writer: ", boom.writer)
    def cita(self):
        pass
    def citodknj(self):
        mekik = (int(input("Enter the book number to search:")))
        adab = Book.get(Book.id==mekik)
        print(adab.name, " ", adab.isbn)

        #booknum = 123
        #self.num = (int(input()))
        #df = pd.read_csv('book.dat', sep=" ", header = None)
        #if(df[3]==333):
        #   print(df)


