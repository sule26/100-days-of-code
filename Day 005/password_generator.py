import random 
import string

letters = list(string.ascii_letters)
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
numbers = ["0" ,"1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []

for i in range(0, nr_letters):
  password_list.append(random.choice(letters))

for i in range(0, nr_symbols):
  password_list.append(random.choice(symbols))
  
for i in range(0, nr_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)

print(f"Here is your password: {password}")
