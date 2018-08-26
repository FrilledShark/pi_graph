from decimal import Decimal, getcontext
from time import time
from multiprocessing import Pool

rounds = 1421

prec = rounds
getcontext().prec = 10000

def BBP(k):
    k = Decimal(k)
    return 1/(16**k) * (4 /(8*k + 1) -2 /(8*k + 4)-1 /(8*k + 5)-1 /(8*k + 6))

# Calculating π
# Using Bailey–Borwein–Plouffe formula
# https://en.wikipedia.org/wiki/Bailey–Borwein–Plouffe_formula
# picorrect = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)

def singlethread():
    results = []
    start = time()
    # for item in range(rounds):
    #     results.append(BBP(item))
    end = time()
    return [sum(results), end-start]

def multithread():
    with Pool(4) as pool:
        results = pool.map(BBP, range(rounds))
    return sum(results)

def checkpi(pi):
    pi = str(pi)
    with open("pi.txt", "r") as f:
        content = f.readlines()
    piRead = content[0]
    for i in range(len(piRead)):
        if piRead[i] == pi[i]:
            pass
        else:
            return i+1



if __name__ == "__main__":
    if True:
        print("Calculating {0} rounds of pi.".format(prec))
        start = time()
        pi = multithread()
        end = time()
        print("Calcualted pi. Time taken: {0} seconds".format(end - start))
        print("Time per round = {0} seconds".format((end - start)/rounds))
        print("Total correct: {0}".format(checkpi(pi)))
    else:
        mt = multithread()
        print(mt[0])
