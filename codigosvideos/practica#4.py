def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [2, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)