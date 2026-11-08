#Hard 
#1
phrase = input("kindly write a phrase: ").strip().casefold().replace(" ","")

if phrase == phrase[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#2
#come back !!!!
card_number = input("kindly write your card number: ").strip()

if (len(card_number)== 19) and card_number[4::5] == "   " and card_number.replace(" ", "").isdigit() and  card_number.replace(" ", "").isascii():
    print(f"**** **** **** {card_number[-4:]}")
else:
    print("Invalid card number ")

#3
#split conversts a string into a list and title only works on strings not lists 
#come back 
name = input("type your full name: ").title().strip()
print(" ".join(name))

#4
#come back 
time = input("write time in this format h:m: ")
print(time.find(":"))

#5
#come back
sentence = input("write a sentence of several words: ").strip()
print(f"Characters: {len(sentence)}")
print(f"Without spaces: {len(sentence.replace(" ",""))}")
print(f"Words {len(sentence.split())}")
print(f"Letter e : {sentence.casefold().count("e")}")
print(f"First Word: {sentence[:sentence.find(' ')]}")
print(f"Last word: {sentence[sentence.rfind(" ") + 1:]}")
# why the slicing bit though ????????????, why find why rfind???






