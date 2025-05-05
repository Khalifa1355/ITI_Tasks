def print_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * i)


def print_from_list(height):
    L = [" "] * height
    for index in range(1,len(L)+1) :
        L.pop(0)
        L.append("*")
        print("".join(L))

print_from_list(6)


print_triangle(6)