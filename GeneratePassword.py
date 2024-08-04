import random
while True:
    length_password = input("Enter the password length")
    try:
        length_password = int(length_password)
        if isinstance(length_password, int):
            break
    except:
        print("Invalid input, please try again.")
count = 0
password = ""
while length_password > 0:
   length_password -= 1
   random_number =  random.randrange(48,123)
   password += chr(random_number)
print(password)


