


# Takrorlash uchun topshiriqlar
# funksiya yaratib bajarishingiz kerak

# 1-topshiriq
# ro'yxatdagi unli harf bilan boshlanadigan so'zlarni yangi ro'yxatga joylashtiring
# sozlar = ['olma', 'anor', 'banan', 'shaftoli', 'uzum', 'nok', 'gilos']
# natija = ['olma', 'anor', 'uzum']

# natija = ['olma', 'anor', 'uzum']
# def unli_harf(sozlar: list):
#     unli = 'aeiou'
#     yangi_royhat = []
#     for soz in sozlar:
#         if soz[0].lower() in unli:
#             yangi_royhat.append(soz)
#     return yangi_royhat
    
# sozlar = ['Olma', 'Anor', 'banan', 'shaftoli', 'uzum', 'nok', 'gilos']
# natija = unli_harf(sozlar)
# print(natija)


# 2-topshiriq
# berilgan ro'yxatdagi juft sonlarni yangi ro'yxatga joylashtiring
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# natija = [2, 4, 6, 8, 10]


# def even_numbers(numbers: list):
#     juft_sonlar = []

#     for son in numbers:
#         if son % 2 == 0:
#             juft_sonlar.append(son)
#     return juft_sonlar


# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# natija = even_numbers(numbers=sonlar)

# print(natija)


# 3-topshiriq
# berilgan matndagi so'zlarni sonini hisoblang. Bunda bir xil so'zlar soni qo'shib hisoblanadi
# salom: 2, dunyo: 2, odamlar: 1


# def count_words(text: str):
#     words = text.split()
#     # ['salom', 'dunyo', 'salom', 'odamlar', 'dunyo']
#     count = {}
#     for word in words:
#         if word not in count:
#             count[word] = 1
#         else:
#             count[word] = count[word] + 1
#     return count
# matn = "salom dunyo salom odamlar dunyo salom xalq salom qovun"
# natija = count_words(matn)
# print(natija)


# 4-topshiriq
# ko'paytirish jadvalini hosil qiling (1 dan 10 gacha)
# natija:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 10 x 10 = 100


# def karra_jadval():
#     for i in range(1, 11):
#         for k in range(1, 11):
#             print(f"{i} x {k} = {i * k}", end="|\n==================\n")


# karra_jadval()




# 5-topshiriq
# ro'yxat ichidagi eng katta sonni toping(max funksiyasidan foydalanmang)
# sonlar = [34, 12, 45, 67, 23, 89, 2, 90, 11]
# natija = 90


# def max_number_in_list(sonlar: list):
    
#     maxx = sonlar[0]

#     for son in sonlar:
#         if son > maxx:
#             maxx = son
#     return maxx

# sonlar = [34, 12, 45, 67, 23, 89, 2, 90, 11]

# natija = max_number_in_list(sonlar)
# print(natija)



# 6-topshiriq
# berilgan matn ichida raqamlarni ajratib beruvchi funksiya yarating
# matn = "a1b2c3d4e5"
# natija = ['1', '2', '3', '4', '5']


# def raqam(matn: str):
#     # numbers = ['0', '1', '2']
    
#     new_arr = []

#     for i in matn:
#         if i.isdigit():
#             new_arr.append(i)

#     return new_arr

# matn = "a1b2c3d4e5g56"
# natija = raqam(matn)
# print(natija)


# 7-topshiriq | hard
# sonni stringga aylantirish(str funksiyasidan foydalanmang)
# son = 12345
# natija = "12345"

# 123 > '123'

# def int_to_str(n: int):
#     digits = "0123456789"
#     s = ''

#     while n > 0:
#         oxirgi_raqam = n % 10
#         s = digits[oxirgi_raqam] + s
#         n //= 10
#     return s

# son = 12345
# natija = int_to_str(son)

# print(natija * 3)
# print(type(natija))
