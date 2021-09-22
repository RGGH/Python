
<span style="color:blue;font-size:40px;">Reverse the vowels in a string</span>

### What you will learn in this tutorial:
# Manipulating lists and debugging

    vowels = ['a', 'e', 'i', 'o', 'u']

## before we do anything else we need to iterate through the string and capture the vowels
## We'll make an empty list and populate it using append

    str = 'microphones'

    lsv = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in str:
        if i in vowels:
            lsv.append(i)

## We can use an f string to see the output

    print(f"list of vowels {lsv}")

## Next, iterate through the vowels in the STRING and replace them with the vowels in our list, in reversed order 
## Making a COPY of our list is a key thing to remember here.  The code will not work otherwise.

    lsv2 = list(lsv)
    answer = []

## Now we can make a function to switch the vowels
## We iterate through EVERY letter in the string

    def reverser():
        for letter in str:

## If the letter is in our COPY of of original list of vowels, we'll substitute it
## with the LAST vowel in our ORIGINAL list, and remove it from our ORIGINAL list

        if letter in lsv2:
            answer.append(lsv[-1])
            lsv.remove(lsv[-1])

        else:
            answer.append(letter)
    return answer

## Now we set our answer to the return value from our function 'reverser' and print it 

    # main
    answer = reverser()
    print(answer)

## Let's test it
## Question : what would have happened if we had not made a copy of the list?
    
    lsv2 = list(lsv)




