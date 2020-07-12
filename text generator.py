import random , string

vowels = 'aeiouy'
consonents = 'bcdfghjklmnpqrstuvwxz'
letters = string.ascii_lowercase

input1 = input("enter 'v' for vowels 'c'for consonents 'l' for any letters: ")
input2 =input("enter 'v' for vowels 'c'for consonents 'l' for any letters: ")
input3 = input("enter 'v' for vowels 'c'for consonents 'l' for any letters: ")
input4 = input("enter 'v' for vowels 'c'for consonents 'l' for any letters: ")

def generator():
    if input1 == 'v':
      letter1 = random.choice(vowels)
    elif input1 == 'c':
      letter1 = random.choice(consonents)
    elif input1 == 'l':
      letter1 = random.choice(letters)
    else:
      letter1= input1

    if input2 == 'v':
          letter2 = random.choice(vowels)
    elif input2 == 'c':
          letter2 = random.choice(consonents)
    elif input2 == 'l':
          letter2 = random.choice(letters)
    else:
          letter2= input2

    if input3 == 'v':
              letter3 = random.choice(vowels)
    elif input3 == 'c':
              letter3 = random.choice(consonents)
    elif input3 == 'l':
              letter3 = random.choice(letters)
    else:
             letter3= input3

    if input4 == 'v':
          letter4 = random.choice(vowels)
    elif input4 == 'c':
          letter4 = random.choice(consonents)
    elif input4 == 'l':
          letter4 = random.choice(letters)
    else:
          letter4= input4

    name=letter1+letter2+letter3+letter4
    return(name)


for i in range(20):
    print(generator())
