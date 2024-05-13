
import random
import math

def Hesabla():
    random_ededler = []
    while len(random_ededler) < 5:
        number = random.randint(20, 50)
        if number % 2 == 0:
            random_ededler.append(number)
    cut_ededler = list(map(lambda num: num ** 2, random_ededler))

 
    return cut_ededler
result = Hesabla()
print("kvadrata yukselmis ededler: ", result)
