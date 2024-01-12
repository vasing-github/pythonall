"""use python design the first game"""


import random
rand = random.randint(1,10)



count = 10
before = 1
bake = 10
while count > 0:
    temp = input("why not guess which number i am think now?")
    guess = int(temp)
    if guess == rand:
        print("are you huichong???")
        print ("no gift even you are right")
        break
    else:
        if guess > rand:
            bake = guess
            print ("too big,",before,bake)
        else:
            before = guess
            print ("too small,",before,bake)
    
    count = count -1
