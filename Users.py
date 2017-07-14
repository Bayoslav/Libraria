import datetime
from peewee import *
db = SqliteDatabase('books.db')
class User(Model):
    Name = CharField()
    Age = IntegerField()
    Adress = CharField()
    Phone = IntegerField()
    Datet = DateField()
    def addbook(self,num):
        pass
        #f=open('users.dat','r')

    def cita(self):
        citad = User.select()
        for korisnik in citad:
            print(korisnik.Name, " ", korisnik.Adress)
    class Meta:
        database = db
    def newuser(self):
        self.name = input("Name of the user: ")
        self.age  = (int(input("User's age: ")))
        self.adress = (input("User's adress: "))
        self.phone = (input("User's phone: "))
        dudu = User(Name=self.name,Age=self.age,Adress=self.adress,Phone=self.phone,Datet=datetime.date.today())
        dudu.save()
    def readnumus(self):
        numnum = (int(input("Enter the users number")))
        bob = User.get(User.id == numnum)
        print(bob.Name)


