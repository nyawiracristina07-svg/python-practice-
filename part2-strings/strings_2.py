#Intermediate Strings

#1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"{first_name[0].upper()}. {last_name[0].upper()}.")

#2
email_address = input("Enter your email address: ")

if "@" in email_address and  " " not in email_address and ".com" in email_address or ".fr" in email_address:
    print("Accepted")
    
elif "@" not in email_address:
    print("Refused: no @")
elif " "  in email_address:
    print("Refused: contains a space ")
elif ".com" not in email_address or ".fr" not in email_address  in email_address:
    print("Refused: must end with .com or .fr ")

#3
answer = input("Continue?").strip().lower()

if answer == "yes" or answer == "y":
    print("Confirmed")
elif answer == "no" or answer == "n":
    print("Cancelled")
else:
    print("Please answer yes or no")

#4
first_name = input("Enter your first name: ").lower() 
last_name = input("Enter your last name: ").lower()
year_of_birth = (input("Enter your year of birth: "))

print (f"Username: {last_name[0:4]}{first_name[0]}{year_of_birth[-2:]}")


#5
value = input("Enter a value: ")

if value.isdigit():
    print(f"Doubled {int(value) * 2}" )
elif value.startswith("-") and value[1:].isdigit():
    print(f"Negative number: {value}")
else:
    print("Not a whole number")

#6
item_1 = "Tea" 
price_1 = 3.5
item_2 = "Chocolate cake" 
price_2 = 12.25 
item_3 = "Water" 
price_3 = 1.8

print("="*24)
print(f"{item_1:<16}{price_1:>8.2f}")
print(f"{item_2:<16}{price_2:>8.2f}")
print(f"{item_3:<16}{price_3:>8.2f}")
print("="*24)
print(f"Total {(price_1 + price_2 + price_3):>8.2f}")


#7
#raw string type shiiii
print(r"C:\Users\ada\new_folder")
# i ran this code , imagine instead of running the other stuff first it ran this and gave me this error "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"
print("He said 'Python' is not hard")
print("Name\tAda  Age\t36")

#\t → Horizontal tab (spacing)
#\n → New line
#\\ → Prints a literal backslash

#8
#strange stuff
a, b, c = 12, 15, 18
average = (a + b + c) / 3
print(average)
