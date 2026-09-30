def get_unique_number(numbers: list[int]) -> list[int]:
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return [num for num, count in counts.items() if count == 1]

data = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9]
lenght_unique_n = get_unique_number(data)
print(get_unique_number(data))
print(len(lenght_unique_n))

from collections import Counter

def count_number(nums: list[int]) -> list[int]:
    return dict(Counter(nums))

print(count_number(data))



# bruteforce
another_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even_or_odd(numbers: list[int]) -> list[int]:
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


def isPalindrome(s: str) -> bool:
    cleaned = [char.lower() for char in s if char.isalnum()]

    return cleaned == cleaned[::-1]

print(isPalindrome("Was it a car or a cat I saw?"))  # True
print(isPalindrome("tab a cat"))
