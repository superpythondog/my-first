# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:15:32 2024

@author: airbx
"""

def min_coins(M, coins):
    if M == 0:
        return 0
    min_count = float('inf')
    for coin in coins:
        if M >= coin:
            count = min_coins(M - coin, coins) + 1
            if count < min_count:
                min_count = count
    return min_count

# 测试
M = 40
coins = [25, 20, 5, 1]
print("拼成{}元的最小硬币数为：{}".format(M, min_coins(M, coins)))