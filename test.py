# original_data = {
#     "divisions": [
#         {
#             "id": "1",
#             "name": "Barishal",
#             "bn_name": "বরিশাল",
#             "lat": "22.701002",
#             "long": "90.353451"
#         },
#         {
#             "id": "2",
#             "name": "Chattogram",
#             "bn_name": "চট্টগ্রাম",
#             "lat": "22.356851",
#             "long": "91.783182"
#         },
#         {
#             "id": "3",
#             "name": "Dhaka",
#             "bn_name": "ঢাকা",
#             "lat": "23.810332",
#             "long": "90.412518"
#         },
#         {
#             "id": "4",
#             "name": "Khulna",
#             "bn_name": "খুলনা",
#             "lat": "22.845641",
#             "long": "89.540328"
#         },
#         {
#             "id": "5",
#             "name": "Rajshahi",
#             "bn_name": "রাজশাহী",
#             "lat": "24.363589",
#             "long": "88.624135"
#         },
#         {
#             "id": "6",
#             "name": "Rangpur",
#             "bn_name": "রংপুর",
#             "lat": "25.743892",
#             "long": "89.275227"
#         },
#         {
#             "id": "7",
#             "name": "Sylhet",
#             "bn_name": "সিলেট",
#             "lat": "24.894929",
#             "long": "91.868706"
#         },
#         {
#             "id": "8",
#             "name": "Mymensingh",
#             "bn_name": "ময়মনসিংহ",
#             "lat": "24.747149",
#             "long": "90.420273"
#         }
#     ]
# }

# converted_data = []

# for division in original_data["divisions"]:
#     converted_data.append({
#         "model": "bangladesh.division",
#         "pk": int(division["id"]),
#         "fields": {
#             "name": division["name"],
#             "bn_name": division["bn_name"],
#             "lat": division["lat"],
#             "long": division["long"]
#         }
#     })

# print(converted_data)


# District list 
# from random import * 
# import os 

# u_pass =input("Enter your password: ")
# pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5', '6']
# pw=""
# while (pw!=u_pass):
#     pw=""
#     for letter in range(len(u_pass)):
#         guess_pwd = pwd[randint(0,17)]
#         pw=str(guess_pwd)+str(pw)
#         print(pw)
#         print("Password is checking... please wait...")
#         os.system("cls")
# print("Your password is: ",pw)


from random import randint
import os

u_pass = input("Enter your password: ")
pwd = 'abcdefghijklmnopqrstuvwxyz123456'
pw = ""

while pw != u_pass:
    pw = ""
    for _ in range(len(u_pass)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw += guess_pwd
    print("Password is checking... please wait...")
    os.system("cls")  # Use "clear" on macOS/Linux, or "cls" on Windows

print("Your password is: ", pw)

