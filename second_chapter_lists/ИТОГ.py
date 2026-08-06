# """В этой главе вы узнали, что собой представляют списки и как работать с отдельными элементами в списках. Вы научились определять списки, добавлять и удалять
# элементы, выполнять сортировку (постоянную или временную для отображения).
# Также вы узнали, как определить длину списка и как избежать ошибок индексирования при работе со списком.
# В главе 4 рассматриваются приемы более эффективной работы со списками. Перебор всех элементов списка всего в нескольких строках кода, даже если список содержит тысячи или миллионы элементов, сокращает объем программы."""
# print(f"Popped last digital this: {numbers.pop()}")

# print(f"Before: {sorted(numbers)}")
#
# print(f"After: {numbers}")
#
# print(f"{numbers}")
#
# numbers.sort(reverse=True)
# print(f"\n{numbers}")
# numbers.sort()
# print(f"\n{numbers}")



# numbers.sort(reverse=True)
# print(numbers)
numbers = [9, 10, 3, 7, 2, 5, 4, 8, 6, 1]
# print(len(numbers))
def sort_num(arr):
    n = arr.copy()
    length = len(n)
    for inx in range(length):
        for j in range(0, length - inx - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

sorted_numbers = sort_num(numbers)
print(sorted_numbers)

#         if v <= nn:
#             n.append(v)
#     return n
# print(sort_num(numbers))
