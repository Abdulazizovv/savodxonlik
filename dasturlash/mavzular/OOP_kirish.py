# OOP - Object Oriented Programming (Obyektga Yo'naltirilgan Dasturlash)
# OOP dasturlash paradigmasi bo'lib, unda dastur obyektlar atrofida tashkil etiladi.
# Obyektlar - bu ma'lumotlar (xususiyatlar) va funksiyalar (metodlar) to'plami bo'lib, ular birgalikda ishlaydi.


# OOP ning asosiy tushunchalari:
# 1. Sinflar (Classes): Sinf - bu obyektlarning shabloni yoki andozasi. U xususiyatlar va metodlarni aniqlaydi.
# 2. Obyektlar (Objects): Obyekt - bu sinfning konkret namunasidir. Har bir obyekt o'zining xususiyatlariga ega bo'lishi mumkin.
# 3. Meros (Inheritance): Meros - bu bir sinfning boshqa sinfdan xususiyatlar va metodlarni olishi.
# 4. Polimorfizm (Polymorphism): Polimorfizm - bu bir nechta sinflar bir xil metod nomiga ega bo'lishi mumkinligi.
# 5. Inkapsulatsiya (Encapsulation): Inkapsulatsiya - bu ma'lumotlarni va metodlarni birlashtirish va ularni tashqi kirishdan himoya qilish.

# OOP dasturlashning asosiy afzalliklari:
# - Kod qayta foydalanish: Sinflar va obyektlar qayta ishlatilishi mumkin.
# - Kod tuzilishi: OOP kod tuzilishini yaxshilaydi va uni o'qishni osonlashtiradi.
# - Murakkab tizimlarni boshqarish: OOP murakkab tizimlarni modullarga bo'lish orqali boshqarishni osonlashtiradi.



# Quyida Python dasturlash tilida OOP ning asosiy tushunchalarini ko'rsatadigan oddiy misol keltirilgan:
class Animal:
    def __init__(self, name):  # Konstruktor
        # inkapsulatsiya uchun xususiyatni private qilish mumkin:
        # self.__name = name  # private xususiyat
        self._name = name  # Xususiyat
    
    def set_name(self, name):  # Setter metod
        self._name = name
    
    def get_name(self):  # Getter metod
        return self._name
    

    def speak(self):  # Metod
        return f"{self._name} makes a sound."


class Dog(Animal):  # Meros olish
    def speak(self):  # Polimorfizm
        return f"{self.name} barks."
    
    
class Cat(Animal):  # Meros olish
    def speak(self):  # Polimorfizm
        return f"{self.name} meows."
    
    
# Obyektlar yaratish
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Metodlarni chaqirish
# print(dog.speak())  # Output: Buddy barks.
# print(cat.speak())  # Output: Whiskers meows.

























class Human:
    def __init__(self, name, age):
        self._name = name
        self.age = age
        
    
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def greeting(self):
        print(f"Salom, {self._name}")
        
    def check_age(self, min_age=15):
        if self.age >= min_age:
            print("Siz katta odamsiz")
        else:
            print("Siz kichkina odamsiz")


abdulloh = Human(name="Abdulloh", age=13)
ubaydulloh = Human(name="Ubaydulloh", age=16)



# abdulloh.greeting()
# ubaydulloh.greeting()


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"Ismi: {self.name}\nYoshi: {self.age}\nBahosi: {self.grade}")



student1 = Student(age=16, name="Palonchi", grade=3)
student2 = Student(age=22, name="Pistonchi", grade=4)
student3 = Student(age=18, name="Handalak", grade=5)



