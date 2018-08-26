from multiprocessing import Pool
from decimal import Decimal, getcontext
from math import factorial as fac
from time import time
from tqdm import tqdm


def Chud(k):
    k = Decimal(k)
    return (fac(6 * k) * (545140134 * k + 13591409)) / (
        fac(3 * k) * (fac(k)**3) * (-262537412640768000)**k)


def multithread(n):
    try:
        with Pool() as pool:
            results = list(tqdm(pool.imap_unordered(Chud, range(n)), total=n))
    except Exception as ex:
        print("Calculating pi Failed.")
        print(ex)
        print("Calculated {0} rounds".format(len(results)))
    pi = Decimal(426880 * Decimal(10005).sqrt()) / sum(results)
    return pi


def checkpi(pi):
    pi = str(pi)
    with open("pi.txt", "r") as f:
        content = f.read()
    for i in range(len(content)):
        if content[i] == pi[i]:
            pass
        else:
            return i


def base16(number):
    length = len(str(number)) - 1
    hexdecimal = "0123456789ABCDEF"
    remaining = number
    b16 = ""
    towrite = round(remaining - Decimal(0.5))
    b16 += hexdecimal[towrite]
    remaining -= towrite
    for n in range(length - 1):
        towrite = round(16 * remaining - Decimal(0.5))
        b16 += hexdecimal[towrite]
        remaining = remaining * 16 - towrite
    return b16


if __name__ == "__main__":
    if True:
        digits = int(input("Number of digits: "))
        rounds = round(digits / 1.0128 / 14 + 0.5)
        getcontext().prec = round(digits * 1) + 2
        print("Calculating {0} rounds of pi.".format(rounds))
        start = time()
        pi = multithread(rounds)
        end = time()
        # b16pi = base16(pi)
        print("Calcualted pi. Time taken: {0} seconds".format(end - start))
        print("Time per round = {0} seconds".format((end - start) / rounds))
        checked = checkpi(pi)
        print("Total correct: {0}".format(checked))
        # validation = validatePI()
        # print("Checked {0} digit: {1}".format(checked, ))
        if "y" in input("Want me to display pi? ").lower():
            pi = Decimal(str(pi)[:checked + 1])
            print(pi)
            # print(b16pi[1000])
    else:
        pi = multithread(rounds)
        print(pi)
