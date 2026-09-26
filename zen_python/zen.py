# bruteforce
another_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even_or_odd(numbers):
    is_even = []
    is_odd = []
    for number in numbers:
        if number % 2 == 0:
            is_even.append(number)
        else:
            is_odd.append(number)
    return is_even, is_odd

even_numbers, odd_numbers = is_even_or_odd(another_count)
print(f"Чётные: {even_numbers}")
print(f"Нечётные: {odd_numbers}")

# list comprehension
even_numbers = [n for n in another_count if n % 2 == 0]
odd_numbers = [n for n in another_count if n % 2 != 0]

print(f"Чётные: {even_numbers}")
print(f"Нечётные: {odd_numbers}")