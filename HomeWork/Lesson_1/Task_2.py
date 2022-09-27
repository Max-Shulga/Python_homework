# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# -------------------------------------------------------------------------------------------------------------

x = input("input something: ")
y = input("input something: ")
z = input("input something: ")

if not(x or y or z) == (not x and not y and not z):
    print('true')
else :
    print('false')




# def try_to_int(str):
#     if str.isdigit() == True:
#         str = int(str)
#     return str

# try_to_int(x)
# try_to_int(y)
# try_to_int(z)