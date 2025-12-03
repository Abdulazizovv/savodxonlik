
# Ma'lumot turlari | data types
# str
# int
# float
# bool


matn = input("Matn kiriting".lower())

# satr - belgilar ketma-ketligi

name = "Bobur"

# print(name[0])
# print(name[-3])

print(name[::-1]) # satrni teskarisini qaytaradi


print(name[1:]) # 1-indexdan boshlab oxirigacha -> obur
print(name[:4]) # boshidan boshlab 4-indexgacha(o'zi olinmaydi) -> Bobu


uzunlik = len(name)
print(uzunlik)



# satr ustida amallar

# satrlarni bir biriga qo'shish
print(name + " yaxshi bola")

# takrorlash
print(("ab" * 30))


# belgini satrni ichida borligiga tekshirish
# in - ichida bormi
# not in - ichida yo'qmi
print("o" in "Bobur")
print("x" not in "Bobur")

# satrlarni formatlash

print("Ismingiz:", name)
print(f"\tIsmingiz: {name} \nyoshingiz: {10 + 10} \nstudentmisiz: {True}")

# satr metodlari

# .upper() - satrdagi barcha harflarni katta qiladi
print(name.upper())

# .lower() - satrdagi belgilarni kichkina qiladi
print("BoBUr".lower())

# .replace("a", "b") - satrdagi a ni b ga almashtiradi
name = name.replace("o", "a")
print(name)


# .find("a") - satrdagi birinchi uchragan a harfini indeksini qaytaradi topilmasa -1 qaytaradi
print(name.find("a")) # 1
print(name.find("x")) # -1

# "Abdulaziz".find(a) -> 5


# .strip() - satrdagi o'ng va chap qismdagi bo'sh joylarni olib tashlaydi

satr = "     Hello world       "
print(satr.strip())


# .count("a") - satrda nechta a borligini sanaydi
print(name.lower().count("b")) # 2


# .isalpha() - satr faqatgina harflardan tashil topganligiga tekshiradi
print("bobur".isalpha())


# .isdigit() - satr faqatgina raqamlardan tashkil topganiga tekshiradi
print("123456".isdigit())


# .isspace() - satr faqatgina bo'sh joylardan iboratligini tekshiradi
print("   ".isspace())


# .capitalize() - satrni bosh harfini katta qiladi
print("BObuR".capitalize())

# .title() - satrdagi har bir so'zni bosh harfini katta qiladi

print("o'zbekiston respublikasi".title())


# .startswith("Bo") - satr Bo bilan boshlanishiga tekshiradi
print(name.startswith("Bab"))

# .endswith("ur") - satr ur bilan tugashiga tekshiradi
print(name.endswith("ur"))

# .zfill(10) - satrni boshiga 0 bilan to'ldiradi
print("1".zfill(4)) # 0001
print("1000".zfill(4)) # 1000