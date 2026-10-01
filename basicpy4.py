import math
number = int(input("Enter a number?"))
if number 
    print(number, "is not a perfect number")
else:
    is_perfect = True
    for i in range(1, number):
        if number % i ==0:
            is_perfect=False
            break

    if is_perfect:
        print(number, "is a perfect number")
    else:
        print(number, "is not a perfect number")
        