class Product:
    def __init__(self, name: str, cost: int, stock=1, percent=20, unit="dona"):
        self.name = name
        self.cost = cost
        self.stock = stock
        self.unit = unit
        self.price = (self.cost / 100) * percent + self.cost
    
    
    def sell(self, count=1):
        if self.stock < count:
            print(f"Mahsulot yetarli emas!\nYetmayabdi: {count - self.stock} {self.unit}\nMaksimum sotish mumkin: {self.stock} {self.unit}")
            return
        self.stock -= count
        print(f"Mahsulot sotildi\nQoldi: {self.stock} {self.unit}")

    
    # mahsulotni hammasini sotganda qancha foyda olish
    def profit(self):
        natija = (self.price - self.cost) * self.stock
        print(f"Agar {self.stock} {self.unit} sotilsa foyda: {natija} so'm")
        return natija
        
    


olma = Product(name="Olma", cost=5000, percent=200, stock=10, unit="kg")

# foyda = olma.profit()




class Car:
    def __init__(self, model: str, color: str, year: int, price: int):
        self._model = model
        self.color = color
        self.year = year
        self.price = price
    


    def info(self):
        print("=" * 30)
        print("Car info:")
        print(f"Model: {self._model}")
        print(f"Color: {self.color}")
    

    def move(self, speed=50, time=1):
        print(f"{speed * time} km yurildi")
        return speed * time


class Nexia(Car):

    def beep_beep(self):
        print("Di Dit")


class Nexia2(Nexia):

    def beep_beep(self):
        print("Bip Bip")

nexia = Nexia(model="Nexia", color="Black", year=2008, price=8000)

nexia2 = Nexia2(model="Nexia2", color="Blue", year=2015, price=9000)


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    

class Student(Human):

    def set_grades(self, grades: list):
        self.grades = grades

    def get_grades(self):
        print("Baholari:")
        for i in self.grades:
            print(i)

student1 = Student("Abdulloh", 13)



# print("=" * 30)
# print("Omborxona boshqaruv tizimi")
# print("=" * 30)

# class Category:
#     def __init__(self, name):
#         self.name = name

#     def write(self):
#         with open("categories.txt", "a") as file:
#             file.write(f"{self.name}\n")
#         print("Kategoriya qo'shildi")


# def get_categories():
#     with open("categories.txt", "r") as file:
#         data = file.read()
#         return data

# categories = get_categories().split("\n")
# categories.pop()


# class Product:
#     def __init__(self, name: str, category: str, cost: int, unit: str, percent=20, stock=1):
#         self.name = name
#         self.category = category
#         self.cost = cost
#         self.percent = percent
#         self.stock = stock
#         self.unit = unit
#         self.price = (cost // 100) * 20 + self.cost
    
#     def write(self):
#         with open("products.txt", "a") as file:
#             file.write(f"{self.name} | {self.category} | {self.cost} | {self.percent} | {self.price } | {self.stock} | {self.unit}\n")
#         print("Mahsulot qo'shildi!")

# product1 = Product("Shaftoli", "meva", 15000, "kg", 20, 150)

# product1.write()

# def get_products():
#     pass

# products = [
#     ["olma", "meva", 10000, 20],
#     []
# ]

# while True:
#     pass





# shart belgilar

# > katta
# < kichik
# == tengmi
# != teng emas
# >= katta yoki teng
# <= kichik yoki teng





# DRY - DONT REPEAT YOURSELF
# SOLID
# KISS



class User:
    def __init__(self, name: str, age: int, gender="male"):
        self.__name = name
        self.age = age
        self.gender = gender
    
    # getter metod
    def get_name(self):
        print(self.__name)
    
    # setter metod
    def set_name(self, name: str):
        self.__name = name

abdulloh = User(name="Abdulloh", age=13)


class BankAccount:
    def __init__(self, user: User):
        self.user = user
        self.__balance = 0
    
    def withdraw(self, amount: int):
        if self.__balance >= amount:
            print("Pul yechildi!")
            self.__balance -= amount
        else:
            print("Pul yetarli emas!")
    
    def deposit(self, amount: int):
        if amount > 3000000:
            print("Shubhali tranzaksiya")
        else:
            self.__balance += amount

    def show_balance(self):
        print("=" * 30)
        print(f"{self.user.get_name()}")
        print(f"{self.__balance} so'm")
        print("=" * 30)



