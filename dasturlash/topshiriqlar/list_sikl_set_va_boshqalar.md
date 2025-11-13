# List, Sikl va Shartli Ifodalar Bo'yicha Vazifalar

Quyidagi mashqlar ro'yxatlar (list), sikllar (`for`, `while`) va shart operatorlarini mustahkamlash uchun tuzilgan.

---
## 1‑vazifa: Juft va toq sonlar ro'yxati
1 dan 20 gacha bo'lgan sonlarni ajrating:
- Juft sonlarni alohida listga
- Toq sonlarni alohida listga
Va ikkalasini ekranga chiqaring.

**Kutilyotgan natija:**
```python
juft_sonlar = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
toq_sonlar  = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

**Maslahat:** `range(1, 21)` va `if son % 2 == 0` dan foydalaning.

---
## 2‑vazifa: 3 va 5 bo'linuvchanlik etiketi
1 dan 30 gacha bo'lgan sonlar uchun:
- 3 ga bo'linsa: `Python`
- 5 ga bo'linsa: `Dasturlash`
- 3 ham, 5 ham ga bo'linsa: `Python Dasturlash`
- Aks holda: sonni o'zi

**Maslahat:** Avval eng aniq holatni (3 va 5) tekshiring.

**Namuna chiqishi (qisqa):**
```
1
2
Python
4
Dasturlash
Python
...
Python Dasturlash   # 15
```

---
## 3‑vazifa: 1 dan N gacha bo'lgan sonlar yig'indisi
Foydalanuvchi kiritgan `N` sonigacha bo'lgan barcha natural sonlar yig'indisini hisoblang.

**Formula:** `N * (N + 1) // 2` (tezkor usul) yoki sikl bilan qo'shish.

**Namuna:**
```
N = 5  -> Yig'indi = 15   (1 + 2 + 3 + 4 + 5)
```

---
## 4‑vazifa: 3 ta sondan eng katta va eng kichigi
Foydalanuvchi kiritgan 3 ta sondan:
- Eng kattasini toping
- Eng kichigini toping

**Maslahat:** `max(a, b, c)` va `min(a, b, c)` yoki ketma‑ket solishtirish.

**Namuna chiqishi:**
```
Eng kichik: 4
Eng katta: 27
```

---
## 5‑vazifa: Ismlar ro'yxatini to'plash
Foydalanuvchi ism kiritadi va ular listga qo'shiladi. `"stop"` (kichik harflarda) kiritilganda jarayon to'xtaydi.

**Maslahat:** `while True:` va `break` ishlating.

**Namuna:**
```python
Ismlar: ["Ali", "Vali", "Hasan"]
```

---
## 6‑vazifa: Sonlar va ularning kvadrati jadvali
1 dan 10 gacha bo'lgan sonlar uchun jadval chiqaring: `son - kvadrat`.

**Kutilyotgan format:**
```
Son  Kvadrat
1    1
2    4
3    9
...
10   100
```

**Maslahat:** Jadvalni tekis ko'rsatish uchun `print(f"{son:<4}{son**2}")` dan foydalaning.

---
### Qo'shimcha g'oyalar
- 2‑vazifaga 7 ga bo'linadigan sonlar uchun qo'shimcha matn qo'shishga urinib ko'ring.
- 5‑vazifada: Ism uzunligini ham chiqarish (`len(ism)`).
- 6‑vazifada: Kvadrat o'rniga kub jadvali ham sinab ko'ring.

Omad! Har bir vazifani alohida fayl yoki alohida funksiyada bajarish strukturani tartibli qiladi.