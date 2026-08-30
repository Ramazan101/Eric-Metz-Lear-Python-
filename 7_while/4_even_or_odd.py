nums = input("Enter a number, and I'll tell you it's even or odd: ")
nums = int(nums)

if nums % 2 == 0:
    print(f"\nThe number {nums} is even.")
else:
    print(f"\nThe number {nums} is odd")