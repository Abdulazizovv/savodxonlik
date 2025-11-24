# Pythonda funksiyalar bilan ishlash

# Funksiya nima?
# Funksiya - bu ma'lum bir vazifani bajarish uchun yozilgan kod blokidir.
# Funksiyalar kodni qayta ishlatish va uni tartibga solish uchun juda foydalidir.
# bu esa dastur yozishni osonlashtiradi va xatoliklarni kamaytiradi.

# Funksiya yaratish
# Funksiyani yaratish uchun "def" kalit so'zidan foydalanamiz, 
# undan keyin funksiyaning nomi va qavslar ichida 
# parametrlar (agar kerak bo'lsa) yoziladi.

# Oddiy funksiya
def salom_ber():
    print("Salom, dunyo!")


# Paramerli funksiya
def salom_ber2(ism):
    """Foydalanuvchiga salom beruvchi funksiya"""
    print(f"Salom, {ism}!")
    return # Funksiya hech narsa qaytarmaydi

# def kalit so'zi
# salom_ber - funksiyaning nomi
# ism - parametr
# """Foydalanuvchiga salom beruvchi funksiya""" - docstring (funksiya haqida ma'lumot)
# print(f"Salom, {ism}!") - funksiyaning bajaradigan vazifasi | funksiya tanasi
# return - funksiyani tugatish va natija qaytarish (ixtiyoriy) | qiymat qaytarish

# Funksiyani chaqirish
salom_ber()  # Funksiyani chaqirish
salom_ber2("Ali")  # Parametr bilan funksiyani chaqirish

# Funksiyadan qiymat qaytarish
def yigindi(a, b):
    """Ikki sonning yig'indisini qaytaruvchi funksiya"""
    return a + b

natija = yigindi(5, 10)
print("Yig'indi:", natija)


# Funksiyaga ko'p parametrlar berish
def toliq_ism(ism, familiya):
    """To'liq ismni qaytaruvchi funksiya"""
    return f"{ism} {familiya}"

natija = toliq_ism("Ali", "Valiyev")
print("To'liq ism:", natija)


# Funksiyaga standart qiymatlar berish
def toliq_ism2(ism, familiya, otasining_ismi=""):
    """To'liq ismni qaytaruvchi funksiya, otasining ismi ixtiyoriy"""
    if otasining_ismi:
        return f"{ism} {otasining_ismi} {familiya}"
    else:
        return f"{ism} {familiya}"
natija1 = toliq_ism2("Ali", "Valiyev")
natija2 = toliq_ism2("Ali", "Valiyev", "Otaniyoz")
print("To'liq ism 1:", natija1)
print("To'liq ism 2:", natija2)

# Funksiyaga nomlangan argumentlar berish
natija = toliq_ism(familiya="Valiyev", ism="Ali")
print("To'liq ism (nomlangan argumentlar):", natija)

# Funksiyada ro'yxat va lug'atlardan foydalanish
def talaba_malumotlari(ism, yosh, kurs, baholar):
    """Talaba haqida ma'lumotlarni qaytaruvchi funksiya"""
    return {
        "ism": ism,
        "yosh": yosh,
        "kurs": kurs,
        "baholar": baholar
    }
talaba1 = talaba_malumotlari("Ali", 20, 2, [5, 4, 5])
print("Talaba ma'lumotlari:", talaba1)

# Funksiyada ichma-ich funksiyalar yaratish
def tashqi_funksiyalar(x):
    """Tashqi funksiya"""
    def ichki_funksiyalar(y):
        """Ichki funksiya"""
        return y * 2
    return ichki_funksiyalar(x) + 5
natija = tashqi_funksiyalar(10)
print("Natija:", natija)

# Amaliy mashqlar

# Matnni teskari qaytaruvchi funksiya
def teskari_matn(matn):
    """Matnni teskari qaytaruvchi funksiya"""
    return matn[::-1]
natija = teskari_matn("Salom")
print("Teskari matn:", natija)

# Faktorial hisoblovchi funksiya
def faktorial(n):
    """Sonning faktorialini hisoblovchi funksiya"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
natija = faktorial(5)
print("Faktorial:", natija)

# Matnni palindrom ekanligini tekshiruvchi funksiya | O'quvchi mashq
def palindrom_tekshir(matn):
    """Matn palindrom ekanligini tekshiruvchi funksiya"""
    pass