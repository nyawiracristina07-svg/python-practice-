#1
fruits = ["apple","banana","cherry"]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[-1])

#2
days = ["Monday", "Tuesday", "Wendesday", "Thursday", "Friday"]

days[2] = "Wednesday"
print(days)
print(days[-3:])

#3
animals = ["cat", "dog", "apple"]
animals.pop()
print(animals)
animals.append("rabbit")#last position
print(animals)
animals.insert(0,"horse")
print(animals)

#4
fishes = ["catfish", "perch", "cod", "carp"] 
print(fishes[-2:])
##### come back********
print(fishes[len(fishes) - 1])
fishes[1] = "Tilapia"
print(fishes)

#5
bits = [0, 0, 1, 0, 1, 1]
print(bits.count(0))
print(bits.index(1,1))
print(2 in bits)

#6
a = [1, 2]
a.append([3, 4])
print(a, len(a))
#length = 3
b = [1, 2]
b.extend([3, 4])
print(b, len(b))
#length = 4
#this is because the first one adds the entire list as a whole thus making it seem like one item.the second one just adds the numers into the original list coz of the function "extend""

#7
grades = [12, 18, 9, 15]
print(sorted(grades,reverse=False))
print(grades)
grades = sorted(grades,reverse=True)
print(grades)

#reverse=False → Smallest to biggest (default).
#reverse=True → Biggest to smallest.
#sorted() → Creates a new sorted list.
#sort() → Modifies the original list.

# a)
colors = ["red", "blue", "green"]
print(colors[2]) #IndexError: list index out of range
# b)
colors.remove("blue") #ValueError: list.remove(x): x not in list
# c)
nums = [3, 1, 2]
nums = sorted(nums)
print(nums[0])#TypeError: 'NoneType' object is not subscriptable




