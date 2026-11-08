#1
plate = input("write a number plate: ").upper().strip()

if  len(plate) != 9:
    print("Wrong length")
elif plate[2] != '-' or plate[6] != '-':
    print("Dashes misplased")
elif not  plate[0:2].isalpha() or not plate[3:6].isdigit() or not plate[7:9].isalpha():
    print("Wrong characters")
elif "I" in plate or "O" in plate or "U" in plate:
    print("Forbidden letter")
else:
    print(f"Valid plate: {plate}")

#2
password = input("kindly input a password: ").strip()

#at least 8 characters
#at least 12 characters
# an uppercase letter
# a lowercase letter
# a digit
# display the score and verdict
characters_8 = len(password) >= 8
characters_12 = len(password) >= 12

uppercase = password.lower() != password
lowercase = password.upper() != password

digit = password.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")


score = 0
if characters_8:
    score += 1

if characters_12:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1
if len(password) > len(digit):
    score += 1


if score <= 2:
    verdict = "Weak"
elif score <= 4:
   verdict = "medium"
else:
    verdict = "strong"

print(f"Score: {score}/5, {verdict}")


