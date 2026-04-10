
import random
from time import sleep
import os


def clear():
    os.system("cls" if os.name=="nt" else "clear")

# 1 tosh
# 2 qaychi
# 3 qogoz

def son_ol(matn=":>>"):
    print("Tanlang")
    print("1) Tosh")
    print("2) Qaychi")
    print("3) Qog'oz")
    son = input(matn)
    while not son.isdigit() or son not in ["1", "2", "3"]:
        son = input("Faqat son kiriting(1,2,3):>>")

    return int(son)


options = {
    1: "Tosh",
    2: "Qaychi",
    3: "Qogoz"
}

def main():
    print("=" * 30)
    print("TOSH QAYCHI QOGOZ o'yini")
    print("=" * 30)

    while True:
        sleep(5)
        clear()
        ss = random.randint(1, 3)
        son = son_ol()

        if son == ss:
            print("=" * 30)
            print("Durang")
            print("=" * 30)
            print("Men tanlagandim", options.get(ss))

            continue
        
        if ss == 1:
            if son == 2:
                print("=" * 30)
                print("Siz yutqazdingiz!")
                print("=" * 30)
                print("Men tanlagandim", options.get(ss))

                continue
            elif son == 3:
                print("Siz yutdingiz!")
                print("Men tanlagandim", options.get(ss))
                continue
        
        if ss == 2:
            if son == 3:
                print("Siz yutqazdingiz!")
                print("Men tanlagandim", options.get(ss))
                continue
            elif son == 1:
                print("Siz yutdingiz!")
                print("Men tanlagandim", options.get(ss))
                continue
        
        if ss == 3:
            if son == 1:
                print("Siz yutqazdingiz!")
                print("Men tanlagandim", options.get(ss))
                continue
            elif son == 2:
                print("Siz yutdingiz!")
                print("Men tanlagandim", options.get(ss))
                continue
        


main()