
# Bu fayldan kodlar export qilinadi


def salom_ber(name: str):
    print(f"Salom, {name}!")
# va boshqa fayllarda import qilinishi mumkin



def kvadrat(x: int):
    return x * x
# Bu funksiya berilgan sonning kvadratini hisoblaydi


name = "Ali"

age = 25
# Bu o'zgaruvchilar boshqa fayllarda import qilinishi mumkin

# Import qilish orqali boshqa fayllardagi funksiyalar va o'zgaruvchilarni ishlatish mumkin



def factorial(n: int):
    """Berilgan sonning faktorialini hisoblaydigan funksiya"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)