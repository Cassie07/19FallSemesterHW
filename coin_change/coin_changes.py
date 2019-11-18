import sys
import math

# initial
quarter = 25
dime = 10
nickel = 5
penny = 1
coin_list = [penny, nickel, dime, quarter]

def dynamic_programming(n):
    if n < 0:
        raise Exception("Wrong Number")

    if n == 0:
        return 0

    len_table = [0] + [sys.maxsize]*n
    dp_item = [0] + [sys.maxsize]*n
    for i in range(1, n+1):
        for coin in coin_list:
            if coin <= i:
                remain = i - coin
                if len_table[i] > len_table[remain] + 1:
                    len_table[i] = len_table[remain] + 1
                    dp_item[i] = coin
    temp = n
    res = []
    while temp > 0:
        res.append(dp_item[temp])
        temp = temp - dp_item[temp]

    return len_table[n], sorted(res)

def greedy(n):
    if n < 0:
        raise Exception("Wrong Number")

    if n == 0:
        return 0

    res = []
    for coin in reversed(coin_list):
        if n >= coin:
            times = int(n / coin)
            n = n % coin
            res = res + [coin] * times
    return len(res), sorted(res)

if __name__ == '__main__':
    test_nums = [5, 30, 82, 365]
    i = 1
    for num in test_nums:
        print("[Test {}]".format(i))
        print("coin changes for: ", num)
        length_dp, res_dp = dynamic_programming(num)
        print("[Dynamic Programming] the change for the fewest number of coin is: {}".format(length_dp))
        length_greedy, res_greedy = greedy(num)
        print("coins: ", res_dp)
        print("[Greedy algorithm] the change for the fewest number of coin is: {}".format(length_greedy))
        print("coins: ", res_greedy)
        print()
        i += 1
