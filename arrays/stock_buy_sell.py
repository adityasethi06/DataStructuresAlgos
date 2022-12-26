def max_profit(prices):
    max_profit = 0
    buy_ind, sell_ind = 0, 1
    while sell_ind < len(prices):
        if prices[buy_ind] < prices[sell_ind]:
            max_profit = max(prices[sell_ind] - prices[buy_ind], max_profit)
        else:
            buy_ind = sell_ind
        sell_ind += 1
    return max_profit


if __name__ == '__main__':
    print(max_profit([7,6,5,1,4,8,4]))