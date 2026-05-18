# Nested Try 

user_name = input("Enter your name: ")
password = input("Enter your password: ")

try:
    if user_name == "admin" and password == "M1racle@123":
        print("Login successful!")
    else:
        raise ValueError("Invalid username or password.")

    try:
        with open("Example.txt","r") as file:
            content = file.read()
            print(content)

    except FileNotFoundError as e:
        print(e)

except ValueError as e:
    print(e)

finally:
    print("Login attempt completed.")



# with open("04_TryException.py","a") as file:
#     file.write(""" 
#         user_name = input("Enter your name: ")
#         password = input("Enter your password: ")

#         try:
#             if user_name == "admin" and password == "M1racle@123":
#                 print("Login successful!")
#             else:
#                 raise ValueError("Invalid username or password.")

#             try:
#                 with open("Example.txt","r") as file:
#                     content = file.read()
#                     print(content)

#             except FileNotFoundError as e:
#                 print(e)

#         except ValueError as e:
#             print(e)

#         finally:
#             print("Login attempt completed.")
#             """)