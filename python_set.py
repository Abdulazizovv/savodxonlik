# Pythonda set yaratish va undan foydalanish

# set pythonda 4 built in(oldindan o'rnatilgan) ma'lumotlar tuzilmalaridan biridir.
# bular: list(ro'yxat), tuple(kortej), set(to'plam) va dict(lug'at).
# Set bu o'ziga xos elementlarni saqlaydigan ma'lumotlar tuzilmasi.
# ya'ni faqatgina noyob(takrorlanmaydigan) elementlarni o'z ichiga oladi.
# set tartiblanmagan va takrorlanmaydigan elementlarni o'z ichiga oladi
# set elementlarini o'zgartirish mumkin emas, lekin setga yangi elementlar qo'shish va mavjud elementlarni o'chirish mumkin

# setda elementlar qavs ichida {} ko'rsatiladi va elementlar vergul bilan ajratiladi
# setda indekslash yo'q, shuning uchun elementlarga indeks orqali murojaat qilib bo'lmaydi

# setda True va 1 bir xil element sifatida qabul qilinadi, shuning uchun ularni alohida elementlar sifatida saqlab bo'lmaydi
# xuddi shunday False va 0 ham bir xil element sifatida qabul qilinadi


# real proyektlarda ishlatilishi:
# 1. Takrorlanmaydigan elementlarni saqlash uchun
# 2. Tezkor qidiruv va a'zolik tekshiruvlari(in, not in) uchun. Chunki hash table asosida ishlaydi va qidiruv O(1) vaqt oladi
# 3. Matematik to'plam operatsiyalarini bajarish uchun (birlashma, kesishma, farq va boshqalar)

my_set = set()  # bo'sh set yaratish
# my_set = {}   # bo'sh dict(lug'at) yaratish
print("Bo'sh set:", my_set)



my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)


# Element qo'shish
my_set.add(6)
print("Set after adding 6:", my_set)

# Iterable (takrorlanadigan) elementlar qo'shish
my_set.update([7, 8, 9])
print("Set after updating with [7, 8, 9]:", my_set)


# Element o'chirish
my_set.remove(3) # agar element setda bo'lmasa, xato beradi
print("Set after removing 3:", my_set)  
my_set.discard(10) # agar element setda bo'lmasa, xato bermaydi
print("Set after discarding 10:", my_set)
my_set.pop()  # tasodifiy elementni o'chiradi va o'chirilgan elementni qaytaradi
print("Set after popping an element:", my_set)


# Setdagi barcha elementlarni ko'rsatish
for item in my_set:
    print("Set item:", item)


# Setdagi elementlar sonini olish
set_length = len(my_set)
print("Set length:", set_length)

# Set tozalash
my_set.clear()
print("Set after clearing:", my_set)
# Set o'chirish
del my_set
# print(my_set)  # bu xato beradi, chunki my_set o'chirilgan

# Setlarni boshqa setlar bilan matematik operatsiyalarni bajarish
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Birlashma
# Ikkala setdagi barcha noyob elementlar
set_union = set_a.union(set_b) # yoki set_a | set_b
print("Set union:", set_union) # {1, 2, 3, 4, 5, 6}

# Kesishma
# Umumiy elementlar
set_intersection = set_a.intersection(set_b) # yoki set_a & set_b
print("Set intersection:", set_intersection) # {3, 4}

# Farq
# birinchi setda mavjud bo'lib, ikkinchisida mavjud bo'lmagan elementlar
set_difference = set_a.difference(set_b) # yoki set_a - set_b
print("Set difference:", set_difference) # {1, 2}

# Simmetrik farq
# Ikkala setda ham mavjud bo'lmagan elementlar
set_symmetric_difference = set_a.symmetric_difference(set_b) # yoki set_a ^ set_b
print("Set symmetric difference:", set_symmetric_difference) # {1, 2, 5, 6}