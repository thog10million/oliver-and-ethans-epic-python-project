# 4
print("\n#4\n")
(1, 2, 3)

# 5
print("\n#5\n")
# camel case
anotherTuple = (4, 5, 6)

# 6
print("\n#6\n")
some_values = ('a', 'b', 3)
print(some_values[1]) # b
print(some_values[0:2]) # a, b

# 7
print("\n#7\n")
a = 10
tup = (9, a, 11)
print(tup[1] == 10) # true
a = 15
print(tup[1]) # 10

# 8
print("\n#8\n")
values = ['a', 'b', 3]
print(values[1:]) # b, 3

# 9
print("\n#9\n")
values[2] = '3' # string
print(values[2] == 3) # integer, false

# 10
print("\n#10\n")
values = values + [4, 5] # will add 4 and 5 to the end of the list
print(values)
values.append([6, 7]) #adds [6, 7] as a single value in the list
print(values)

# 11
print("\n#11\n")
# values = values + 5
# doesn't work because we are trying to add 5 to a list

# 12
print("\n#12\n")
a = 6
a *=3 # a = a * 3, 18
print(a)

# 13
print("\n#13\n")
import random
print(random.choice(values))
print(random.randint(5,8))
print(random.uniform(5,8))

# 14
print("\n#14\n")
def rollTwoDice():
    return random.randint(1,6) + random.randint(1,6)
print(rollTwoDice())

#15
print("\n#15\n")
def guessLetter():
    letters = "abcdefghijklmnopqrstuvwxyz"
    n = random.randint(0,25)
    return letters[n]
print(guessLetter())


