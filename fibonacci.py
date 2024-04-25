def fibo():
    a = int(input("enter the range: "))
    for i in range(1, a):
        n = int(input("ENTER THE NUMBER: "))
        i = 0
        start = 0
        num_1 = 1
        while i < n:#1<10
            print(start)
            result = start + num_1
            start = num_1
            num_1 = result
            i += 1
fibo()