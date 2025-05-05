def count_vowels(x):
    x = x.lower()
    y = "aeiou"
    c = 0
    for i in range(len(x)):
        if x[i] in y:
            print(f"found vowel : {x[i]}")
            c += 1
    print(f"Total number of vowels : {c}")

def find_i_location(x):
    x = x.lower()
    for i in range(len(x)):
        if x[i] == 'i':
            print(f"location of 'i' = {i}")







def sort_numbers(number_list):
    # Use the provided list directly
    numbers = number_list.copy() 
    # Sort the list in ascending order
    ascending_order = sorted(numbers)

    # Sort the list in descending order
    descending_order = sorted(numbers, reverse=True)

    # Display the results
    print("\nOriginal List:", numbers)
    print("Sorted in Ascending Order:", ascending_order)
    print("Sorted in Descending Order:", descending_order)
    print("========================================================")



sort_numbers([5, 2, 8, 1, 9])  # Sort numbers

count_vowels("htis is my name")
find_i_location("i is my i")