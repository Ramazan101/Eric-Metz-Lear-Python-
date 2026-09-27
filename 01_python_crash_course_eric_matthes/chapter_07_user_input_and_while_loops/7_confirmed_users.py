# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.

unconfirmed_users = ["alice", "brain", "candace"]
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying users: {current_users.title()}.")
    confirmed_users.append(current_users)

# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for current_user in confirmed_users:
    print(current_user.title())