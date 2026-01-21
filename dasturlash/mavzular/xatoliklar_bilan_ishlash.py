

# def main():

#     try:
#         son1 = int(input("1-sonni kiriting:>>"))
#         son2 = int(input("2-sonni kiriting:>>"))
#     except Exception as err:
#         print(err)
#         print("Faqat son kiriting")
    

#     # bolinma = son1 / son2
#     # print(bolinma)

#     try:
#         bolinma = son1 / son2
#         print(bolinma)
#     except ZeroDivisionError as err:
#         print(err)
#         print("Noma'lum xatolik")
#     except ValueError as err2:
#         pass
    
#     finally:
#         print("Har qanaqa holatda ishlayman")

#     print("Yaxshi")

# main()





# import math


# son = -16

# print(math.sqrt(son))


# Logical errors are the most subtle because the 
# code runs without crashing and without producing 
# any error messages. The program simply produces 
# an incorrect or unintended result due to flawed 
# logic in the code itself. 





def main():
    matn = input(">>>").lower()

    sozlar = matn.split()

    unikal_sozlar = set(sozlar)

    natija = {}

    for soz in unikal_sozlar:
        natija[soz] = sozlar.count(soz)
    
    print(natija)

main()
