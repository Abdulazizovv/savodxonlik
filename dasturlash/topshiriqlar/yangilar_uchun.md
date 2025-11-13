# Boshlang'ich Amaliy Vazifalar

Quyidagi vazifalar Python asosiy operatorlari va oddiy arifmetikani mustahkamlash uchun mo'ljallangan.

---
## 1‑vazifa: 4 ta asosiy arifmetik amal
Foydalanuvchi kiritgan 2 ta son ustida qo'shish, ayirish, ko'paytirish va bo'lish amallarini bajaring.

**Talablar:**
- 2 ta sonni `input()` orqali oling
- Qo'shish (+), ayirish (-), ko'paytirish (*), bo'lish (/) ni hisoblang
- Natijani chiroyli formatda chiqaring

**Namuna:**
```
Birinchi son: 10
Ikkinchi son: 5

10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
```

---
## 2‑vazifa: Kvadrat va kub
Foydalanuvchi kiritgan sonning kvadrati va kubini hisoblang.

**Talablar:**
- Sonni `input()` orqali oling
- `**` operatori yordamida kvadrat (`son ** 2`) va kub (`son ** 3`) ni hisoblang
- Natijalarni chiqaring

**Namuna:**
```
Son: 4
Kvadrat: 16
Kub: 64
```

---
## 3‑vazifa: Bo'linma va qoldiq
Ikkita sonni bo'ling va butun bo'linma hamda qoldiqni toping.

**Talablar:**
- 2 ta sonni oling
- `//` operatori bilan butun bo'linmani toping
- `%` operatori bilan qoldiqni toping
- Natijalarni chiqaring

**Namuna:**
```
Birinchi son: 17
Ikkinchi son: 5

Butun bo'linma: 3
Qoldiq: 2
```

---
## 4‑vazifa: 3 xonali son raqamlari yig'indisi
Berilgan 3 xonali sonning raqamlarini ajratib, yig'indisini toping.

**Talablar:**
- 3 xonali sonni oling (100–999 oralig'i)
- `//` va `%` operatorlari yordamida yuzlik, o'nlik, birlik raqamlarini ajrating
- Raqamlar yig'indisini hisoblang

**Namuna:**
```
Son: 123
Raqamlar: 1, 2, 3
Yig'indi: 6 (1 + 2 + 3)
```

---
## 5‑vazifa: Sekundlarni soat-daqiqa-sekundga aylantirish
Berilgan umumiy sekundni soat, daqiqa va sekund ko'rinishiga ajrating.

**Talablar:**
- Sekundlar sonini oling
- `//` bilan to'liq soat va daqiqalarni, `%` bilan qolganini ajrating
- Natijani formatlangan holda chiqaring

**Namuna:**
```
Sekundlar: 3665
Soat: 1, Daqiqa: 1, Sekund: 5
```

---
### Qo'shimcha maslahatlar
- Kiritmalarni `int()` ga aylantirishni unutmang.
- Bo'lish (`/`) natijasi har doim `float` bo'lishi mumkin.
- Test uchun turli sonlarni kiriting (masalan: 0, katta sonlar, 3 xonali bo'lmagan son) va xatoliklarni kuzating.