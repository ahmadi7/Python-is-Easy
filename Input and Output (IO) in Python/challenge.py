with open("sample.txt", "a") as sample:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:>2} times {1:2} is {2:<3}".format(i, j, i*j), file=sample)
        print("-" * 40, file=sample)
