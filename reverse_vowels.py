str = 'microphones'

lsv = []
vowlels = ['a', 'e', 'i', 'o', 'u']

for i in str:
    if i in vowlels:
        lsv.append(i)

print(f"list of vowels {lsv}")

# make a copy of the list, to use when iterating through the main string
# otherwise if you have 2 or more of one vowel you can miss some by the end
lsv2 = list(lsv)
answer = []

def check():
    for letter in str:

        if letter in lsv2:
            answer.append(lsv[-1])
            lsv.remove(lsv[-1])

        else:
            answer.append(letter)
    return answer

# main
answer = check()
print(answer)
