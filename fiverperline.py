START = 1000
END = 2000
INTS_PER_LINE = 5

for i in range(START, END):
    print(str(i) + ' ')
    if i % INTS_PER_LINE == INTS_PER_LINE - 1:
        print("")