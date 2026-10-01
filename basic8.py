def extract_even(numbers):
    result = []

    for number in numbers:
        if number %2 == 0:
           result.append(number)
    return result
numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))