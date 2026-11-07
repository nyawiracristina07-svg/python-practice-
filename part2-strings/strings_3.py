#Hard 
#1
#phrase = input("kindly write a phrase: ").strip().casefold().replace(" ","")

#if phrase == phrase[::-1]:
 #   print("Palindrome")
#else:
  #  print("Not a palindrome")

#2
#come back !!!!
card_number = input("kindly write your card number: ").strip()

if (len(card_number)== 19) and card_number[4::5] == "   " and card_number.replace(" ", "").isdigit() and  card_number.replace(" ", "").isascii():
    print(f"**** **** **** {card_number[-4:]}")
else:
    print("Invalid card number ")

#3
