

# numbers = [1, 2, 3, 4, 5, 6]
# squares = []

# for num in numbers:
#     if num % 2 == 0:
#         squares.append(num ** 2)

# print(squares)  # [4, 16, 36]

# List comprehension
# squares = [num ** 2 for num in numbers if num % 2 == 0]





# my_list = list(range(1, 11))
# print(my_list)

# my_list = [son for son in range(1, 11) if son % 2 == 0]
# print(my_list)





# 1. Oddiy nusxa ko'chirish
# names = ["Ali", "Vali", "Sardor"]
# upper_names = [name.upper() for name in names if name != "Bobur"]
# # # ['ALI', 'VALI', 'SARDOR']

# upper_names = []
# for name in names:
#     if name != "Bobur":
#         upper_names.append(name.upper())


# # 2. Matematik amal
# squares = [x**2 for x in range(1, 11)]          # 1 dan 10 gacha kvadratlari

# # 3. Filter + transform
users = [
    {"id": 1, "name": "Ali", "age": 25, "is_active": True},
    {"id": 2, "name": "Vali", "age": 17, "is_active": False},
    {"id": 3, "name": "Sardor", "age": 30, "is_active": True},
]

# active_adults = [u["name"] for u in users if u["age"] >= 18 and u["is_active"]]

active_adults = []
for user in users:
    if user['age'] > 18 and user['is_active']:
        active_adults.append(user['name'])

# print(active_adults)

# # ['Ali', 'Sardor']

# # 4. String bilan ishlash (backendda juda kerak)



# emails = ["ali@gmail.com", "test@spam.ru", "vali@yahoo.com", "bot@spam.com"]
# clean_emails = [email for email in emails if email.endswith("@spam.com")]
# print(clean_emails)

# # ['ali@gmail.com', 'test@spam.ru', 'vali@yahoo.com']

# # 5. Nested (ichma-ich)
# 
#  
matrix = [[1, 2], [3, 4], [5, 6]]

flat = [num for row in matrix for num in row]

# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
print(flat)

# # [1, 2, 3, 4, 5, 6]

