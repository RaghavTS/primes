import numpy as np
import matplotlib.pyplot as mp
run = True
while run:
    last_limit = int(input("Provide an upper limit:  "))
    if last_limit == 0 or last_limit == 1:
        run = False
    permission = input("Show the primes:  ")
    permission_num = input("Show the number of primes:  ")
    for limit in range(2, last_limit+1):
        i = 2
        n = 1
        while i <= limit - 1:
            i += 1
            prime = True
            r = np.floor(np.sqrt(i)) + 1
            for j in range(2, int(np.floor(np.sqrt(i)) + 1)):
                factor = i / j
                delta = np.floor(factor) - factor
                if delta == 0.0:
                    r = j
                    prime = False
                    break
            if prime == True:
                n += 1
                if permission == 'Y':
                    print(i)
        print("Upto " + str(limit))
        if permission_num == 'Y':
            print("Number of primes= " + str(n))
        percentage = (n*100)/limit
        print("Percentage of primes="+str(percentage))
    #mp.plot(limit, n)
    #mp.show()
