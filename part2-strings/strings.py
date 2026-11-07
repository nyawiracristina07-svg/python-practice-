#1
name = input ("What is your name? ")

print(f"First: {name[0]}")
print(f"Last: {name[-1]}")
print(f"Length: {len(name)}")

#2
word = "Programming"
print(f"{word[0:3]},{word[3:7]},{word[7:11]}")
print(word[-3:])
print(word[1:-1])

#3
digits = "0123456789"
print(f"{digits[0:-1:2]},{digits[-9::2]}")
print(digits[-10::3])
print(digits[2:-1:2])
print(digits[10:0:-1])
print(digits[-2::-2])
print(digits[-3:-8:-1])
print(digits[2:7:-1])
 # [last print] This will print an empty string because the start index is greater than the end index and the step is negative

#4
text = " hELLO wORLD "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.upper().strip())
print(text) 
# the text variable remains the same undless reassigned

#5
sentence = "Python is easy to learn and Python is fun"
print(sentence.index("Python",0))
print(sentence.find("Java"))
print(sentence.count("Python"))
print(sentence.replace("fun","powerful"))
print(sentence.startswith("Python")) 
print(sentence.endswith("!")) 

#6
name = "Martin"
age = 23
city = "Nairobi"

print(f"{name} is {age} years old and lives in {city}.")
print(f"Next year,{name} will be {age + 1 }")

#7 --crazyshiet 
price = 1234.5678
rate = 0.0825
print(f"{round(price,2)}, {round(price,2):,}, {rate:.1%} [{price:>12.2}]")


#8
#how can see all the methods available for a string object?
#print(dir(str))

# a)
word = "Python"
word = "J" + word[1:]
print(word)
#TypeError: 'str' object does not support item assignment
# b)
print(word[3])
#IndexError: string index out of range
# c)
age = 20
print(f"Age: {age}")
#TypeError: can only concatenate str (not "int") to str