# account = BankAccount(user=abdulloh)


# print("=" * 30)
# print("Halol bank")
# print("=" * 30)
# while True:
#     print("Amaliyotni tanlang:")
#     print("1) Balans ko'rish")
#     print("2) Balans to'ldirish")
#     print("3) Balans yechish")
#     amaliyot = input(">>>")


#     if amaliyot == "1":
#         account.show_balance()
#     elif amaliyot == "3":
#         amount = int(input("Miqdorni kiriting:>>"))
#         account.withdraw(amount)
#     elif amaliyot == "2":
#         amount = int(input("Miqdorni kiriting:>>"))
#         account.deposit(amount)
#     else: 
#         break
        

class Payment:
    def __init__(self):
        pass
    
    def pay(self):
        print("to'landi")

class Card(Payment):
    def __init__(self):
        pass

    def pay(self):
        print("Plastik karta orqali to'landi")

class Cash(Payment):
    def __init__(self):
        pass

    # def pay(self):
    #     print("Naqd pul orqali to'landi")


a = Card()
b = Cash()
c = Payment()

# b.pay()
























class Car:
    def __init__(self, name: str, year: int, color: str="black"):
        self.name = name # property | xususiyat
        self.year = year
        self.color = color
    
    # metod
    def move(self, speed: int=50):
        print(f"{speed} km/h")

    def honk(self, sound: str="beep beep"):
        print(sound)


# cobalt = Car("Cobalt", 2024, "White")

# cobalt.move()
# cobalt.honk()




class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def move(self):
        print("Yurish")
    

class Student(Human):
    
    def go_university(self):
        print("Universitetga borish")
    
    def move(self):
        print("tezroq yuryabdi")






class BankAccount:
    def __init__(self, user: Human):
        self.user = user
        self.__balance = 0
    
    def deposit(self, amount: int):
        print(f"Pul mablag'i yechildi: {amount}\nQoldi: {self.__balance}")
        self.__balance += amount
        return amount
    
    def withdraw(self, amount: int):
        if amount > self.__balance:
            print("Yetarli mablag' mavjud emas")
            return
        self.__balance -= amount
        return amount

    def show_balance(self):
        print(f"{self.user.name} balansi: {self.__balance}")
    


kamronbek = Human("Kamronbek", age=20)
k_account = BankAccount(kamronbek)

k_account.show_balance()


k_account.deposit(10000)

k_account.show_balance()

k_account.withdraw(15000)

k_account.withdraw(7000)

k_account.show_balance()




class Author:
    def __init__(self, name: str, country: str = "Uzbekistan"):
        self.name = name.capitalize()
        self.country = country.capitalize()


class Book:
    def __init__(self, title: str, year: int, genre: str, author: Author):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return self.title + " | " + self.author.name


class Member:
    def __init__(self, full_name: str, age: int):
        self.full_name = full_name
        self.age = age


class Library:
    def __init__(self, name: str, members: list[Member] = [], books: list[Book] = []):
        self.name = name.capitalize()
        self.members = members
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def get_all_books(self):
        natija = []
        for book in self.books:
            natija.append([book.title, book.author.name, book.year, book.genre])

        return natija
    
    def find_book(self, search: str):
        natija = []
        for book in self.get_all_books():
            if search.lower() in book[0].lower() or search.lower() in book[1].lower():
                natija.append(book)
        return natija


author1 = Author("Erkin Vohidov", "Uzbekistan")
book1 = Book(title="Vatanim", year=2015, genre="She'r", author=author1)
member1 = Member("Kamronbek", 19)

kutubxona = Library("QamarBooks")

kutubxona.add_book(book1)
# kutubxona.add_book(book1)



print(kutubxona.get_all_books())

