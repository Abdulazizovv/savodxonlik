# pythonda fayllar bilan ishlash
# Fayl yaratish va unga yozish

# fayl - bu kompyuter xotirasida saqlanadigan ma'lumotlar to'plami
# Fayllar turli formatlarda bo'lishi mumkin: matn fayllari (.txt, .csv, .json), 
# rasm fayllari (.jpg, .png), hujjat fayllari (.pdf, .docx) va boshqalar.

# Biz matn fayllari bilan ishlashni ko'rib chiqamiz.

# open() funksiyasi - faylni ochish yoki yaratish uchun ishlatiladi.
# Sintaksis: open(fayl_nomi, rejim)
# rejimlar: 'r' - o'qish, 'w' - yozish, 'a' - qo'shish, 'rb' - binar o'qish, 'wb' - binar yozish

# Fayl yaratish va unga yozish
fayl = open('misol.txt', 'w')  # 'misol.txt' nomli fayl yaratish
fayl.write('Salom, dunyo!\n')  # Faylga matn yozish
fayl.write('Fayllar bilan ishlash juda qiziqarli.\n')
fayl.close()  # Faylni yopish
# Faylni yopish muhim, chunki bu yozilgan ma'lumotlarning saqlanishini ta'minlaydi.

# Fayldan o'qish
fayl = open('misol.txt', 'r')  # 'misol.txt' faylini o'qish rejimida ochish
kontent = fayl.read()  # Fayldan barcha ma'lumotlarni o'qish
print(kontent)  # O'qilgan ma'lumotlarni chiqarish
fayl.close()  # Faylni yopish

# Faylga ma'lumot qo'shish
fayl = open('misol.txt', 'a')  # 'misol.txt' faylini qo'shish rejimida ochish
fayl.write('Yana bir qator matn qo\'shildi.\n')
fayl.close()  # Faylni yopish

# O'qilgan ma'lumotlarni chiqarish
fayl = open('misol.txt', 'r')  # 'misol.txt' faylini o'qish rejimida ochish
kontent = fayl.read()  # Fayldan barcha ma'lumotlarni o'qish
print(kontent)  # O'qilgan ma'lumotlarni chiqarish
fayl.close()  # Faylni yopish


# with() kontekts menejeri yordamida fayllar bilan ishlash
# with kontekts menejeri faylni avtomatik ravishda yopishni ta'minlaydi
with open('misol.txt', 'r') as fayl:
    kontent = fayl.read()
    print(kontent)
# Fayl avtomatik ravishda yopiladi, chunki with bloki tugadi.

