import random,string

vowels = 'aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters= string.ascii_lowercase

letter_input1=input("What do you want ? Enter 'v' for vowels, Enter 'c' for consonants, Enter 'l' for letters: ")
letter_input2=input("What do you want ? Enter 'v' for vowels, Enter 'c' for consonants, Enter 'l' for letters: ")
letter_input3=input("What do you want ? Enter 'v' for vowels, Enter 'c' for consonants, Enter 'l' for letters: ")
print(letter_input1,letter_input2,letter_input3)

def generator():
    if letter_input1=='v':
        letter1=random.choice(vowels)
    elif letter_input1=='c':
        letter1=random.choice(consonants)
    elif letter_input1=='l':
        letter1=random.choice(letters)
    else:
        letter1=letter_input1

    if letter_input2=='v':
        letter2=random.choice(vowels)
    elif letter_input2=='c':
        letter2=random.choice(consonants)
    elif letter_input2=='l':
        letter2=random.choice(letters)
    else:
        letter2=letter_input2

    if letter_input3=='v':
        letter3=random.choice(vowels)
    elif letter_input3=='c':
        letter3=random.choice(consonants)
    elif letter_input3=='l':
        letter3=random.choice(letters)
    else:
        letter3=letter_input3


    name=letter1+letter2+letter3
    return name
for i in range(20):
    print (generator())