print("=" * 30)
print(f"{kutubxona.name}ga xush kelibsiz")
print("=" * 30)
while True:

    print()
    print("1) Kitoblarni ko'rish")
    print("2) Kitob qo'shish")
    print("3) Kitob qidirish")
    amal = input(">>>")

    if amal == "1":
        for idx, kitob in enumerate(kutubxona.get_all_books(), start=1):
            print(f"{idx}) {kitob[0]} - {kitob[1]} | {kitob[2]} - {kitob[3]}")
        print("=" * 30)

    elif amal == "2":
        book_name = input("Kitob nomini kiriting:>>")
        book_year = int(input("Kitob yili?>>"))
        book_author = input("Avtorni ismini kiriting:>>")
        author = Author(book_author)
        book_genre = input("Janrni kiriting:>>")

        book = Book(book_name, book_year, book_genre, author)
        kutubxona.add_book(book)
        print("Kitob yaratildi")
        print("=" * 30)

    elif amal == "3":
        search = input("Nimani qidiramiz?>>")
        found_books = kutubxona.find_book(search)

        if not found_books:
            print("Hech narsa mavjud emas!")
            continue
        print("=" * 30)
        print(f"topilgan kitoblar: {len(found_books)} ta")
        for idx, kitob in enumerate(found_books, start=1):
            print(f"{idx}) {kitob[0]} - {kitob[1]} | {kitob[2]} - {kitob[3]}")
        print("=" * 30)




# ======================== Ecommerce ====================
class Base:

    def __str__(self):
        return self.get("name", "Obyekt")


class Client(Base):
    def __init__(self, name: str, phone: str=""):
        self.name = name
        self.phone = phone


class Product(Base):
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock


class Cart:
    def __init__(self, client: Client):
        self.client = client
        self.__products = []
    
    def add_product(self, product, quantity: int):
        self.__products.append([product[0], product[1], quantity, product[1] * quantity])

    def get_products(self):
        return self.__products


class Market(Base):
    def __init__(self, name: str, products: list[Product]=[], clients: list[Client]=[]):
        self.name = name
        self.products = products
        self.clients = clients

    def get_all_products(self):
        natija = []
        for product in self.products:
            if product.stock > 0:
                natija.append([product.name, product.price, product.stock])
        return natija
    
    def add_product(self, product: Product):
        self.products.append(product)

market = Market("Qorabozor")



def create_product():
    name = input("Mahsulot nomini kiriting:>>")
    price = int(input("Mahsulot narxini kiriting:>>"))
    stock = int(input("Mahsulot sonini kiriting:>>"))
    product = Product(name, price, stock)
    return product


def greeting():
    print("=" * 30)
    print(f"{market.name}ga xush kelibsiz")
    print("=" * 30)


def show_main_menu():
    print("=" * 30)
    print("1) Mahsulotlarni ko'rish")
    print("2) Mahsulot qo'shish")
    print("3) Savatchani ko'rish")

def show_products(products: list):
    print(f"Bizdagi mavjud mahsulotlar: {len(products)} ta")

    for idx, product in enumerate(products, start=1):
        print(f"{idx}) {product[0]} - {product[1]} - {product[2]}")
    print("~" * 30)


def register_user():
    name = input("Ismingizni kiriting:>>")
    user = Client(name)
    return user



def main():
    greeting()
    client = register_user()

    card = Cart(client)

    while True:

        show_main_menu()

        amal = input(">>>")

        if amal == "1":
            products = market.get_all_products()
            if not products:
                print("Mahsulotlar mavjud emas!")
                continue
            show_products(products)
            print("Orqaga qaytish uchun 0 ni yuboring")
            selectec_product_index = int(input(">>>"))

            if selectec_product_index == 0:
                continue

            product = products[selectec_product_index - 1]
            quantity = int(input(f"Miqdorini kiriting(max:{product[2]})>>"))
            card.add_product(product, quantity)
            print("Mahsulot qo'shildi")
            print("Davom eting")


        elif amal == "2":
            product = create_product()
            market.add_product(product)
            print("Mahsulot yaratildi")
            print("=" * 30)

        elif amal == "3":
            products = card.get_products()
            show_products(products)


main()