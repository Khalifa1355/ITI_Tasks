def generate_multiplication_table():
    number = int(input("Enter a number: "))
    bigTable = []

    for i in range(1, number + 1):
        smalltable = []
        for j in range(1, i + 1):
            result = i * j
            smalltable.append(result)
            print(f"{i} x {j} = {result}")
        print(smalltable)
        bigTable.append(smalltable)

    print(bigTable)


def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"{j}x{i}={j*i}", end=" ")
        print()




if __name__ == "__main__":
    generate_multiplication_table()
    multiplication_table()