

# ekranga 10 marta salom deb chiqaruvchi


#print("Dastur ishga tushdi")

# for i in range(0, 10, 2):
#    print(i)

#print("Dastur tugadi")



#for i in range(101):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i, " soni 15 bo'linadi")
#    elif i % 5 == 0:
#        print(i, " soni 5 bo'linadi")
#    elif i % 3 == 0:
#        print(i, " soni 3 bo'linadi")
    

#n = int(input("Son kiriting:>"))

#jami = 1

#for i in range(1,  n + 1):
#    jami = jami * i

#print(jami)


# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# pythonda while sikli

# while takrorlash operatori shart rost bo'lsa, takrorlanadi

# son = 0
# while son < 10:
#    print(son)
#    son += 1
#    if son == 5:
#        break


# login = "admin"
# passwd = "admin"



# while True:
#     input_login = input("Loginni kiriting:")
#     passwd_login = input("Parolni kiriting:")
#     if not input_login == login or not passwd_login == passwd:
#         print("Login yoki parol xato")
#         print("\n")
#         print("=" * 30)
#     else:
#         print("Tizimga kirdingiz")
#         break


# for i in range(1, 10):
#     print(i)


# n = 1

# while n < 11:
#     print(n)
#     # n = n + 1
#     n += 1

# n = 11

# while n > 0:
#     n -= 1
    
#     if n == 5:
#         continue
    
#     print(n)
    


# n = 11

# while n > 0:
#     n -= 1
    
#     if n == 5:
#         break
    
#     print(n)



summ = 0

while True:
    n = int(input("Son kiriting:>"))

    if n == 0:
        print("Yigindi: ", summ)
        break

    summ += n


# Topshiriqlar

# 1) 1 dan 100 gacha juft sonlarni chiqarish(while yordamida)

# 2) foydalanuvchidan 0 kiritmaguncha sonlarni qabul qilib, ularni eng kattasini topamiz