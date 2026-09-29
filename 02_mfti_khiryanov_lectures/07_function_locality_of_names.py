# def foo(x) -> int: # 'annotation' another called 'comment'.
#     return x * 2
#
# y = foo(32)
# print(y) # если передаваемый переменный будет не y а х
#          # тогда будет NameError
#
#
#
# # DuckTyping
# def foo(x: str, y: int) -> str:
#     result = x
#     for i in range(y - 1):
#         result += x
#     return result
#
# t = foo("ma", 2)
# print(t)



def count_letters(text : str):
    vowels = set("aeiou")

    result = {
        "Гласных": 0,
        "Согласных": 0
    }

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                result["Гласных"] += 1
            else:
                result["Согласных"] += 1
    return result

print(count_letters("Hello world!"))



def word_count(text: str):
    words = text.split()

    return {
        "total_words": len(words),
        "unique_words": len(set(words))
    }


print(word_count("hello world helo"))


def filter_long_word(words: str, n: int) -> list:
    return [word for word in words if len(word) > n]


words = ["apple", "cat", "banana", "dog"]
print(filter_long_word(words, 3))



def count_numbers(nums: list[int]):
    result = {}

    for num in nums:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    return result

print(count_numbers([1, 2, 2, 3, 1, 1]))