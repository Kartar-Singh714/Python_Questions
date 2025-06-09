def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result

print(square_list([10,23,45]))