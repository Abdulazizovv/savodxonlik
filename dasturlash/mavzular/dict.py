# Python dict (lug'at) ma'lumot turini o'rganamiz
# Lug'at kalit-qiymat juftliklaridan tashkil topgan ma'lumot turidir
# Lug'at ma'lumot turi o'zgaruvchan (mutable) va tartibli* bo'ladi va takroriy kalitlarga ruxsat bermaydi, 
# unga yangi elementlar qo'shish yoki mavjud elementlarni o'chirish mumkin
# Lug'at yaratish uchun qavslar {} yoki dict() funksiyasidan foydalanamiz

# *Python 3.7 va undan keyingi versiyalarda lug'atlar tartibli hisoblanadi, ya'ni elementlar qo'shilish tartibida saqlanadi.

# Lug'at yaratish
my_dict = {'ism': 'Ali', 'yosh': 25, 'shahar': 'Toshkent'}
print(my_dict)

another_dict = dict(ism='Sara', yosh=28, shahar='Samarqand')
print(another_dict)



# Lug'atga yangi element qo'shish
my_dict['kasb'] = 'Dasturchi'
print(my_dict)


# Lug'atdan element o'chirish
del my_dict['yosh']
print(my_dict)


# Lug'at elementlariga murojaat qilish
print(my_dict['ism'])
# Agar kalit mavjud bo'lmasa, xato yuz beradi
# print(my_dict['yosh'])  # KeyError: 'yosh'

# Lug'at elementini olish (get)
ism = my_dict.get('ism', 'Noma\'lum')
print(ism)  # Output: Noma'lum
# Agar kalit mavjud bo'lsa, qiymatni qaytaradi, aks holda 'Noma'lum' ni qaytaradi


# Lug'at kalitlari va qiymatlarini olish
print(my_dict.keys()) # Output: dict_keys(['ism', 'shahar', 'kasb'])

print(my_dict.values()) # Output: dict_values(['Ali', 'Toshkent', 'Dasturchi'])

print(my_dict.items()) # Output: dict_items([('ism', 'Ali'), ('shahar', 'Toshkent'), ('kasb', 'Dasturchi')])


# Lug'at elementlarini aylantirish
for kalit in my_dict:
    print(f"Kalit: {kalit}, Qiymat: {my_dict[kalit]}")


for kalit, qiymat in my_dict.items():
    print(f"{kalit}: {qiymat}")


# Lug'at uzunligini olish
print(len(my_dict))


# Lug'atni tozalash
my_dict.clear()
print(my_dict)


# Lug'at nusxasini yaratish
new_dict = my_dict.copy()
print(new_dict)


# Lug'atni yangilash
my_dict.update({'ism': 'Vali', 'yosh': 30}) # Output: {'ism': 'Vali', 'yosh': 30}
print(my_dict)


# Lug'at elementini olish va o'chirish (pop)
yosh = my_dict.pop('yosh')
print(yosh)  # Output: 30
print(my_dict)  # Output: {'ism': 'Vali'}


# Lug'at elementini olish va o'chirish (popitem)
item = my_dict.popitem()
print(item)  # Output: ('ism', 'Vali')
print(my_dict)  # Output: {}


# Element mavjudligini tekshirish
if 'ism' in my_dict:
    print("Kalit mavjud")
else:
    print("Kalit mavjud emas")
    
# Lug'atni yaratishda turli ma'lumot turlaridan foydalanish
mixed_dict = {'ism': 'Olim', 'yosh': 22, 'balans': 1500.75, 'faol': True}
print(mixed_dict)


# Ichma-ich lug'atlar (nested dictionaries)
student = {
    'personal_info': {
        'name': 'Dilshod',
        'age': 21,
        'address': {
            'city': 'Toshkent',
            'street': 'Amir Temur'
        }
    },
    'academic_info': {
        'major': 'Computer Science',
        'gpa': 3.8,
        'courses': ['Python', 'Algorithms', 'Database']
    }
}

# Ichki elementlarga murojaat
print(student['personal_info']['name'])  # Dilshod
print(student['personal_info']['address']['city'])  # Toshkent
print(student['academic_info']['courses'][0])  # Python