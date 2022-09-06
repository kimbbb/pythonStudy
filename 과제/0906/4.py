def testPrime(n):
    for i in range(2, 101):
        a = 0
        for j in range(2, 101):
            if i % j == 0:
                a += 1

        if a == 1:
            print(i, end=' ')
testPrime(1)