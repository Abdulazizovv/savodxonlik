
# talaba_id = {"Ali": 101, "Vali": 102, "Hasan": 103, "Polonchi": 101}
# id_talaba = {101: ["Ali", "Polonchi"], 102: "Vali", 103: "Hasan"}

# for key, value in talaba_id.items():
#     print(value, key)


# baholar = {"Ali": [5,4,5], "Vali": [3,4,4], "Hasan": [5,5,4]}

# avg_dict = {}

# for i in baholar:
#     avg_dict[i] = sum(baholar[i]) // len(baholar[i])


# print(avg_dict)


# 11-vazofa
# talaba_id = {"Ali": 101, "Vali": 102, "Hasan": 103, "Gani": 101}
# id_talaba = {}

# for talaba, idx in talaba_id.items():
#     if idx in id_talaba:
#         id_talaba[idx].append(talaba)
#     else:
#         id_talaba[idx] = [talaba]

# print(id_talaba)


# 12

# q1 = {"olma": 10, "banan": 5}
# q2 = {"olma": 3, "anor": 7, "banan": 10}

# natija = q1.copy()

# for kalit, qiymat in q2.items():
#     natija[kalit] = natija.get(kalit, 0) + qiymat

# print(natija)


# 1

talaba = {"ism": "Ali", "yosh": 18, "kurs": 1}

# print("Ism: ", talaba["ism"])
# print("Yosh: ", talaba["yosh"])
# print(talaba.keys())
# print(talaba.values())
# print(talaba.items())

# 2

# talaba["baholar"] = [5, 4, 5]
# talaba["yosh"] = talaba.get("yosh") + 1

# print(talaba)

# 5

# for key, value in talaba.items():
#     print(f"{key} : {value}")


# print(("ism","Ali") in talaba.items())



# x = 5
# y = 10
# name = "python"
# print(not (x == y - 5 and (y > 8 or name != "java")) or (x * 2 <= y and name == "python"))



magazin = {
    "mahsulotlar": [
        {"nomi": "Olma", "kategoriya": "mevalar", "narxi": 15000, "sotuvdami": True},
        {"nomi": "Banan", "kategoriya": "mevalar", "narxi": 20000, "sotuvdami": True},
        {"nomi": "Sabzi", "kategoriya": "sabzavotlar", "narxi": 10000, "sotuvdami": True},
    ],
    "xodimlar": [
        {"ismi": "Abdulloh", "lavozim": "direktor", "maosh": 0},
        {"ismi": "Ubaydulloh", "lavozim": "sotuvchi", "maosh": 1000000},
    ]
}


print("""
    Assalomu alaykum! Xush kelibsiz
    Oshxona boshqaruv tizimi
    Amallar:
    1) Mahsulotlarni ko'rish
    2) Mahsulot qo'shish
    3) Mahsulot sotuvdan olib tashlash/qo'yish
    4) Xodimlarni ko'rish
    5) Xodimlarni o'chirish    

""")

while True:
    print("Amalni tanlang:>")
    amal = input()

    if amal == "1":
        for mahsulot in magazin["mahsulotlar"]:
            if mahsulot["sotuvdami"]:
                sotuvdami = "Sotuvda"
            else:
                sotuvdami = "Sotuvda emas"
            print(f"{magazin["mahsulotlar"].index(mahsulot) + 1}) {mahsulot["nomi"]} - {mahsulot["narxi"]} - {sotuvdami}")
    
