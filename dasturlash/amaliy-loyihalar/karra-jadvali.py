from time import sleep
import os


def clear():
    os.system("cls" if os.name=="nt" else "clear")

def son_ol(matn="Son kiriting:>>"):
    son = input(matn)
    while not son.isdigit():
        son = input("Faqat son kiriting:>>")

    return int(son)


def main():
    son = son_ol()

    for i in range(1, son + 1):
        print("=" * 30)
        
        for k in range(1, 11):
            print(f"{i} x {k} = {i * k}")
            sleep(0.5)
        sleep(3)
        clear()

main()