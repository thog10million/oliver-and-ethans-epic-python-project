# 7

slogan = 'My school is the best'
print(slogan[2])
print(slogan[8])
print(slogan[20])
print(slogan[1])
# print(slogan[25]) - breaks

# 8
print(slogan[:5])
print(slogan[17:])

# 9
print(slogan[:13] + 'awesome!')

# 10
activity = 'theater'
print(len(activity))
print(activity[0:len(activity)])


# 12
def how_eligible(text):
    points = 0
    if '?' in text:
        points += 1
    if '"' in text:
        points += 1
    if ',' in text:
        points += 1
    if '!' in text:
        points += 1
    return points


print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

print(len('How many characters are in this sentence?'))
