#!/usr/bin/python

import argparse
# profit = [10, 7, 5, 8, 11, 9]
def find_max_profit(prices):
  max_price = 0
  min_price = prices[0]
  for i in prices:
    min_price = min(min_price, i)
    compare_price = i - min_price
    max_price = max(max_price, compare_price)
  return max_price
# print(find_max_profit)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers)) 