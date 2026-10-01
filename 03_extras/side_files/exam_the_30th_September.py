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



def digit_s(nums: int):
    if nums == 0:
        return 0
    sd = 0
    str_num = str(nums)
    for s_n in str_num:
        if s_n.startswith("-"):
            continue
    return sd


print(digit_s(32))

num = -100
num = -1 * num
print(num)


def digit_s(nums: int):
    summ_digital = 0
    for num in str(abs(nums)):
        summ_digital += int(num)
    return summ_digital

print(digit_s(32))
print(digit_s(-32))


def unique_once(nums: list[int]) -> list[int]:
    uniq_s = {}
    for num in nums:
        uniq_s[num] = uniq_s.get(num, 0) + 1

    return [num for num in nums if uniq_s[num] == 1]

print(unique_once([1, 2, 3, 3, 4]))


def char_count(text: str) -> dict:
    char_c = {}
    for char in text:
        # if char in char_c:
        char_c[char] = char_c.get(char, 0) + 1

    return char_c


print(char_count("hello"))



def longest_word(text: list[str]) -> list[str]:
    c_text = ""
    for char in text:
        if len(char) > len(c_text):
            c_text = char

    return [c_text]


print(longest_word(["elephant", "cat", "dog", "elephants", "elephantss"]))


def sort_employees(texts):
    return sorted(
        texts,
        key=lambda epmployee: (-epmployee["salary"], epmployee["name"])
    )
data = [
    {"name": "Bek",
     "salary": 500},
    {"name": "Aida",
     "salary": 700},
    {"name": "Azat",
     "salary": 500},
]
print(sort_employees(data))