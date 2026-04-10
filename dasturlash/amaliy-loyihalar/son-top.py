# Bu kompyuter o'ylagan sonini topish o'yini

import random

def son_ol(matn="Son kiriting:>>"):
    son = input(matn)
    while not son.isdigit():
        son = input("Faqat son kiriting:>>")

    return int(son)

def main():
    print("=" * 30)
    print("O'ylagan sonimni top o'yini")
    print("=" * 30)

    ss = random.randint(1, 10)
    limit = 2
    while True:
        print(limit + 1, "urinish qoldi")
        son = son_ol()
        while 0 < son or son > 10:
            son = son_ol("Faqat 1 va 10 oralig'ida son kiriting>>")
        
        if ss > son:
            print("Men o'ylagan son kattaroq")
        
        elif ss < son:
            print("Men o'ylagan son kichikroq")
        
        else:
            print("Siz yutdingiz!...")
            break
            
        if limit == 0:
            print("Siz yutqazdingiz!")
            print(f"Men o'ylagan son: {ss} edi!")
            print("=" * 30)
            break

        limit -= 1

main()
