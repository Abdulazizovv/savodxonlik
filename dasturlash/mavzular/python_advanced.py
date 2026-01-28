


# def my_decorator(func):
#     def wrapper():
#         print("Funksiayadan oldin bajariladigan ishlar")

#         func()

#         print("Funksiyadan keyingi ishlar")
#     return wrapper


# @my_decorator
# def my_func():
#     print("My func ishladi")


# my_func()


from time import time, sleep


def how_much_time(func):
    def wrapper():
        start = time()
        func()
        end = time()

        delta = end - start
        print(delta)
    return wrapper


@how_much_time
def big_function():
    print("Funksiya ishga tushdi")
    sleep(5)
    print("Funksiya tugadi")


# big_function()



def retry(count: int=1):
    def my_decorator(func):
        def wrapper():

            for _ in range(count):
                func()
        
        return wrapper
    return my_decorator


@retry(10)
def test_func():
    print("Men ishladim")


# test_func()




def my_decorator(func):
    def wrapper():
        for i in range(1, 4):
            print(i, end=" | ")
        print()

        func()

        for i in range(4, 7):
            print(i, end=" | ")
        print()
    return wrapper


@my_decorator
def my_function():
    print("test")


# my_function()


# class Countdown:

#     def __init__(self, start: int=5):
#         self.current = abs(start)
    

#     def __iter__(self):
#         return self
    
#     def __next__(self):
        
#         if self.current <= -1:
#             raise StopIteration
        
#         self.current -= 1
#         return self.current + 1


# for i in Countdown(-50):
#     print(i)



# def my_generator():
#     yield 1
#     yield 2

# def my_function():
#     return 1123



# for i in my_generator():
#     print(i)






def alphabet(start: str="a", end: str="z", step: int=1):
    from string import ascii_lowercase

    start_index = ascii_lowercase.index(start)
    end_index = ascii_lowercase.index(end)

    for i in range(start_index, end_index + 1, step):
        yield ascii_lowercase[i]



# for i in alphabet("a", "z", 2):
#     print(i)

# c
# d
# e
# f
# g





uzbek_names = [
    "Ali", "Vali", "Hasan", "Husan", "Aziz", "Akmal", "Anvar", "Asad", "Bekzod", "Bobur",
    "Dilshod", "Diyor", "Elyor", "Farrux", "Gʻani", "Islom", "Jamshid", "Javlon", "Kamol", "Laziz",
    "Murod", "Nodir", "Odil", "Otabek", "Ravshan", "Sardor", "Sherzod", "Shoxrux", "Temur", "Ulugbek",
    "Umid", "Xurshid", "Yodgor", "Zafar", "Zuhur", "Abdulla", "Abror", "Ahror", "Alisher", "Anvarbek",
    "Azizbek", "Bekmirza", "Doston", "Doniyor", "Eshmat", "Faxriddin",
    "Gulnoza", "Dilnoza", "Malika", "Mohira", "Nodira", "Nigora", "Munisa", "Maftuna", "Sevara", "Sitora",
    "Shaxnoza", "Shirin", "Zulfiya", "Ziyoda", "Yulduz", "Lola", "Rayhona", "Farida", "Dildora", "Kamola",
    "Madina", "Mavluda", "Nafisa", "Oydin", "Ozoda", "Robiya", "Saida", "Umida", "Xadicha", "Zarnigor",
    "Zarina", "Zebo", "Shoira", "Iroda", "Feruza", "Gulbahor", "Gulchehra", "Gulzoda", "Halima", "Humora",
    "Iqboloy", "Jamila", "Komila", "Laylo", "Mohinur", "Nasiba", "Omina", "Rano", "Sabina", "Tohira",
    "Yasmira", "Zuxra", "Zilola", "Mehribon"
]


def get_random_name(count: int=5):
    from random import choice

    if count > len(uzbek_names):
        raise Exception("Mumkin bo'lmagan son")

    natija = []

    while len(natija) < count:
        random_name = choice(uzbek_names)
        if random_name not in natija:
            natija.append(random_name)
    
    for i in natija:
        yield i


ismlar = list(get_random_name(10))

print(ismlar)
