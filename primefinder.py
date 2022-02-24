import numpy as np

print("Type any number greater than 1. To close, type 1 or 0")
run = True
while run == True:
    number = int(input("Number:"))
    if number == 1 or number == 0:
        print("Closed")
        run = False
    elif number == 2 or number == 3:
        square_root = np.sqrt(number)
        print("The root is " + str(square_root))
        print("The number is a prime")
    else:
        print(type(number))
        root = np.sqrt(number)
        r = np.floor(root)
        print('The root is ' + str(root))
        i = 2
        while i <= r:
            i += 1
            factor = number / i
            if factor - np.floor(factor) == 0:
                print("The number is not a prime")
                break
            else:
                while i == r:
                    print("The number is prime")
                    break
