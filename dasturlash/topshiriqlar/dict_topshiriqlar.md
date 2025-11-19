# Dictionary (lug'at) bo'yicha amaliy vazifalar

Lug'atlar — kalit-qiymat juftliklari bilan ishlashga imkon beruvchi kuchli ma'lumot tuzilmasi. Quyidagi mashqlar 3 darajada (boshlang'ich → o'rta → murakkab) ketma‑ketlikda berilgan.

---
## 1‑daraja: Boshlang'ich
Yangi o'rganuvchilar uchun asosiy amaliyotlar.

### 1‑vazifa: Oddiy lug'at yaratish
- `talaba` nomli lug'at yarating: `{"ism": "Ali", "yosh": 18, "kurs": 1}`
- `ism` va `yosh` qiymatlarini alohida chiqaring
- Kalitlar ro'yxatini (`keys()`), qiymatlar ro'yxatini (`values()`) ko'rsating

**Namuna chiqish:**
```
Ism: Ali
Yosh: 18
Kalitlar: dict_keys(['ism', 'yosh', 'kurs'])
Qiymatlar: dict_values(['Ali', 18, 1])
```

### 2‑vazifa: Qo'shish va yangilash
- `talaba["baholar"] = [5, 4, 5]` qo'shing
- `yosh` qiymatini `+1` ga oshiring
- Yangilangan lug'atni chiqaring

**Maslahat:** `talaba["yosh"] = talaba["yosh"] + 1`

### 3‑vazifa: Xavfsiz o'qish `get` va `setdefault`
- `talaba` lug'atidan `guruh` kalitini `get` bilan o'qing; topilmasa `"A-101"` ni qaytaring
- `setdefault` yordamida `fakultet` kalitini `"KIF"` ga o'rnating (agar bo'lmasa)

### 4‑vazifa: O'chirish usullari
- `kurs` kalitini `pop` yordamida o'chiring va o'chirilgan qiymatni alohida chiqaring
- Oxirgi elementni `popitem()` bilan o'chirib ko'ring (natijani tekshiring)

### 5‑vazifa: Sikl bilan aylaning
- `talaba.items()` bo'yicha aylanib, `kalit: qiymat` formatida har qatorni chiqaring

### 6‑vazifa: Birlashtirish
- `manzil = {"shahar": "Toshkent", "tuman": "Yunusobod"}`
- `talaba` bilan birlashtiring (`update()` yoki `|` operatori)

---
## 2‑daraja: O'rta
Bir nechta elementlar, hisoblash va tartiblash.

