"""7.3. Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет."""
number = int(input("Напиши свое число и я скажу четное число или нечетное."))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")