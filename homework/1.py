import random

matrix = []

for j in range(3):
    row = []
    for m in range(100):
        number = random.randint(3,99)
        isPrime = True
        for i in range(2, number):
            if (number % i) == 0:
                isPrime = False
                break
        if isPrime == True:
            row.append(number)
            if len(row) == 3:
                break
            else:
                continue
    matrix.append(row)

for n in range(3):
    print(matrix[n])

       