### 7‑vazifa: Baholar statistikasi
- `baholar = {"Ali": [5,4,5], "Vali": [3,4,4], "Hasan": [5,5,4]}`
- Har bir talabaning o'rtacha bahosini hisoblab, `o'rtacha` lug'atini yarating
- O'rtachasi eng yuqori bo'lgan 1 talabaning nomini chiqaring

**Maslahat:** `sum(lst) / len(lst)`; qiymat bo'yicha solishtiring.

### 8‑vazifa: Harf chastotasi
- Foydalanuvchi kiritgan so'zdagi harflar chastotasini hisoblang (lug'at ko'rinishida)
- Masalan: `"sanoq" -> {'s':1, 'a':1, 'n':1, 'o':1, 'q':1}`

### 9‑vazifa: So'z chastotasi (matn)
- Matnni `split()` qiling, hammasini `lower()` qiling
- So'zlar chastotasini lug'atda saqlang va eng ko'p uchraydigan 3 so'zni chiqaring

### 10‑vazifa: Lug'atni qiymat bo'yicha saralash
- `narxlar = {"olma": 12000, "banan": 18000, "gilos": 35000, "anor": 25000}`
- Eng arzon 2 va eng qimmat 2 mahsulot nomlarini chiqaring (qiymat bo'yicha sort)

**Maslahat:** `sorted(narxlar.items(), key=lambda x: x[1])`

### 11‑vazifa: Invert (kalit ↔️ qiymat)
- `talaba_id = {"Ali": 101, "Vali": 102, "Hasan": 103}`
- Uni `id_talaba = {101: "Ali", ...}` ko'rinishga aylantiring
- Agar qiymatlar takrorlansa, bir idga bir nechta ism bo'lishi mumkin – bunday holatda ro'yxat saqlang: `{id: [ismlar...]}`

### 12‑vazifa: Bir nechta lug'atlarni birlashtirish va yig'ish
- `q1 = {"olma": 10, "banan": 5}`, `q2 = {"olma": 3, "anor": 7}`
- Natija: `{ "olma": 13, "banan": 5, "anor": 7 }` (bir xil kalitlar yig'iladi)

---
## 3‑daraja: Murakkab
Ichma‑ich (nested) tuzilmalar, guruhlash, transformatsiyalar.

### 13‑vazifa: Nested lug'at bilan ishlash
- `kitoblar` lug'ati yarating:
```python
kitoblar = {
  "fantastika": [
    {"nom": "Dune", "muallif": "Frank Herbert", "yil": 1965},
    {"nom": "Foundation", "muallif": "Isaac Asimov", "yil": 1951}
  ],
  "detektiv": [
    {"nom": "The Hound", "muallif": "Arthur Conan Doyle", "yil": 1902}
  ]
}
```
- Fantastika bo'limiga yangi kitob qo'shing
- Muallifi `Isaac Asimov` bo'lgan kitoblarni topib ro'yxatlang
- Eng eski kitob nomini toping

### 14‑vazifa: Guruhlash (kategoriya)
- `mahsulotlar = [("olma", 12000), ("banan", 18000), ("shaftoli", 9000), ("gilos", 35000)]`
- 15000 dan arzon — `"arzon"`, aks holda `"qimmat"`
- Natija: `{ "arzon": [nomlar], "qimmat": [nomlar] }`

### 15‑vazifa: Ro'yxatdagi lug'atlarni indekslash
- Quyidagidan `id` bo'yicha lug'at yarating (tez qidirish uchun):
```python
foydalanuvchilar = [
  {"id": 1, "ism": "Ali", "rol": "admin"},
  {"id": 2, "ism": "Vali", "rol": "user"},
  {"id": 3, "ism": "Hasan", "rol": "moderator"}
]
```
- Natija: `{1: {...}, 2: {...}, 3: {...}}`

### 16‑vazifa: Parametrlarni tozalash (transformatsiya)
- `params = {"Limit": "10", "Page": "2", "Query": "Olma"}`
- Barcha kalitlarni `lower()` qiling, `"10"` va `"2"` ni `int` ga aylantiring
- Natija: `{"limit": 10, "page": 2, "query": "Olma"}`

### 17‑vazifa: Kunlar bo'yicha qatnashish
- `qatnashuv = {"Du": True, "Se": False, "Ch": True, "Pa": True, "Ju": False}`
- Nechta kunda qatnashgan/qatnashmaganini hisoblang
- Foizda ham chiqaring (masalan: `60%`)

### 18‑vazifa: JSONga tayyorlash
- `buyurtma = {"id": 501, "mahsulotlar": [{"nom": "olma", "soni": 3, "narx": 12000}]}`
- Umumiy qiymatni hisoblang (`soni * narx` yig'indisi)
- `status` kalitini `"yangi"` deb qo'shing
- Natijani JSONga mos formatda chiroyli chiqaring (masalan, `print` bilan tartibli)

---
### Qo'shimcha maslahatlar
- `get`, `setdefault`, `update`, `pop`, `popitem`, `items`, `keys`, `values` metodlarini amalda sinab ko'ring.
- `copy()` va `deepcopy()` farqini izohlab bering (nested tuzilmada muhim).
- Saralashda `sorted(..., key=...)` ishlating; qiymatga ko'ra sortlash uchun `key=lambda x: x[1]`.
- Birlashtirish uchun: Python 3.9+ da `dict1 | dict2`, aks holda `update()`.

Omad! Har bir vazifadan so'ng qisqa xulosa yozing: nimalarni o'rgandingiz va yana qanday holatlarni sinab ko'rishingiz mumkin.
