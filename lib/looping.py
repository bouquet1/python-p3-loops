#!/usr/bin/env python3

#while loop version
def happy_new_year():
    i = 10
    while i >= 0:  # Change the condition to include 0 in the loop
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)
        i -= 1

happy_new_year()


def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list

result = square_integers([1, 2, 3, 4, 5])
print(result) #boyle deyince sonucu yazdirdim [1, 4, 9, 16, 25]

def fizzbuzz():
    for num in range(1, 101):
        if (num %3 == 0 and num %5 == 0):
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
fizzbuzz()

# Python while loop syntax
# i = 0
# while i < 5:
#     print("Looping!")
#     i += 1


# python for loop syntax
# for i in range(10):
#     print("Looping!")
#     print(f"i is: {i}")
