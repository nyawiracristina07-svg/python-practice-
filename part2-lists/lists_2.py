#1
integers = [0, 1, 3]
integers.append(4)
integers.insert(2,2)
integers.extend( [5, 6, 7])
integers.pop(0)
print(integers)

#2
floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]
print(floats[1:4])
print(floats[2:])
print(floats[0:5])
print(sorted(floats,reverse=True))
print(floats[-2::-2])

#3
record = ["abc", False, 1, 3.14159]
record[1:3]= [True, 0]
print(record)
strings, boolean, integer, floats = record
print(record)
###wtff
first, *others = record
print(first)
print(others)


