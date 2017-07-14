from peewee import *
import datetime
import Users
import book
db = SqliteDatabase('books.db')
class Relationk(Model):
    userid = ForeignKeyField(Users.User)
    bookid = ForeignKeyField(book.Book)
    dateio = DateField()
    def newrelation(self):
        amkccc = (int(input("User's number: ")))
        dadakk = (int(input("Book's number: ")))
        papap = Relationk(userid=amkccc,bookid=dadakk,dateio=datetime.date.today())
        papap.save()
    class Meta:
        database = db
kek = book.Book()
dek = Users.User()
mek = Relationk()
book.db.connect()
book.db.create_tables([kek, dek,mek],safe=True)
while(1):
    d = (int(input("dalzelisdodasknjigu majmune unesi 0 ako nes, ako os 1")))
    if(d==0):
        break
    else:
        a = (int(input("1 to add a book, 2 to add a user, 3 to read the users, 4 to read the books, 5 to read a specific book,7 to add book to the user")))
        if(a==1):
            kek.newbook()
        if(a==2):
            dek.newuser()
        if(a==3):
            dek.cita()
        if(a==4):
            kek.ispis()
        elif(a==5):
            kek.citodknj()
        elif(a==6):
            dek.readnumus()
        elif(a==7):
            mek.newrelation()
        elif(a==8):
            boos = mek.select()
            for boor in boos:
                usr = dek.get(dek.id == boor.userid).Name
                buk = kek.get(kek.id == boor.bookid).Name
                print("User Name: ",usr, " ", "Book Name: ", buk)







