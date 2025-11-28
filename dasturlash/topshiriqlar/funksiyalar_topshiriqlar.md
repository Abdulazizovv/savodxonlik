## Funksiyalar — topshiriqlar to'plami

Ushbu faylda Python funksiyalarini o'rganayotgan o'quvchilar uchun bosqichma-bosqich topshiriqlar berilgan. Har bir daraja uchun vazifalar oqilona murakkablikda tanlangan: Boshlang'ich (o'rganishni boshlaganlar), O'rta (praksis uchun) va Ilg'or (tajriba va muammolarni hal qilish).

Har bir topshiriq uchun:
- vazifa tavsifi
- kirish/chiqish namunasi (agar kerak bo'lsa)
- qisqa maslahat (hint) yoki tekshiruv mezoni

Ish tartibi: har bir vazifani avval qo'lda sinab ko'ring, so'ng kodni funksiyaga joylang va kichik testlar yozing.

---

## Kirish — qisqacha eslatma

Funksiya — Python'da qayta ishlatiladigan kod blokidir. Sintaksis:

```
def funk_nomi(param1, param2=default):
    """(ixtiyoriy) docstring"""
    # ishlov
    return natija
```

Maslahat: funksiyalarni kichik, bitta vazifali va testlanadigan qiling.

---

## 1-daraja — Boshlang'ich (o'rganayotganlar uchun)

1. Salomlashuvchi funksiya
   - Tavsif: foydalanuvchining ismiga qarab "Salom, <ism>!" qaytaruvchi funksiya yozing.
   - Kirish: ism (string)
   - Chiqish: matn (string)
   - Hint: f-string yoki string concatenation ishlatish.

2. Toq yoki juft
   - Tavsif: butun son qabul qilib, `True` agar juft bo'lsa, `False` aks holda qaytaring.
   - Kirish: int
   - Chiqish: bool
   - Hint: modulus operator `%`.

3. Kvadratni hisoblovchi funksiya
   - Tavsif: son qabul qilib, uning kvadratini qaytaring.
   - Kirish: int/float
   - Chiqish: int/float

4. Ro'yxatdagi elementlar soni
   - Tavsif: ro'yxat qabul qilib uning elementlar sonini qaytaruvchi funksiya yozing (builtin len ishlatmasdan).
   - Kirish: list
   - Chiqish: int
   - Hint: sikl va hisoblagich ishlating.

5. Nomerni katta harflarga aylantirish
   - Tavsif: matn qabul qilib, uni katta harflarga aylantiruvchi funksiya.
   - Kirish: string
   - Chiqish: string
   - Hint: str.upper() mavjud, lekin o'quvchi uchun bu tipik amaliyot.

6. Minimal topshiriq (bonus)
   - Tavsif: ikkita son qabul qilib, kattasini qaytaruvchi funksiya yozing (if-else bilan).

---

## 2-daraja — O'rta (amaliy ko'nikmalar)

1. Faktorial
   - Tavsif: n berilgan (n >= 0). n! ni hisoblovchi funksiya yozing.
   - Kirish: int
   - Chiqish: int
   - Hint: rekursiya yoki sikl.

2. Fibonacci qatoridan n-chi element
   - Tavsif: n-chi Fibonacci sonini qaytaruvchi funksiya yozing (0-indeks yoki 1-indeksni aniq belgilang).
   - Baholash: vaqt va xotira haqida qisqacha o'ylash.

3. Ro'yxatni filtrlash
   - Tavsif: ro'yxat va shart (masalan, funk is_odd) qabul qilib yangi ro'yxat qaytaruvchi funk.
   - Kirish: list, callable
   - Chiqish: list
   - Hint: list comprehension yoki sikl.

4. So'zlarni sanash
   - Tavsif: matn qabul qilib, har bir so'z nechta marta uchrayotganini lug'at (dict) ko'rinishida qaytaring.
   - Kirish: string
   - Chiqish: dict
   - Hint: .split(), dict.get yoki defaultdict.

5. Palindrom tekshiruvchi
   - Tavsif: string qabul qilib, u palindrom ekanligini tekshiruvchi funksiya.
   - Qo'shimcha: bo'shliqlar va punktuatsiyani hisobga olmasdan tekshash.

6. Ro'yxatdagi juft sonlar yig'indisi
   - Tavsif: raqamlar ro'yxatini qabul qilib faqat juftlarini qo'shib qaytaring.

7. Funksiya ichida funksiyani qaytarish (closure) — amaliy mashq
   - Tavsif: n qiymatini saqlovchi funksiya yarating; qaytargan funksiya shu n ga qo'shilgan qiymatlarni qabul qilib natija beradi.

---

## 3-daraja — Ilg'or (muammolar va kombinatsiyalar)

1. Lambda va map/filter/reduce amaliyoti
   - Tavsif: ro'yxatdagi har bir elementni kvadratlash uchun lambda + map yozing; keyin filter bilan faqat katta elementlarni oling.

2. Decorator tushunchasi
   - Tavsif: funksiyani chaqirish vaqtini konsolga chiqaruvchi oddiy decorator yozing.
   - Hint: *args, **kwargs qabul qilishni unutmayin.

3. Rekursiv qidiruv (backtracking) — kombinatsiyalar
   - Tavsif: berilgan ro'yxatdan barcha kombinatsiyalarni (power set) qaytaruvchi funksiya yozing.

4. Tahrir masofasi (Levenshtein) — ixtiyoriy murakkab mashq
   - Tavsif: ikki matn orasidagi minimal tahrir amallar sonini hisoblovchi funksiya.
   - Eslatma: bu murakkabroq; DP bilan yechiladi.

5. Memoizatsiya bilan tezlashtirish
   - Tavsif: sekin ishlaydigan rekursiv funksiyani (masalan, naive Fibonacci) memoizatsiya qilib tezlashtiring — dekorator yordamida.

6. API yengilligi: funksiyaga tip tekshiruv qo'shish
   - Tavsif: funksiya kirishlarini avtomatik tekshiruvchi dekorator yozing (masalan, input turlarini solishtirish uchun).

---

## Loyihalar (kichik) — bir nechta birlashtirilgan topshiriqlar

1. Matnni tahlil qilish (mini-loyih)
   - Tavsif: fayldan matn o'qib, so'zlar soni, eng ko'p uchraydigan so'z, o'rtacha so'z uzunligi kabi ko'rsatkichlarni qaytaruvchi funksiya/funktsiyalar to'plamini yozing.

2. Raqamlarni qayta ishlovchi utilita
   - Tavsif: raqamlar ro'yxatini qabul qilib, statistik (min, max, mean, median) qiymatlarni qaytaruvchi modul yozing. Har bir natija uchun alohida funksiya bo'lsin.

3. Mini-kalkulyator (CLI)
   - Tavsif: foydalanuvchi kiritgan ifodani (misol: "12 + 7 * 3") funksiya orqali hisoblab natijani qaytaruvchi dastur yozing. (Ehtiyot bo'ling: eval xavfsiz emas — parsing yoki shartli tekshiruv kerak.)

---

## Baholash mezonlari va maslahatlar

- To'g'rilik: funksiya barcha ko'rsatilgan kirishlarda kutgan natijani qaytargan bo'lishi kerak.
- Qayta ishlatiluvchanlik: funksiyalar kichik va bitta vazifali bo'lsin.
- Xatoliklarni boshqarish: kutilmagan kirishlar uchun ValueError yoki mos xatolik tashlang.
- Test yozing: har bir funksiya uchun kamida 2-3 kichik test yozib ko'ring.

---

## Qo'shimcha: teacher uchun eslatma

- O'quvchilarni rag'batlantirish uchun daraja va ball tizimi joriy eting (masalan, 1-daraja har bir topshiriq 1 ball, 2-daraja 2 ball va h.k.).
- Har bir topshiriq uchun qisqa hintlarni (1-2 qator) alohida faylga yoki yechimlar bo'limiga joylashtirish mumkin.

---

Agar xohlasangiz, men shu faylga: (A) har bir topshiriq uchun test fayl (.py) yaratib bera olaman, yoki (B) har bir topshiriq uchun qadam-baqadam yechim (yoki faqat hints) qo'shishim mumkin. Qaysi variantni xohlaysiz?
