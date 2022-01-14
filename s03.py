# print("salam")
#
# valid_username = "mohammad"
# valid_password = "mft123"
#
# username = input("please enter username: ")
# password = input("please enter password:")
#
# if username == valid_username and password == valid_password:
#     print("welcome")
# else:
#     print("username or password is not valid!")


# valid_username1 = "mohammad"
# valid_password1 = "mft123"
#
# valid_username2 = "ali"
# valid_password2 = "123"
#
# username = input("usename: ")
# password = input("password: ")
#
# if (username == valid_username1 and password == valid_password1) or (username == valid_username2 and password == valid_password2):
#     print("welcome!")
# else:
#     print("username or password in wrong!")


# age = int(input("please enter your age:"))

# if age <= 8:
#     print("koodak")
# else:
#     if age <= 18:
#         print("nojavan")
#     else:
#         if age <= 30:
#             print("javan")
#         else:
#             if age <= 60:
#                 print("miansal")
#             else:
#                 print("taze aval chelchelite!")

# if 0 < age <= 8:
#     print("koodak")
# if 8 < age <= 18:
#     print("nojavan")
# if 18 < age <= 30:
#     print("javan")
# if 30 < age <= 60:
#     print("miansal")
# if age > 60:
#     print("taze aval chelchelite!")


# if age <= 8:
#     print("koodak")
# elif age <= 18:
#     print("nojavan")
# elif age <= 30:
#     print("javan")
# elif age <= 60:
#     print("miansal")
# else:
#     print("taze aval chelchelite!")


# valid_username1 = "mohammad"
# valid_password1 = "mft123"
#
# valid_username2 = "ali"
# valid_password2 = "123"
#
# username = input("usename: ")
# password = input("password: ")
#
# if username == valid_username1 and password == valid_password1:
#     print("welcome!", valid_username1)
# elif username == valid_username2 and password == valid_password2:
#     print("welcome!", valid_username2)
# else:
#     print("username or password in wrong!")



valid_username1 = "mohammad"
valid_password1 = "mft123"

valid_username2 = "ali"
valid_password2 = "123"

username = input("usename: ")
password = input("password: ")

if username == valid_username1:
    if password == valid_password1:
        print("welcome")
    else:
        print("wrong password")

elif username == valid_username2:
    if password == valid_password2:
        print("welcome")
    else:
        print("wrong password")
else:
    print("wrong username!")














