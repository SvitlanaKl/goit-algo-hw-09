# Маємо набір монет [50, 25, 10, 5, 2, 1]. 
# Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.
# Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:
# Функція жадібного алгоритму find_coins_greedy; Функція динамічного програмування find_min_coins.

# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            if num_coins > 0:
                result[coin] = num_coins
    return result

# Приклад використання
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))

# Функція динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Приклад використання
amount = 113
print("Динамічне програмування:", find_min_coins(amount))
